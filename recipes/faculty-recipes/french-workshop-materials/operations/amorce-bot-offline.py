"""
amorce-bot-offline.py — Générateur d'amorces FR30 (version hors ligne)

Requires: Python 3.6+, no API key, no external libraries.
Usage:    python3 amorce-bot-offline.py
          python3 amorce-bot-offline.py --grammar subjonctif
          python3 amorce-bot-offline.py --all
"""

import argparse
import random
import textwrap

# ── amorces ────────────────────────────────────────────────────────────────
# Each entry: insight drawn from Diouf / FR30 materials + amorce fragment.
# Grammar key: subjonctif | passe | discours_indirect | plus_que_parfait

AMORCES = [
    # ── Subjonctif présent ─────────────────────────────────────────────────
    {
        "grammar": "subjonctif",
        "grammar_label": "Subjonctif présent",
        "insight": (
            "Diouf compare l'humanité connectée à un superorganisme d'insectes sociaux — "
            "chaque individu uni aux autres par un réseau invisible mais puissant."
        ),
        "amorce": "Il est essentiel que nous...",
    },
    {
        "grammar": "subjonctif",
        "grammar_label": "Subjonctif présent",
        "insight": (
            "Selon Diouf, les grandes entreprises technologiques savent depuis longtemps "
            "que notre cerveau cherche des récompenses sans effort — et elles en profitent."
        ),
        "amorce": "C'est dommage que les jeunes...",
    },
    {
        "grammar": "subjonctif",
        "grammar_label": "Subjonctif présent",
        "insight": (
            "Diouf rappelle que même une simple balade dans un parc peut apporter "
            "des bienfaits réels à notre santé mentale — la nature reste une pharmacopée accessible."
        ),
        "amorce": "Il faut que la société...",
    },
    {
        "grammar": "subjonctif",
        "grammar_label": "Subjonctif présent",
        "insight": (
            "Pour Diouf, les médias sociaux peuvent être des espaces de solidarité et "
            "d'apprentissage — mais leur côté obscur prend trop de place."
        ),
        "amorce": "Bien que les réseaux sociaux soient utiles,...",
    },
    {
        "grammar": "subjonctif",
        "grammar_label": "Subjonctif présent",
        "insight": (
            "Diouf cite sa mère : « Tends la main et ouvre ton cœur, car l'humain "
            "reste le meilleur remède pour son prochain. »"
        ),
        "amorce": "Je doute que l'intelligence artificielle puisse...",
    },
    {
        "grammar": "subjonctif",
        "grammar_label": "Subjonctif présent",
        "insight": (
            "L'auteur avertit que l'ère du « grand repos neuronal » approche à mesure "
            "que l'IA prend en charge chacune de nos activités."
        ),
        "amorce": "Il est urgent que les enseignants...",
    },

    # ── Imparfait / passé composé ──────────────────────────────────────────
    {
        "grammar": "passe",
        "grammar_label": "Imparfait / passé composé",
        "insight": (
            "Diouf rappelle qu'autrefois, « c'étaient les pieds qui traçaient le chemin "
            "de la parenté et de l'amitié » — on se déplaçait pour rejoindre ceux qu'on aimait."
        ),
        "amorce": "Avant les réseaux sociaux, les gens...",
    },
    {
        "grammar": "passe",
        "grammar_label": "Imparfait / passé composé",
        "insight": (
            "Au début de la télévision, il fallait se lever pour changer de chaîne. "
            "Puis la télécommande est arrivée — première étape vers l'économie d'effort total."
        ),
        "amorce": "Quand j'étais plus jeune, je passais mon temps à...",
    },
    {
        "grammar": "passe",
        "grammar_label": "Imparfait / passé composé",
        "insight": (
            "Diouf décrit comment la technologie a évolué du téléphone fixe au cellulaire : "
            "à chaque étape, on nous a épargné un effort de plus."
        ),
        "amorce": "La première fois que j'ai utilisé un réseau social, j'ai remarqué que...",
    },
    {
        "grammar": "passe",
        "grammar_label": "Imparfait / passé composé",
        "insight": (
            "La sœur de Diouf, 70 ans, était si absorbée par les vidéos en ligne "
            "lors d'un rassemblement familial au Sénégal qu'elle en oubliait les gens autour d'elle."
        ),
        "amorce": "Pendant le cours, l'étudiant(e) a d'abord..., puis il/elle...",
    },
    {
        "grammar": "passe",
        "grammar_label": "Imparfait / passé composé",
        "insight": (
            "Diouf souligne que l'humanité a passé plus de 99 % de son existence "
            "en interaction étroite avec la nature — un lien qu'on a presque perdu."
        ),
        "amorce": "À cette époque-là, la communauté...",
    },
    {
        "grammar": "passe",
        "grammar_label": "Imparfait / passé composé",
        "insight": (
            "Selon Diouf, nous marchons sur le chemin de l'économie d'effort depuis "
            "bien avant le boom du numérique — c'est un trait profondément humain."
        ),
        "amorce": "Quand Internet est arrivé dans les foyers, tout a changé parce que...",
    },

    # ── Discours indirect ──────────────────────────────────────────────────
    {
        "grammar": "discours_indirect",
        "grammar_label": "Discours indirect",
        "insight": (
            "Diouf s'appuie sur les sciences de la nature pour aborder les réseaux sociaux — "
            "une approche originale qui touche le cœur autant qu'elle stimule la réflexion."
        ),
        "amorce": "Dans son introduction, Diouf explique que...",
    },
    {
        "grammar": "discours_indirect",
        "grammar_label": "Discours indirect",
        "insight": (
            "Le neuroscientiﬁque Sébastien Bohler compare l'humanité à un superorganisme "
            "comme une colonie de fourmis — une image que Diouf reprend à son compte."
        ),
        "amorce": "Selon l'auteur, les médias sociaux...",
    },
    {
        "grammar": "discours_indirect",
        "grammar_label": "Discours indirect",
        "insight": (
            "Diouf cite la sagesse de sa mère sénégalaise pour nous rappeler que "
            "la présence humaine reste irremplaçable, même à l'ère de l'IA."
        ),
        "amorce": "La mère de Diouf lui a appris que...",
    },
    {
        "grammar": "discours_indirect",
        "grammar_label": "Discours indirect",
        "insight": (
            "Sartre écrivait : « L'enfer, c'est les autres. » Diouf le contredit : "
            "c'est justement grâce aux autres que se construit le bien-être durable."
        ),
        "amorce": "Diouf affirme que Sartre avait partiellement tort quand il disait que...",
    },
    {
        "grammar": "discours_indirect",
        "grammar_label": "Discours indirect",
        "insight": (
            "L'auteur avertit que les prédateurs numériques sont difficiles à éviter "
            "car, contrairement à la nature, les médias sociaux n'offrent aucune cachette."
        ),
        "amorce": "Dans le texte, on apprend que les jeunes victimes d'intimidation...",
    },
    {
        "grammar": "discours_indirect",
        "grammar_label": "Discours indirect",
        "insight": (
            "Diouf reconnaît ne pas être un expert, mais un observateur curieux et inquiet "
            "qui emprunte à la biologie pour mieux comprendre notre rapport aux écrans."
        ),
        "amorce": "L'auteur nous rappelle que la solution proposée consiste à...",
    },

    # ── Plus-que-parfait ───────────────────────────────────────────────────
    {
        "grammar": "plus_que_parfait",
        "grammar_label": "Plus-que-parfait",
        "insight": (
            "Avant l'arrivée du cellulaire, les gens avaient déjà commencé à perdre "
            "l'habitude de se déplacer pour voir leurs proches — le téléphone fixe avait "
            "ouvert la voie."
        ),
        "amorce": "Avant que les smartphones n'arrivent, l'humanité avait déjà...",
    },
    {
        "grammar": "plus_que_parfait",
        "grammar_label": "Plus-que-parfait",
        "insight": (
            "Diouf montre que le capitalisme numérique avait étudié le cerveau humain "
            "en profondeur avant de lui proposer ses plateformes addictives."
        ),
        "amorce": "Les entreprises technologiques avaient compris que...",
    },
    {
        "grammar": "plus_que_parfait",
        "grammar_label": "Plus-que-parfait",
        "insight": (
            "Selon Diouf, l'humanité n'avait jamais imaginé qu'un moustique en Afrique "
            "pourrait faire réagir instantanément un internaute à Montréal."
        ),
        "amorce": "On n'avait jamais imaginé qu'un jour...",
    },
    {
        "grammar": "plus_que_parfait",
        "grammar_label": "Plus-que-parfait",
        "insight": (
            "Quand Diouf a écrit ce livre, les recherches sur les effets des écrans "
            "chez les jeunes avaient déjà alerté de nombreux professionnels de santé."
        ),
        "amorce": "Quand ce livre a été publié, les scientifiques avaient déjà démontré que...",
    },
    {
        "grammar": "plus_que_parfait",
        "grammar_label": "Plus-que-parfait",
        "insight": (
            "Diouf souligne que certains pays avaient eu le courage de légiférer sur "
            "l'usage des écrans chez les jeunes — mais les entreprises n'avaient pas suivi."
        ),
        "amorce": "Les gouvernements avaient tenté de..., mais...",
    },
    {
        "grammar": "plus_que_parfait",
        "grammar_label": "Plus-que-parfait",
        "insight": (
            "L'auteur rappelle que les liens sociaux concrets avaient toujours soutenu "
            "la santé mentale — bien avant que la psychologie moderne ne le prouve."
        ),
        "amorce": "Avant même que les chercheurs ne le confirment, les anciens avaient su que...",
    },
]

# ── display ────────────────────────────────────────────────────────────────
WRAP = 72


def display(entry: dict) -> None:
    print(f"\n── Structure cible : {entry['grammar_label']} ──\n")
    print(textwrap.fill(entry["insight"], width=WRAP))
    print()
    print(entry["amorce"])
    print()


def main():
    parser = argparse.ArgumentParser(description="Générateur d'amorces FR30 (hors ligne)")
    parser.add_argument(
        "--grammar",
        choices=["subjonctif", "passe", "discours_indirect", "plus_que_parfait"],
        default=None,
        help="Structure grammaticale cible (défaut : aléatoire)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Afficher toutes les amorces groupées par structure",
    )
    args = parser.parse_args()

    if args.all:
        for key in ["subjonctif", "passe", "discours_indirect", "plus_que_parfait"]:
            pool = [a for a in AMORCES if a["grammar"] == key]
            for entry in pool:
                display(entry)
                print("─" * WRAP)
        return

    pool = (
        [a for a in AMORCES if a["grammar"] == args.grammar]
        if args.grammar
        else AMORCES
    )
    display(random.choice(pool))


if __name__ == "__main__":
    main()
