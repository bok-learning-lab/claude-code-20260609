(function () {
  "use strict";
  var C = window.CORPUS;

  // This page is LOCAL-ONLY by design. Normalize every video to a local
  // HTML5 source regardless of what the pipeline emitted, so a regenerated
  // corpus-data.js (which may mark a video "youtube") never reintroduces an
  // embed here.
  //
  // The site lives at outputs/site/, so inputs/ is two levels up. Recompute
  // every file path (overriding whatever corpus-data.js contained) so the
  // correct depth is guaranteed. If you relocate the site, change this prefix.
  var INPUTS_PREFIX = "../../inputs/";
  C.videos.forEach(function (v) {
    v.source_type = "local";
    v.youtube_id = null;
    v.file = INPUTS_PREFIX + v.source_id + ".mp4";
  });

  var uById = {};
  C.utterances.forEach(function (u) { uById[u.utterance_id] = u; });
  var vById = {};
  C.videos.forEach(function (v) { vById[v.source_id] = v; });
  var spById = {};
  C.speakers.forEach(function (s) { spById[s.speaker_id] = s; });

  function fmt(t) {
    // Keep sub-second precision visible: the pipeline emits float seconds
    // (e.g. 14.16) and we seek to that exact value, so show it, not a floor.
    var m = Math.floor(t / 60), s = t - m * 60;
    var ss = s.toFixed(2);
    if (s < 10) ss = "0" + ss;
    return m + ":" + ss;
  }
  function speakerLabel(id) { return spById[id] ? spById[id].label : id; }
  function videoTitle(id) { return vById[id] ? vById[id].title : id; }

  function esc(s) {
    return String(s).replace(/[&<>]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c];
    });
  }

  // The "match context": the set of utterances the current search/lemma
  // produced. The player page lists exactly these (across ALL videos), with
  // the active one highlighted. Null means a bare deep-link with no context.
  var matchContext = null; // { ids: [...], label: "..." }

  // Extra playback time, in seconds, kept after a segment's nominal end before
  // auto-advancing. SRT/diarized end times can clip a hair early; this pads the
  // tail. Dial it in (e.g. 0.05, 0.15) to taste.
  var END_BUFFER = 0.2;

  // Playback queue = the segments currently listed under the player, in order.
  // We stop at each segment's end and auto-advance to the next (wrapping to
  // the first after the last). Segments may span videos, so advancing can
  // switch the player source.
  var queue = [];          // utterance objects, in displayed order
  var queueRows = [];       // parallel array of row elements
  var activeIdx = -1;       // index into queue of the playing segment
  var currentEnd = Infinity; // stop playback when currentTime reaches this
  var currentSource = null;  // source_id of the loaded video

  // ---------- View switching ----------
  function showView(name) {
    // Leaving the Videos tab: pause any inline thumbnails still playing.
    if (name !== "videos") {
      document.querySelectorAll("#view-videos video").forEach(function (el) {
        try { el.pause(); } catch (e) {}
      });
    }
    ["search", "freq", "videos", "player"].forEach(function (v) {
      document.getElementById("view-" + v).hidden = (v !== name);
    });
    document.querySelectorAll(".nav-btn").forEach(function (b) {
      b.classList.toggle("active", b.dataset.view === name);
    });
  }
  document.querySelectorAll(".nav-btn").forEach(function (b) {
    b.addEventListener("click", function () {
      teardownPlayer();
      location.hash = "";
      showView(b.dataset.view);
      if (b.dataset.view === "freq") renderFreq();
      if (b.dataset.view === "videos") renderVideoList();
    });
  });

  // ---------- Videos view ----------
  // Each video's full set of utterances, in line order, becomes the queue so
  // you can watch the whole clip and click/auto-advance through every segment.
  function videoUtterances(sourceId) {
    return C.utterances
      .filter(function (u) { return u.source_id === sourceId; })
      .sort(function (a, b) { return a.line - b.line; });
  }
  function openFullVideo(sourceId) {
    var us = videoUtterances(sourceId);
    if (!us.length) return;
    var ids = us.map(function (u) { return u.utterance_id; });
    var v = vById[sourceId];
    openPlayer(sourceId, us[0].line, us[0].start, { ids: ids, label: v ? v.title : sourceId, kind: "video" });
  }
  function renderVideoList() {
    var host = document.getElementById("video-list");
    host.innerHTML = "";
    C.videos.forEach(function (v) {
      var us = videoUtterances(v.source_id);
      var card = document.createElement("div");
      card.className = "video-card";

      var thumb = document.createElement("video");
      thumb.className = "video-thumb";
      thumb.src = v.file;
      thumb.controls = true;
      thumb.preload = "metadata";

      var info = document.createElement("div");
      info.className = "video-info";
      info.innerHTML =
        "<div class='video-title'>" + esc(v.title) + "</div>" +
        "<div class='video-meta muted'>" + us.length + " segments" +
        (v.scene_meta && v.scene_meta.topic ? " &middot; " + esc(v.scene_meta.topic) : "") + "</div>";
      var btn = document.createElement("button");
      btn.className = "open-player-btn";
      btn.textContent = "Open full player";
      btn.addEventListener("click", function () { openFullVideo(v.source_id); });
      info.appendChild(btn);

      card.appendChild(thumb);
      card.appendChild(info);
      host.appendChild(card);
    });
  }

  // ---------- Filters ----------
  var META_FIELDS = ["gender", "age_group", "region"];
  function populateFilters() {
    var vSel = document.getElementById("filter-video");
    C.videos.forEach(function (v) {
      var o = document.createElement("option");
      o.value = v.source_id; o.textContent = v.title; vSel.appendChild(o);
    });
    META_FIELDS.forEach(function (f) {
      var vals = {};
      C.speakers.forEach(function (s) { if (s[f] != null) vals[s[f]] = true; });
      var keys = Object.keys(vals);
      var sel = document.getElementById("filter-" + f);
      if (!keys.length) return; // skip all-null fields
      sel.hidden = false;
      var def = document.createElement("option");
      def.value = ""; def.textContent = "All " + f.replace("_", " ");
      sel.appendChild(def);
      keys.forEach(function (k) {
        var o = document.createElement("option"); o.value = k; o.textContent = k; sel.appendChild(o);
      });
    });
  }

  function passesFilters(u) {
    var vf = document.getElementById("filter-video").value;
    if (vf && u.source_id !== vf) return false;
    var sp = spById[u.speaker_id];
    for (var i = 0; i < META_FIELDS.length; i++) {
      var f = META_FIELDS[i];
      var sel = document.getElementById("filter-" + f);
      if (sel.value && (!sp || sp[f] !== sel.value)) return false;
    }
    return true;
  }

  // ---------- Search + KWIC ----------
  function findMatchIndex(u, q, mode) {
    var arr = mode === "exact" ? u.tokens : u.lemmas;
    for (var i = 0; i < arr.length; i++) if (arr[i] === q) return i;
    return 0;
  }

  function runSearch() {
    var q = document.getElementById("query").value.trim().toLowerCase();
    var mode = document.getElementById("mode").value;
    var tbody = document.querySelector("#results tbody");
    tbody.innerHTML = "";
    var countEl = document.getElementById("result-count");
    if (!q) { countEl.textContent = ""; return; }

    var index = mode === "exact" ? C.form_index : C.lemma_index;
    var ids = index[q] || [];
    var hitIds = [];
    ids.forEach(function (id) {
      var u = uById[id];
      if (!u || !passesFilters(u)) return;
      hitIds.push(id);
      var mi = findMatchIndex(u, q, mode);
      var pre = u.tokens.slice(0, mi).join(" ");
      var match = u.tokens[mi];
      var post = u.tokens.slice(mi + 1).join(" ");
      var tr = document.createElement("tr");
      tr.innerHTML =
        "<td>" + esc(videoTitle(u.source_id)) + "</td>" +
        "<td>" + u.line + "</td>" +
        "<td>" + esc(speakerLabel(u.speaker_id)) + "</td>" +
        "<td>" + fmt(u.start) + "</td>" +
        "<td class='pre'>" + esc(pre) + "</td>" +
        "<td class='match'>" + esc(match) + "</td>" +
        "<td class='post'>" + esc(post) + "</td>";
      tr.addEventListener("click", function () {
        openPlayer(u.source_id, u.line, u.start, { ids: hitIds, label: q });
      });
      tbody.appendChild(tr);
    });
    countEl.textContent = hitIds.length + " result" + (hitIds.length === 1 ? "" : "s");
  }

  document.getElementById("search-form").addEventListener("submit", function (e) {
    e.preventDefault(); runSearch();
  });

  // ---------- Frequency view ----------
  function renderFreq() {
    var list = document.getElementById("lemma-list");
    list.innerHTML = "";
    var lemmas = Object.keys(C.lemma_freq).sort(function (a, b) {
      return C.lemma_freq[b] - C.lemma_freq[a];
    });
    lemmas.forEach(function (lem) {
      var row = document.createElement("div");
      row.className = "lemma-row";
      row.innerHTML = "<span>" + esc(lem) + "</span><span class='count'>" + C.lemma_freq[lem] + "</span>";
      row.addEventListener("click", function () {
        document.querySelectorAll(".lemma-row").forEach(function (r) { r.classList.remove("active"); });
        row.classList.add("active");
        renderLemmaDetail(lem);
      });
      list.appendChild(row);
    });
  }

  function renderLemmaDetail(lem) {
    var host = document.getElementById("lemma-detail");
    var ids = (C.lemma_index[lem] || []).slice();
    var us = ids.map(function (id) { return uById[id]; }).filter(Boolean);
    us.sort(function (a, b) { return a.difficulty - b.difficulty; });
    var sortedIds = us.map(function (u) { return u.utterance_id; });
    host.innerHTML = "<h3>" + esc(lem) + " &middot; easiest first</h3>";
    var tbl = document.createElement("table");
    tbl.innerHTML = "<thead><tr><th>Video</th><th>Line</th><th>Start</th><th>Difficulty</th><th>Text</th></tr></thead><tbody></tbody>";
    var tb = tbl.querySelector("tbody");
    us.forEach(function (u) {
      var tr = document.createElement("tr");
      tr.style.cursor = "pointer";
      tr.innerHTML = "<td>" + esc(videoTitle(u.source_id)) + "</td><td>" + u.line + "</td><td>" +
        fmt(u.start) + "</td><td>" + u.difficulty.toFixed(2) + "</td><td>" + esc(u.text) + "</td>";
      tr.addEventListener("click", function () {
        openPlayer(u.source_id, u.line, u.start, { ids: sortedIds, label: lem });
      });
      tb.appendChild(tr);
    });
    host.appendChild(tbl);
  }

  // ---------- Player ----------
  function teardownPlayer() {
    // Pause the outgoing video before detaching it: a removed-but-unpaused
    // <video> keeps playing and firing timeupdate events.
    if (window._corpusVideo) { try { window._corpusVideo.pause(); } catch (e) {} }
    document.getElementById("player-host").innerHTML = "";
    window._corpusVideo = null;
  }

  function openPlayer(sourceId, line, t, context) {
    var v = vById[sourceId];
    if (!v) return;
    if (context) matchContext = context;
    showView("player");
    document.getElementById("player-title").textContent = v.title;
    setHash(sourceId, line, t);
    teardownPlayer();
    currentSource = sourceId;
    renderMatches(sourceId, line);
    setupLocal(v, t);
  }

  function setupLocal(v, t) {
    var host = document.getElementById("player-host");
    var video = document.createElement("video");
    video.controls = true;
    video.src = v.file;
    video.addEventListener("loadedmetadata", function () {
      video.currentTime = t;
      var p = video.play(); if (p && p.catch) p.catch(function () {});
    });
    // Stop at the active segment's end and auto-advance through the queue.
    // Guard: only the CURRENT element drives advancement. A previous video
    // that was torn down can still be playing detached and firing timeupdate;
    // without this guard it would race ahead and skip/mis-highlight segments.
    video.addEventListener("timeupdate", function () {
      if (video !== window._corpusVideo) return;
      // Whole-video mode: play straight through, just follow the highlight as
      // we cross segment boundaries. No seeking, so no glitches.
      if (matchContext && matchContext.kind === "video") {
        followActiveByTime(video.currentTime);
        return;
      }
      // Concordance/queue mode: stop at the segment end (+ tail) and advance.
      if (video.currentTime >= currentEnd + END_BUFFER) advanceToNext();
    });
    host.appendChild(video);
    window._corpusVideo = video;
  }

  function seekPlayer(t) {
    if (window._corpusVideo) {
      window._corpusVideo.currentTime = t;
      var p = window._corpusVideo.play(); if (p && p.catch) p.catch(function () {});
    }
  }

  function setActiveRow(idx) {
    queueRows.forEach(function (r) { r.classList.remove("active"); });
    if (queueRows[idx]) {
      queueRows[idx].classList.add("active");
      queueRows[idx].scrollIntoView({ block: "nearest" });
    }
  }

  // Play queue[idx]: if it lives in another video, switch the player to it;
  // otherwise just seek and re-highlight in place.
  function playSegment(idx) {
    var u = queue[idx];
    if (!u) return;
    if (u.source_id !== currentSource) {
      openPlayer(u.source_id, u.line, u.start); // rebuilds queue + plays
      return;
    }
    activeIdx = idx;
    currentEnd = (typeof u.end === "number") ? u.end : Infinity;
    setActiveRow(idx);
    seekPlayer(u.start);
    setHash(u.source_id, u.line, u.start);
  }

  function advanceToNext() {
    if (!queue.length) return;
    currentEnd = Infinity; // avoid re-firing while we move to the next segment
    playSegment((activeIdx + 1) % queue.length);
  }

  // Whole-video mode: don't seek, just move the highlight to whichever segment
  // the playhead is currently inside. Between segments (gaps) the previous
  // highlight stays, so playback reads as smooth.
  function followActiveByTime(t) {
    var idx = -1;
    for (var i = 0; i < queue.length; i++) {
      if (t >= queue[i].start && t < queue[i].end) { idx = i; break; }
    }
    if (idx >= 0 && idx !== activeIdx) {
      activeIdx = idx;
      setActiveRow(idx);
      setHash(queue[idx].source_id, queue[idx].line, queue[idx].start);
    }
  }

  // The list below the player = only the matching segments (the current
  // search/lemma hits), across ALL videos, with the active one highlighted.
  // A bare deep-link with no context falls back to just the clicked segment.
  function renderMatches(activeSourceId, activeLine) {
    var host = document.getElementById("transcript");
    host.innerHTML = "";
    var ids = matchContext ? matchContext.ids : null;
    var us;
    if (ids && ids.length) {
      us = ids.map(function (id) { return uById[id]; }).filter(Boolean);
    } else {
      us = C.utterances.filter(function (u) {
        return u.source_id === activeSourceId && u.line === activeLine;
      });
    }
    queue = us;
    queueRows = [];
    activeIdx = -1;
    currentEnd = Infinity;

    var heading = document.createElement("div");
    heading.className = "matches-heading";
    heading.textContent = !matchContext ? "Segment"
      : (matchContext.kind === "video"
          ? "All segments (" + us.length + ")"
          : "Matching segments for “" + matchContext.label + "” (" + us.length + ")");
    host.appendChild(heading);

    us.forEach(function (u, i) {
      var row = document.createElement("div");
      row.className = "tr-line";
      row.innerHTML =
        "<span class='c-vid'>" + esc(videoTitle(u.source_id)) + "</span>" +
        "<span>" + u.line + "</span>" +
        "<span>" + esc(speakerLabel(u.speaker_id)) + "</span>" +
        "<span>" + fmt(u.start) + "</span>" +
        "<span>" + esc(u.text) + "</span>";
      row.addEventListener("click", function () { playSegment(i); });
      host.appendChild(row);
      queueRows.push(row);
      if (u.source_id === activeSourceId && u.line === activeLine) {
        activeIdx = i;
        currentEnd = (typeof u.end === "number") ? u.end : Infinity;
      }
    });
    if (activeIdx >= 0) setActiveRow(activeIdx);
  }

  document.getElementById("back-btn").addEventListener("click", function () {
    teardownPlayer(); location.hash = ""; showView("search");
  });

  // Title acts as a Home link from any view.
  document.getElementById("home-link").addEventListener("click", function (e) {
    e.preventDefault();
    teardownPlayer();
    lastSetHash = null;
    location.hash = "";
    showView("search");
  });

  // ---------- Hash routing: #/v/<id>?line=7&t=18.0 ----------
  // We write the hash ourselves on every seek/advance. To avoid our own writes
  // re-entering the router (which would drop the search context and reset the
  // player), record exactly what we set and ignore that hashchange.
  var lastSetHash = null;
  function setHash(sourceId, line, t) {
    var h = "#/v/" + sourceId + "?line=" + line + "&t=" + t;
    lastSetHash = h;
    location.hash = h;
  }
  function parseHash() {
    var h = location.hash.replace(/^#/, "");
    var m = h.match(/^\/v\/([^?]+)\?(.*)$/);
    if (!m) return null;
    var params = {};
    m[2].split("&").forEach(function (kv) {
      var p = kv.split("="); params[p[0]] = decodeURIComponent(p[1] || "");
    });
    return { sourceId: m[1], line: parseInt(params.line, 10), t: parseFloat(params.t) };
  }
  window.addEventListener("hashchange", function () {
    if (location.hash === lastSetHash) return; // our own write, ignore
    routeFromHash();
  });
  function routeFromHash() {
    var r = parseHash();
    if (r && vById[r.sourceId]) openPlayer(r.sourceId, r.line, isNaN(r.t) ? 0 : r.t);
  }

  // ---------- Init ----------
  populateFilters();
  routeFromHash();
})();
