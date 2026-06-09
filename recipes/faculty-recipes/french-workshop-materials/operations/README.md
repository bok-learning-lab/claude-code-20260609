# Amorce Bot — FR30

Generates a random Boucar Diouf-inspired insight + a sentence-fragment prompt ("amorce") for students to complete in writing. Each run targets one of four grammatical functions from FR30.

## Setup (one time)

```bash
pip install anthropic
export ANTHROPIC_API_KEY=sk-ant-...
```

> The API key can also be added to a `.env` file or your shell profile (`~/.zshrc`) so you don't have to set it each session.

## Running the bot

From the `operations/` folder (or any directory):

```bash
# Fully random — picks a random passage and grammar target
python3 amorce-bot.py

# Fix the grammar target
python3 amorce-bot.py --grammar subjonctif
python3 amorce-bot.py --grammar passe
python3 amorce-bot.py --grammar discours_indirect
python3 amorce-bot.py --grammar plus_que_parfait

# Bias the passage toward a topic
python3 amorce-bot.py --seed "médias sociaux"
python3 amorce-bot.py --seed "nature" --grammar subjonctif
```

## What students see

```
── Structure cible : Subjonctif présent ──

Diouf nous rappelle que les grandes entreprises technologiques ont
conçu leurs plateformes pour exploiter notre besoin naturel de
récompenses — un piège dont peu de gens mesurent la profondeur.

Il est essentiel que...
```

Students complete the amorce in a sentence or short paragraph, using the target grammar structure.

## Grammar targets

| Key | Structure | Example amorce |
|-----|-----------|----------------|
| `subjonctif` | Subjonctif présent | *Il est essentiel que...* |
| `passe` | Imparfait / passé composé | *Avant les réseaux sociaux, on...* |
| `discours_indirect` | Discours indirect | *Diouf affirme que...* |
| `plus_que_parfait` | Plus-que-parfait | *On n'avait jamais imaginé que...* |

## Source material

The bot reads all `.md` files in `../inputs/` — including the Diouf introduction and all FR30 course handouts. Add more `.md` files to `inputs/` to expand the passage pool.
