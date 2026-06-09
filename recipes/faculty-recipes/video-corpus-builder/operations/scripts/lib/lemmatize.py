"""Tokenization + lemmatization — the linguistic layer that makes search smart.

This is the genuinely new contribution over the CORAAL reference: CORAAL does
literal/regex string matching, so searching "go" misses "going" and "went".
Here we map every surface form to its lemma (headword) so a learner who
searches a dictionary form finds ALL of its real utterances.

PLUGGABLE BY DESIGN. A Lemmatizer is anything with:

    tokenize(text)  -> list[str]   # surface tokens, lowercased
    lemmatize(text) -> list[str]   # one lemma per token, same length & order

get_lemmatizer(lang) returns one. We ship a dependency-free English rule-based
lemmatizer so faculty can run the pipeline on a fresh machine with nothing but
Python. Other languages register their own implementation.

LEVANTINE ARABIC (and other rich-morphology languages): a naive English-style
stemmer WILL NOT WORK — Arabic has clitics, prefixes/suffixes, and root-and-
pattern morphology. Plug in a morphology-aware analyzer (CAMeL Tools /
MADAMIRA-style). The slot is the ArabicLemmatizer stub at the bottom: implement
its two methods against your analyzer and register it. Nothing else in the
pipeline or the website needs to change.
"""

from __future__ import annotations

import re

# Tokens: words (incl. internal apostrophes/hyphens like "don't", "twenty-one")
# and, for non-Latin scripts, any run of word characters. Punctuation dropped.
_TOKEN_RE = re.compile(r"[^\W\d_]+(?:['’\-][^\W\d_]+)*", re.UNICODE)


class Lemmatizer:
    """Interface. Subclass and override lemmatize() (and tokenize() if needed)."""

    lang = "und"  # ISO 639 code; "und" = undetermined

    def tokenize(self, text: str) -> list[str]:
        return [t.lower() for t in _TOKEN_RE.findall(text)]

    def lemmatize(self, text: str) -> list[str]:  # pragma: no cover - interface
        raise NotImplementedError


class IdentityLemmatizer(Lemmatizer):
    """Fallback for languages with no analyzer yet: lemma == surface form.

    Search still works (exact + form-grouping is a no-op); you simply don't get
    cross-form grouping until a real analyzer is plugged in. Honest default.
    """

    lang = "und"

    def lemmatize(self, text: str) -> list[str]:
        return self.tokenize(text)


# --- English: small, rule-based, zero-dependency --------------------------- #

# Irregulars worth getting right for a teaching corpus. Extend freely.
_EN_IRREGULAR = {
    # verbs
    "is": "be", "are": "be", "am": "be", "was": "be", "were": "be",
    "being": "be", "been": "be", "'s": "be", "'re": "be", "'m": "be",
    "has": "have", "have": "have", "had": "have", "having": "have", "'ve": "have",
    "does": "do", "did": "do", "done": "do", "doing": "do",
    "goes": "go", "went": "go", "gone": "go", "going": "go",
    "said": "say", "says": "say", "saying": "say",
    "made": "make", "makes": "make", "making": "make",
    "came": "come", "comes": "come", "coming": "come",
    "got": "get", "gotten": "get", "gets": "get", "getting": "get",
    "took": "take", "taken": "take", "takes": "take", "taking": "take",
    "saw": "see", "seen": "see", "sees": "see", "seeing": "see",
    "knew": "know", "known": "know", "knows": "know", "knowing": "know",
    "thought": "think", "thinks": "think", "thinking": "think",
    "told": "tell", "tells": "tell", "telling": "tell",
    "found": "find", "finds": "find", "finding": "find",
    "gave": "give", "given": "give", "gives": "give", "giving": "give",
    "ran": "run", "runs": "run", "running": "run",
    "began": "begin", "begun": "begin", "begins": "begin", "beginning": "begin",
    "let": "let", "lets": "let", "letting": "let",
    "n't": "not", "won't": "will", "can't": "can", "cannot": "can",
    # nouns
    "children": "child", "people": "person", "men": "man", "women": "woman",
    "feet": "foot", "teeth": "tooth", "geese": "goose", "mice": "mouse",
    "dreams": "dream",  # regular, but pinned so the demo is exact
}

# Words we never reduce (closed-class function words + contraction fragments).
_EN_KEEP = {
    "this", "his", "its", "was", "has", "does", "yes", "is", "as", "us",
    "less", "ness", "boss", "class", "glass", "kiss", "miss", "pass",
}


class EnglishLemmatizer(Lemmatizer):
    """Rule-based English lemmatizer. Not perfect; good enough for teaching.

    Order: irregular table -> -ing/-ed/-s suffix rules with light spelling
    fixes (doubled consonants, e-restoration, -ies/-ves plurals).
    """

    lang = "en"

    def lemmatize(self, text: str) -> list[str]:
        return [self._lemma(tok) for tok in self.tokenize(text)]

    def _lemma(self, w: str) -> str:
        if w in _EN_IRREGULAR:
            return _EN_IRREGULAR[w]
        if w in _EN_KEEP or len(w) <= 3:
            return w

        # Verb -ing
        if w.endswith("ing") and len(w) > 5:
            return self._restore(w[:-3])
        # Verb/adj -ed
        if w.endswith("ed") and len(w) > 4:
            return self._restore(w[:-2])
        # Plural / 3sg -es / -s
        if w.endswith("ies") and len(w) > 4:
            return w[:-3] + "y"
        if w.endswith("ves") and len(w) > 4:
            return w[:-3] + "f"  # leaves->leaf, wolves->wolf (knives->knife handled by table if needed)
        if w.endswith(("ses", "xes", "zes", "ches", "shes")):
            return w[:-2]
        if w.endswith("s") and not w.endswith("ss"):
            return w[:-1]
        return w

    @staticmethod
    def _restore(stem: str) -> str:
        """Undo spelling changes a suffix caused: doubled consonant, dropped e."""
        # doubled final consonant: "running"->"runn"->"run", "stopped"->"stopp"->"stop"
        if len(stem) >= 3 and stem[-1] == stem[-2] and stem[-1] not in "lsz":
            return stem[:-1]
        # dropped silent e: "making"->"mak"->"make", "hoped"->"hop"->"hope"
        if len(stem) >= 2 and stem[-1] not in "aeiouy" and stem[-2] not in "aeiou":
            # Heuristic: short CVC stems that look like they lost an 'e'.
            if len(stem) <= 4 and stem[-2] in "aeiou":
                return stem + "e"
        # consonant+'a/i/o/u'+consonant ending often wants its 'e' back (make, hope)
        if re.search(r"[bcdfgptkv]$", stem) and re.search(r"[aeiou][bcdgklmnprstv]$", stem):
            return stem + "e"
        return stem


# --- Levantine Arabic: documented plug-in slot ----------------------------- #

class ArabicLemmatizer(Lemmatizer):
    """STUB — plug a morphology-aware analyzer in here, then register below.

    Recommended: CAMeL Tools (https://github.com/CAMeL-Lab/camel_tools), which
    offers dialectal (incl. Levantine) morphological analysis and disambiguation.

    Implementation sketch:
        from camel_tools.disambig.mle import MLEDisambiguator
        self._mle = MLEDisambiguator.pretrained()         # in __init__
        # tokenize(): use camel_tools.tokenizers.word.simple_word_tokenize
        # lemmatize(): disambiguate(tokens) -> take analysis['lex'] per token,
        #              dediacritize for a clean headword key.

    Until implemented, this raises so a misconfigured run fails loudly instead
    of silently lemmatizing Arabic with English rules.
    """

    lang = "ar"

    def lemmatize(self, text: str) -> list[str]:  # pragma: no cover - stub
        raise NotImplementedError(
            "Arabic lemmatization is not wired up. Install a morphology-aware "
            "analyzer (e.g. CAMeL Tools) and implement ArabicLemmatizer, then "
            "register it in _REGISTRY. Do NOT fall back to the English rules."
        )


_REGISTRY: dict[str, type[Lemmatizer]] = {
    "en": EnglishLemmatizer,
    "ar": ArabicLemmatizer,
    "und": IdentityLemmatizer,
}


def get_lemmatizer(lang: str) -> Lemmatizer:
    """Return a lemmatizer for an ISO 639 code; IdentityLemmatizer if unknown."""
    cls = _REGISTRY.get((lang or "und").lower(), IdentityLemmatizer)
    return cls()


def available_languages() -> list[str]:
    return sorted(_REGISTRY.keys())
