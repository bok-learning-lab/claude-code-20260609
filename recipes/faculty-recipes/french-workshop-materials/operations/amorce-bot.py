"""
amorce-bot.py — Générateur d'amorces pour FR30

Requires: pip install anthropic
Usage:    python3 amorce-bot.py
          python3 amorce-bot.py --grammar subjonctif
          python3 amorce-bot.py --seed "les médias sociaux"

The bot reads all .md files from inputs/, picks a random passage,
and returns one Diouf-inspired insight + one amorce targeting a
specific French grammatical function for students to complete in writing.
"""

import anthropic
import argparse
import os
import random
import sys
import textwrap

# ── paths ──────────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUTS_DIR = os.path.join(SCRIPT_DIR, "..", "inputs")

# ── grammar targets ────────────────────────────────────────────────────────
GRAMMAR_FUNCTIONS = {
    "subjonctif": {
        "label": "Subjonctif présent",
        "cues": [
            "Il est essentiel que...",
            "Je doute que...",
            "Bien que..., je pense que...",
            "Il faut que nous...",
            "C'est dommage que...",
        ],
    },
    "passe": {
        "label": "Imparfait / passé composé",
        "cues": [
            "Avant les réseaux sociaux, on...",
            "Quand j'étais plus jeune, je...",
            "La première fois que j'ai vu..., j'ai...",
            "À cette époque-là, les gens...",
            "Il a d'abord..., puis il...",
        ],
    },
    "discours_indirect": {
        "label": "Discours indirect",
        "cues": [
            "Diouf affirme que...",
            "L'auteur nous rappelle que...",
            "Selon Diouf,...",
            "Il explique que..., ce qui signifie que...",
            "Dans le texte, on lit que...",
        ],
    },
    "plus_que_parfait": {
        "label": "Plus-que-parfait",
        "cues": [
            "Avant que les smartphones n'arrivent, l'humanité avait...",
            "Il a réalisé que la société avait déjà...",
            "Quand il a écrit ce livre, il avait déjà...",
            "On n'avait jamais imaginé que...",
            "Les gens avaient oublié que...",
        ],
    },
}


def load_inputs(inputs_dir: str) -> list[dict]:
    """Return list of {filename, excerpt} dicts from all .md files."""
    docs = []
    for fname in sorted(os.listdir(inputs_dir)):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(inputs_dir, fname)
        with open(path, encoding="utf-8") as f:
            content = f.read()
        # Strip html comments and blank leading lines
        lines = [l for l in content.splitlines() if l.strip() and not l.startswith("<!--")]
        if lines:
            docs.append({"filename": fname, "lines": lines})
    return docs


def pick_passage(docs: list[dict], seed_phrase: str | None = None) -> str:
    """Pick a ~10-line passage, optionally biased toward seed_phrase."""
    if seed_phrase:
        # prefer docs whose content contains the seed
        matches = [d for d in docs if seed_phrase.lower() in " ".join(d["lines"]).lower()]
        pool = matches if matches else docs
    else:
        pool = docs

    doc = random.choice(pool)
    lines = doc["lines"]
    # pick a random window of up to 10 lines
    start = random.randint(0, max(0, len(lines) - 10))
    excerpt = "\n".join(lines[start : start + 10])
    return f"[source: {doc['filename']}]\n{excerpt}"


def pick_grammar(key: str | None = None) -> tuple[str, str]:
    """Return (grammar_key, grammar_label, random_cue)."""
    if key and key in GRAMMAR_FUNCTIONS:
        chosen_key = key
    else:
        chosen_key = random.choice(list(GRAMMAR_FUNCTIONS.keys()))
    entry = GRAMMAR_FUNCTIONS[chosen_key]
    cue = random.choice(entry["cues"])
    return chosen_key, entry["label"], cue


def generate(passage: str, grammar_label: str, cue: str) -> str:
    client = anthropic.Anthropic()

    system = textwrap.dedent("""
        Tu es un assistant pédagogique pour un cours de français de niveau avancé (FR30).
        Ton rôle est de créer des invitations à l'écriture ("amorces") qui aident les étudiants
        à pratiquer des fonctions grammaticales précises tout en réfléchissant aux idées de Boucar Diouf.

        Règles strictes :
        - Réponds UNIQUEMENT en français.
        - Ta réponse comporte exactement deux parties, séparées par une ligne vide :
          1. INSIGHT (1-2 phrases) : une idée frappante tirée du passage fourni, reformulée avec vivacité.
          2. AMORCE : la phrase-fragment fournie, telle quelle, suivie de "..." — rien d'autre.
        - L'amorce doit être naturellement complétable en utilisant la structure grammaticale cible.
        - Ne donne aucune explication, aucun métalangage grammatical, aucune instruction supplémentaire.
    """).strip()

    user = textwrap.dedent(f"""
        Passage source :
        {passage}

        Structure grammaticale cible : {grammar_label}
        Amorce à utiliser : {cue}

        Génère l'INSIGHT et l'AMORCE maintenant.
    """).strip()

    message = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=300,
        messages=[{"role": "user", "content": user}],
        system=system,
    )
    return message.content[0].text.strip()


def main():
    parser = argparse.ArgumentParser(description="Générateur d'amorces FR30")
    parser.add_argument(
        "--grammar",
        choices=list(GRAMMAR_FUNCTIONS.keys()),
        default=None,
        help="Structure grammaticale cible (défaut : aléatoire). Choix : "
        + ", ".join(GRAMMAR_FUNCTIONS.keys()),
    )
    parser.add_argument(
        "--seed",
        default=None,
        metavar="MOT",
        help="Mot-clé pour orienter le choix du passage source (ex: 'médias sociaux')",
    )
    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Erreur : la variable d'environnement ANTHROPIC_API_KEY n'est pas définie.")
        sys.exit(1)

    docs = load_inputs(INPUTS_DIR)
    if not docs:
        print(f"Erreur : aucun fichier .md trouvé dans {INPUTS_DIR}")
        sys.exit(1)

    passage = pick_passage(docs, args.seed)
    grammar_key, grammar_label, cue = pick_grammar(args.grammar)

    print(f"\n── Structure cible : {grammar_label} ──\n")
    result = generate(passage, grammar_label, cue)
    print(result)
    print()


if __name__ == "__main__":
    main()
