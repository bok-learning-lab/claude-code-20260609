#!/usr/bin/env python3
"""
build_explorer.py — generate the interactive grade-trajectory explorer.

Reads the synthetic gradebooks and the assessment schedule from ../inputs/,
bakes them into a single self-contained HTML file at ../outputs/grade_explorer.html
(inline JSON data + inline SVG chart + vanilla JS — no server, no CDN, works
offline). Re-run this after editing the CSVs in ../inputs/ to refresh the page.

The page lets a student type the grades they have so far and see their running
weighted grade traced over a cloud of past students, with a "similar students"
match and a humble, widening projection of where they might finish.
"""

import csv
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
INPUTS = os.path.normpath(os.path.join(HERE, "..", "inputs"))
OUTPUTS = os.path.normpath(os.path.join(HERE, "..", "outputs"))

# Grade weights by column key. The chart's x-axis (and the grade-entry order) is
# derived from the assessment dates in assessment_schedule.csv (see read_schedule),
# not hardcoded — so problem sets and exams interleave in true chronological order.
WEIGHTS = {
    "Mini-Exam": 0.05,
    **{f"PS{i}": 0.30 / 10 for i in range(1, 11)},
    "Midterm1": 0.15,
    "Midterm2": 0.15,
    "Participation": 0.05,
    "Final": 0.30,
}
LETTER_BANDS = [  # (low, high, letter) — high exclusive except the top
    (93, 101, "A"), (90, 93, "A-"), (87, 90, "B+"), (83, 87, "B"),
    (80, 83, "B-"), (77, 80, "C+"), (73, 77, "C"), (70, 73, "C-"),
    (67, 70, "D+"), (63, 67, "D"), (60, 63, "D-"), (0, 60, "F"),
]


def read_schedule():
    path = os.path.join(INPUTS, "assessment_schedule.csv")
    rows = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            rows.append({
                "key": r["column_key"],
                "label": r["assessment"],
                "week": int(r["week"]),
                "date": r["date"],
                "weight": WEIGHTS[r["column_key"]],
            })
    # Chronological order by actual due/exam date (ISO dates sort lexically).
    rows.sort(key=lambda a: a["date"])
    return rows


def read_cohort(filename, cohort, order):
    path = os.path.join(INPUTS, filename)
    students = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            scores = [round(float(r[k]), 1) for k in order]
            students.append({
                "id": r["student_id"],
                "cohort": cohort,
                "scores": scores,
                "final_pct": round(float(r["Course_Pct"]), 1),
                "letter": r["Final_Grade"],
            })
    return students


def build_data():
    assessments = read_schedule()
    order = [a["key"] for a in assessments]
    students = (read_cohort("gradebook_AY25.csv", "AY25", order)
                + read_cohort("gradebook_AY26.csv", "AY26", order))
    return {
        "assessments": assessments,
        "weights": [a["weight"] for a in assessments],
        "order": order,
        "letterBands": [{"low": lo, "high": hi, "letter": l}
                        for lo, hi, l in LETTER_BANDS],
        "students": students,
    }


def main():
    os.makedirs(OUTPUTS, exist_ok=True)
    data = build_data()
    data_json = json.dumps(data, separators=(",", ":"))
    html = HTML_TEMPLATE.replace("/*__DATA__*/", data_json)
    out_path = os.path.join(OUTPUTS, "grade_explorer.html")
    with open(out_path, "w") as f:
        f.write(html)
    n = len(data["students"])
    print(f"Wrote {out_path}")
    print(f"  embedded {n} past students across {len(data['assessments'])} assessments")
    print("  open it by double-clicking the file (works offline, no server needed)")


# ---------------------------------------------------------------------------
# The self-contained page. /*__DATA__*/ is replaced with the inline JSON above.
# ---------------------------------------------------------------------------
HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MATH 21a — Grade Trajectory Explorer</title>
<style>
  :root{
    --ink:#16222b; --muted:#41505c; --line:#d3dce2; --panel:#ffffff;
    --accent:#2f6f8f; --accent-dk:#255a74; --match:#e07b00; --you:#1b5e20; --past:#c3ccd3;
    --shadow:0 1px 2px rgba(20,40,55,.05), 0 14px 32px -20px rgba(20,40,55,.4);
  }
  *{box-sizing:border-box}
  body{margin:0;font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
       color:var(--ink);background:linear-gradient(180deg,#f3f8fa,#eef3f6 260px,#eef3f6);
       -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
  header{padding:28px 28px 4px;max-width:1320px;margin:0 auto}
  .eyebrow{font-size:12px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--accent)}
  h1{margin:3px 0 7px;font-size:27px;font-weight:680;letter-spacing:-.01em;line-height:1.18}
  .sub{color:var(--muted);font-size:15px}
  .how{max-width:1320px;margin:16px auto 0;padding:12px 16px;background:#e3eef4;
       border:1px solid #c2d6e1;border-radius:12px;font-size:13.5px;color:#1f3543}
  .how b{color:var(--accent);font-size:15px}
  .wrap{display:grid;grid-template-columns:minmax(0,1fr) 368px;gap:24px;
        padding:18px 28px 44px;max-width:1320px;margin:0 auto}
  @media (max-width:900px){.wrap{grid-template-columns:1fr}}
  .card{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:18px;
        box-shadow:var(--shadow)}
  .card h2{margin:0 0 12px;font-size:13px;letter-spacing:.04em;text-transform:uppercase;
           color:var(--muted);font-weight:700}
  svg{width:100%;height:auto;display:block}
  .legend{display:flex;flex-wrap:wrap;gap:16px;margin-top:12px;font-size:13px;color:var(--muted)}
  .swatch{display:inline-block;width:22px;height:0;border-top-width:3px;border-top-style:solid;
          border-radius:2px;vertical-align:middle;margin-right:6px}
  .hint{font-size:12.5px;color:var(--muted);margin:0 0 11px}
  .hint b{color:var(--accent);font-weight:700}
  .grid{display:grid;grid-template-columns:1fr 1fr;gap:11px 12px}
  .grid label{display:flex;flex-direction:column;font-size:12px;color:var(--muted);font-weight:500}
  .ifield{position:relative;display:flex;align-items:center;margin-top:3px}
  .ifield input{width:100%;font:inherit;padding:7px 40px 7px 10px;border:1px solid var(--line);
       border-radius:9px;background:#fff;transition:border-color .12s,box-shadow .12s}
  .ifield input::placeholder{color:#bcc8d0}
  .ifield input:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 3px rgba(47,111,143,.16)}
  .ifield .suf{position:absolute;right:10px;color:#7a8893;font-size:11px;font-weight:600;
       pointer-events:none;letter-spacing:.02em}
  .ifield input:not(:placeholder-shown)+.suf{color:var(--accent)}
  .full{grid-column:1 / -1}
  .cohorts{display:flex;flex-wrap:wrap;gap:14px;margin:0 0 14px;font-size:13px;color:var(--muted)}
  .cohorts label{display:flex;align-items:center;gap:5px;cursor:pointer}
  .under{display:grid;grid-template-columns:1.5fr 1fr;gap:16px;align-items:start;margin-top:16px}
  .under>*{margin-top:0}
  @media (max-width:680px){.under{grid-template-columns:1fr}}
  .prompt{margin-top:12px;padding:12px 14px;border-radius:12px;background:#f7fafb;
          border:1px dashed var(--line);color:var(--muted);font-size:13px}
  .outcome{margin-top:16px;padding:14px;border-radius:12px;background:#f7fafb;border:1px solid var(--line)}
  .outcome.empty{color:var(--muted)}
  .big{font-size:19px;font-weight:650;line-height:1.35}
  .tag{display:inline-block;padding:2px 9px;border-radius:999px;background:#eaf3f7;color:var(--accent);
       font-size:11.5px;font-weight:700;margin-left:6px;vertical-align:middle}
  .row{display:flex;justify-content:space-between;gap:8px;margin:5px 0;font-size:13.5px}
  .btnrow{display:flex;gap:10px;margin-top:12px}
  .btnrow button{flex:1;border:1px solid var(--line);background:#fff;border-radius:10px;padding:9px;
       cursor:pointer;font:inherit;font-weight:600;color:var(--ink);
       transition:background .12s,border-color .12s,transform .04s}
  .btnrow button:hover{background:#f1f5f7;border-color:#c4d2da}
  .btnrow button:active{transform:translateY(1px)}
  .btnrow #example{background:var(--accent);border-color:var(--accent);color:#fff}
  .btnrow #example:hover{background:var(--accent-dk);border-color:var(--accent-dk)}
  .note{font-size:12.5px;color:var(--muted);margin-top:10px}
  .foot{padding:0 28px 34px;color:var(--muted);font-size:12px;max-width:1320px;margin:0 auto}
  .tips{margin:8px 0 0;padding-left:18px}
  .tips li{margin:5px 0;color:var(--ink)}
  path[data-hist]{cursor:pointer}
  path[data-hist]:hover{stroke:#566370 !important;stroke-width:2.6 !important;opacity:1 !important}
  .whatif{margin-top:14px;padding:14px;border-radius:12px;background:#fffaf3;
          border:1px solid #f0dcc2;font-size:13px}
  .whatif select{font:inherit;padding:5px 8px;border:1px solid var(--line);border-radius:8px;background:#fff}
  .whatif .need{margin-top:8px;font-size:14px}
  .whatif .need b{font-size:18px}
  .whatif .ok b{color:var(--you)} .whatif .bad b{color:#b3261e}
</style>
</head>
<body>
<header>
  <div class="eyebrow">MATH 21a</div>
  <h1>Grade Trajectory Explorer</h1>
  <div class="sub">Each faint line is a past student, from the first mini-exam to their final grade.
  Type your own scores to see how your path compares, and where past students like you tended to finish.</div>
</header>

<div class="how">How to use: <b>①</b> type the scores you have so far in the panel on the right →
<b>②</b> the amber lines are past students who started like you → <b>③</b> the shaded amber cone
shows the range of where students like you finished. Hover any grey line to inspect a single student.</div>

<div class="wrap">
  <div class="card">
    <div id="chart"></div>
    <div class="legend" id="legend"></div>
    <div class="under" id="under">
      <div class="outcome" id="outcome"></div>
      <div class="whatif" id="whatif"></div>
    </div>
  </div>

  <div class="card">
    <h2>Plot your own grades</h2>
    <div class="cohorts" id="cohorts"></div>
    <div class="hint">Type each score <b>out of 100</b> — leave a box blank for anything you haven't gotten back yet.</div>
    <div class="grid" id="inputs"></div>
    <div class="btnrow">
      <button id="clear">Clear</button>
      <button id="example">Try an example</button>
    </div>
    <div class="prompt" id="prompt">Enter at least one score to see students who looked like you, and where students like you tend to finish — the results appear under the graph.</div>
    <div class="note" id="exampleNote"></div>
    <div class="note">Your grades stay in this browser. Nothing is uploaded or saved.</div>
  </div>
</div>

<div class="foot">Built from two past offerings of synthetic, fully anonymized data — the trajectories are
illustrative, not real individuals. Letter bands and weights follow the course syllabus.</div>

<script>
const DATA = /*__DATA__*/;
const A = DATA.assessments, W = DATA.weights, BANDS = DATA.letterBands;
const N = A.length;
const ALL = DATA.students;

// ---- grade math -----------------------------------------------------------
// Running weighted grade after each completed assessment, renormalizing the
// weights of what has happened so far. `scores` is an array (length N) where
// null/NaN means "not taken yet".
function runningGrade(scores){
  const out = []; let wsum = 0, vsum = 0;
  for(let i=0;i<N;i++){
    const s = scores[i];
    if(s===null||s===undefined||isNaN(s)){ out.push(null); continue; }
    wsum += W[i]; vsum += W[i]*s;
    out.push(wsum>0 ? vsum/wsum : null);
  }
  return out;
}
function letterOf(pct){
  for(const b of BANDS){ if(pct>=b.low && pct<b.high) return b.letter; }
  return pct>=93 ? "A" : "F";
}
// Precompute each historical student's running curve.
for(const st of ALL){ st.run = runningGrade(st.scores); }

// ---- one real "turnaround" student, used to seed the Try-an-example button -
function pickTurnaround(){
  let turn=null,tBest=-1e9;
  for(const st of ALL){
    const d = st.scores[N-1]-st.scores[0];          // Final minus Mini-Exam
    if(st.final_pct>=80 && d>tBest){tBest=d;turn=st;}     // recovered to a good place
  }
  return turn;
}
const TURNAROUND = pickTurnaround();

// ---- chart (hand-rolled SVG) ----------------------------------------------
const SVG="http://www.w3.org/2000/svg";
const VBW=960, VBH=540, M={t:24,r:54,b:64,l:46};
const PW=VBW-M.l-M.r, PH=VBH-M.t-M.b;
// visible grade range — derived from the data so it fits the current CSVs
let DMIN=100;
for(const st of ALL){ for(const v of st.run){ if(v!=null && v<DMIN) DMIN=v; } }
const Y0=Math.max(0,Math.floor((DMIN-4)/5)*5), Y1=100;
const x = i => M.l + (N===1?0:i*PW/(N-1));
const y = v => M.t + PH*(1-(v-Y0)/(Y1-Y0));
const BANDFILL={A:"#e3f0e6",["A-"]:"#e9f2ea",["B+"]:"#eef3ec",B:"#f1f4ec",["B-"]:"#f4f3ea",
  ["C+"]:"#f7f1e6",C:"#f8efe2",["C-"]:"#f8ecdd",["D+"]:"#f7e8d8",D:"#f6e4d3",["D-"]:"#f5e1cf",F:"#f3ddca"};

function el(tag,attrs,parent){const e=document.createElementNS(SVG,tag);
  for(const k in attrs)e.setAttribute(k,attrs[k]); if(parent)parent.appendChild(e); return e;}
function path(points){ // points: [{i,v}]
  return points.map((p,k)=>(k?"L":"M")+x(p.i).toFixed(1)+" "+y(p.v).toFixed(1)).join(" ");
}
function curvePoints(run){const pts=[];for(let i=0;i<N;i++)if(run[i]!=null)pts.push({i,v:run[i]});return pts;}

let svg, layers={};
function drawChart(){
  const host=document.getElementById("chart"); host.innerHTML="";
  svg=el("svg",{viewBox:`0 0 ${VBW} ${VBH}`,role:"img",
    "aria-label":"Grade trajectories from past students"},host);

  // letter-grade bands (major letters only, for a calm backdrop)
  const major=[["A",90,101],["B",80,90],["C",70,80],["D",60,70],["F",Y0,60]];
  for(const [L,lo,hi] of major){
    const yt=y(Math.min(hi,Y1)), yb=y(Math.max(lo,Y0));
    el("rect",{x:M.l,y:yt,width:PW,height:Math.max(0,yb-yt),fill:BANDFILL[L]||"#eee",opacity:.85},svg);
    el("line",{x1:M.l,x2:M.l+PW,y1:yb,y2:yb,stroke:"#fff",["stroke-width"]:1},svg);
    el("text",{x:M.l+PW+8,y:(yt+yb)/2+4,fill:"#6a7884","font-size":13,"font-weight":700},svg).textContent=L;
  }
  // gridlines + y labels
  for(let v=Math.ceil(Y0/10)*10;v<=100;v+=10){
    el("line",{x1:M.l,x2:M.l+PW,y1:y(v),y2:y(v),stroke:"#fff",["stroke-width"]:1},svg);
    el("text",{x:M.l-8,y:y(v)+4,"text-anchor":"end","font-size":11,fill:"#6a7884"},svg).textContent=v;
  }
  // x ticks (assessment labels, abbreviated)
  for(let i=0;i<N;i++){
    const lab=A[i].key.replace("Mini-Exam","Mini").replace("Midterm","M").replace("Participation","Part").replace("Final","Final");
    const tx=x(i);
    el("line",{x1:tx,x2:tx,y1:M.t,y2:M.t+PH,stroke:"#eef3f6",["stroke-width"]:1},svg);
    const t=el("text",{x:tx,y:M.t+PH+18,"text-anchor":"end","font-size":10,fill:"#5f6d78",
      transform:`rotate(-40 ${tx} ${M.t+PH+18})`},svg); t.textContent=lab;
  }
  layers.proj=el("g",{},svg);
  layers.hist=el("g",{opacity:.5},svg);
  layers.match=el("g",{},svg);
  layers.you=el("g",{},svg);

  redrawHistory();
}

let activeCohorts={AY25:true,AY26:true};

function redrawHistory(){
  layers.hist.innerHTML="";
  for(const st of ALL){
    if(!activeCohorts[st.cohort]) continue;
    const p=el("path",{d:path(curvePoints(st.run)),fill:"none",stroke:"var(--past)",
      ["stroke-width"]:1,opacity:.8,"data-hist":"1"},layers.hist);
    const t=document.createElementNS(SVG,"title");
    t.textContent=`Started ${st.run[0].toFixed(0)}% → finished ${st.final_pct.toFixed(0)}% (${st.letter})`;
    p.appendChild(t);
  }
}

// ---- student input + matching --------------------------------------------
let mine=new Array(N).fill(null);

function buildInputs(){
  const g=document.getElementById("inputs");
  A.forEach((a,i)=>{
    const lab=document.createElement("label");
    lab.textContent=a.label+" ("+Math.round(a.weight*100)+"%)";
    const field=document.createElement("div"); field.className="ifield";
    const inp=document.createElement("input");
    inp.type="number"; inp.min=0; inp.max=100; inp.step="0.1"; inp.placeholder="—";
    inp.setAttribute("aria-label",a.label+" score out of 100");
    inp.addEventListener("input",()=>{
      const v=inp.value===""?null:Math.max(0,Math.min(100,parseFloat(inp.value)));
      mine[i]=isNaN(v)?null:v; update();
    });
    const suf=document.createElement("span"); suf.className="suf"; suf.textContent="/100";
    field.appendChild(inp); field.appendChild(suf);
    lab.appendChild(field); g.appendChild(lab);
  });
}
const COHORT_LABEL={AY25:"AY2025",AY26:"AY2026"};
function buildCohorts(){
  const c=document.getElementById("cohorts");
  ["AY25","AY26"].forEach(co=>{
    const l=document.createElement("label");
    const cb=document.createElement("input"); cb.type="checkbox"; cb.checked=true;
    cb.addEventListener("change",()=>{activeCohorts[co]=cb.checked;redrawHistory();update();});
    l.appendChild(cb); l.appendChild(document.createTextNode(" Include "+(COHORT_LABEL[co]||co)));
    c.appendChild(l);
  });
}
function buildLegend(){
  const lg=document.getElementById("legend");
  lg.innerHTML='<span><i class="swatch" style="border-top-color:var(--past)"></i>Past students</span>'
    +'<span><i class="swatch" style="border-top-color:var(--you)"></i>You</span>'
    +'<span><i class="swatch" style="border-top-color:var(--match)"></i>Similar students &amp; projection</span>';
}

// ---- "what do I need on what's left?" (target-grade solver) ----------------
function neededFor(letter){
  const band=BANDS.find(b=>b.letter===letter); if(!band) return null;
  let earned=0, remW=0;                       // weights sum to 1, so earned is already in pct
  for(let i=0;i<N;i++){
    if(mine[i]!=null) earned+=W[i]*mine[i]; else remW+=W[i];
  }
  if(remW<=1e-9) return {done:true, final:earned};
  return {done:false, need:(band.low-earned)/remW, remW};
}
function buildWhatIf(){
  const host=document.getElementById("whatif");
  const opts=BANDS.filter(b=>b.letter!=="F")
    .map(b=>`<option value="${b.letter}">${b.letter}</option>`).join("");
  host.innerHTML=`<div>Goal check — to finish at `+
    `<select id="target">${opts}</select> you'd need:</div>`+
    `<div class="need" id="need">—</div>`;
  const sel=document.getElementById("target"); sel.value="B";
  sel.addEventListener("change",updateWhatIf);
}
function updateWhatIf(){
  const sel=document.getElementById("target"); if(!sel) return;
  const need=document.getElementById("need");
  const r=neededFor(sel.value);
  if(r.done){ need.className="need"; need.textContent=`All grades are in — you finished at ${r.final.toFixed(0)}%.`; return; }
  if(r.need<=0){ need.className="need ok";
    need.innerHTML=`<b>already secured</b> — even a 0 on everything left keeps you at ${sel.value} or above.`; }
  else if(r.need>100){ need.className="need bad";
    need.innerHTML=`<b>out of reach</b> — it would take more than 100% on the remaining work.`; }
  else { need.className="need ok";
    need.innerHTML=`an average of <b>${r.need.toFixed(0)}%</b> across the remaining ${Math.round(r.remW*100)}% of the grade.`; }
}

// ---- hopeful, assignment-type-specific tips for the work still ahead -------
function improvementTips(){
  let pset={w:0,n:0}, mid={w:0,n:0}, fin=0, part=0, mini=0;
  for(let i=0;i<N;i++){
    if(mine[i]!=null) continue;
    const k=A[i].key, w=W[i];
    if(k.startsWith("PS")){pset.w+=w;pset.n++;}
    else if(k.startsWith("Midterm")){mid.w+=w;mid.n++;}
    else if(k==="Final") fin+=w;
    else if(k==="Participation") part+=w;
    else if(k==="Mini-Exam") mini+=w;
  }
  const pct=w=>Math.round(w*100);
  const tips=[];
  if(pset.w>0) tips.push({w:pset.w,html:`<b>${pset.n} problem set${pset.n>1?"s":""} left (${pct(pset.w)}%)</b> — your steadiest points. They reward effort over test nerves, and the Math Question Center can help you lock them in.`});
  if(mid.w>0) tips.push({w:mid.w,html:`<b>${mid.n>1?"Midterms":"A midterm"} ahead (${pct(mid.w)}%)</b> — very recoverable. Students who reviewed in office hours after a shaky start often gained a full letter here.`});
  if(fin>0) tips.push({w:fin,html:`<b>The final exam (${pct(fin)}%)</b> — the biggest single lever left. A strong finish has pulled many students up a letter or more.`});
  if(part>0) tips.push({w:part,html:`<b>Participation (${pct(part)}%)</b> — easy to bank: keep showing up and engaging.`});
  if(mini>0) tips.push({w:mini,html:`<b>The mini-exam (${pct(mini)}%)</b> is still ahead — a low-stakes way to build early momentum.`});
  tips.sort((a,b)=>b.w-a.w);
  return tips.slice(0,3).map(t=>t.html);
}

function enteredIndices(){const ix=[];for(let i=0;i<N;i++)if(mine[i]!=null)ix.push(i);return ix;}

function findNeighbors(ix){
  const pool=ALL.filter(s=>activeCohorts[s.cohort]);
  const scored=pool.map(s=>{
    let d=0;for(const i of ix){const diff=s.scores[i]-mine[i];d+=diff*diff;}
    return {s,dist:Math.sqrt(d/ix.length)};
  }).sort((a,b)=>a.dist-b.dist);
  const k=Math.max(6,Math.min(15,Math.round(pool.length*0.25)));
  return scored.slice(0,k).map(o=>o.s);
}
function quantile(arr,q){const a=[...arr].sort((x,y)=>x-y);
  const p=(a.length-1)*q,b=Math.floor(p),r=p-b;
  return a[b+1]!==undefined?a[b]+r*(a[b+1]-a[b]):a[b];}

function update(){
  // your line
  layers.you.innerHTML="";
  const run=runningGrade(mine), pts=curvePoints(run);
  if(pts.length){
    el("path",{d:path(pts),fill:"none",stroke:"var(--you)",["stroke-width"]:4,
      ["stroke-linejoin"]:"round"},layers.you);
    for(const p of pts) el("circle",{cx:x(p.i),cy:y(p.v),r:3.5,fill:"var(--you)"},layers.you);
  }
  // matching + projection
  layers.match.innerHTML=""; layers.proj.innerHTML="";
  const ix=enteredIndices();
  updateWhatIf();
  const out=document.getElementById("outcome");
  const under=document.getElementById("under");
  const promptEl=document.getElementById("prompt");
  if(ix.length===0){
    under.style.display="none";
    promptEl.style.display="";
    return;
  }
  under.style.display="";
  promptEl.style.display="none";
  const nbrs=findNeighbors(ix);
  for(const s of nbrs)
    el("path",{d:path(curvePoints(s.run)),fill:"none",stroke:"var(--match)",
      ["stroke-width"]:1.6,opacity:.55},layers.match);

  const finals=nbrs.map(s=>s.final_pct);
  const wDone=ix.reduce((a,i)=>a+W[i],0);            // fraction of grade completed
  const med=quantile(finals,.5);
  // base band from neighbors, widened when little of the grade is in yet
  let lo=quantile(finals,.25), hi=quantile(finals,.75);
  const widen=(1-wDone)*5;                            // modest early-term cushion, kept tight for sub-letter precision
  lo=Math.max(Y0, lo-widen); hi=Math.min(100, hi+widen);

  // hopeful, assignment-type-specific tips for the grade still ahead
  const tips=improvementTips();
  const hopeful = tips.length
    ? `<div class="note"><b>Where you can still gain — ${Math.round((1-wDone)*100)}% of the grade is still ahead:</b>`+
      `<ul class="tips">`+tips.map(t=>`<li>${t}</li>`).join("")+`</ul></div>`
    : `<div class="note">Every assessment is in — this is your final standing.</div>`;

  // shaded projection from the student's current point to the end
  const lastIx=ix[ix.length-1];
  const curY=run[lastIx];
  const xL=x(lastIx), xR=x(N-1);
  el("path",{d:`M ${xL} ${y(curY)} L ${xR} ${y(hi)} L ${xR} ${y(lo)} Z`,
    fill:"var(--match)",opacity:.15},layers.proj);
  el("line",{x1:xL,y1:y(curY),x2:xR,y2:y(med),stroke:"var(--match)",
    ["stroke-width"]:1.5,["stroke-dasharray"]:"5 4",opacity:.8},layers.proj);

  const loL=letterOf(lo), hiL=letterOf(hi), medL=letterOf(med);
  const range = loL===hiL ? `around <b>${medL}</b>` : `between <b>${loL}</b> and <b>${hiL}</b>`;
  out.className="outcome";
  out.innerHTML =
    `<div class="big">Students who looked like you ${ix.length<3?"early on":"so far"} `+
    `finished ${range}<span class="tag">${Math.round(wDone*100)}% of grade entered</span></div>`+
    `<div class="row"><span>Most common outcome</span><b>${medL} (${med.toFixed(0)}%)</b></div>`+
    `<div class="row"><span>Range of similar students</span><span>${loL}–${hiL}</span></div>`+
    `<div class="row"><span>Matched past students</span><span>${nbrs.length}</span></div>`+
    `<div class="note">This is the spread of <i>past</i> outcomes for students with similar scores — `+
    `a range of possibilities, not a prediction or a ceiling. It narrows as more of your term is entered.</div>`+
    hopeful;
}

function fillExample(){
  // seed the inputs with a real turnaround student's early scores (through Midterm 1)
  const e=TURNAROUND||ALL[0];
  const stop=DATA.order.indexOf("Midterm1");
  const inputs=document.querySelectorAll("#inputs input");
  mine=new Array(N).fill(null);
  for(let i=0;i<=stop;i++){ mine[i]=e.scores[i]; inputs[i].value=e.scores[i]; }
  for(let i=stop+1;i<N;i++) inputs[i].value="";
  document.getElementById("exampleNote").textContent=
    `Example loaded: a real past student who scored ${e.scores[0].toFixed(0)}% on the mini-exam `+
    `but finished ${e.final_pct.toFixed(0)}% (${e.letter}). Clear it and enter your own scores.`;
  update();
}
function clearAll(){
  mine=new Array(N).fill(null);
  document.querySelectorAll("#inputs input").forEach(i=>i.value="");
  document.getElementById("exampleNote").textContent="";
  update();
}

drawChart(); buildInputs(); buildCohorts(); buildLegend(); buildWhatIf();
document.getElementById("clear").addEventListener("click",clearAll);
document.getElementById("example").addEventListener("click",fillExample);
update();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    main()
