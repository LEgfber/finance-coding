"""Lancer : python test_tri.py"""

from donnees import lire_csv
from tri import filtrer, trier

actions = lire_csv("exemple.csv")
assert len(actions) == 6

# Tri décroissant par variation
noms = [a["nom"] for a in trier(actions, "variation")]
assert noms[0] == "Société Delta" and noms[-1] == "Société Epsilon", noms

# Les valeurs absentes restent à la fin, dans les deux sens
assert trier(actions, "rendement")[-1]["nom"] == "Société Epsilon"
assert trier(actions, "rendement", decroissant=False)[-1]["nom"] == "Société Epsilon"
assert trier(actions, "rendement", decroissant=False)[0]["nom"] == "Société Zêta"

# Filtre avec bornes incluses, valeurs absentes exclues
assert {a["nom"] for a in filtrer(actions, "per", 9.5, 18.3)} == {"Société Alpha", "Société Delta", "Société Epsilon"}

# Critère inconnu refusé
try:
    trier(actions, "prix")
    raise AssertionError("critère inconnu accepté")
except ValueError:
    pass

# Classement : génération et insertion dans le README (sans Internet, yfinance non requis)
import sys, types
sys.modules.setdefault("yfinance", types.ModuleType("yfinance"))
from datetime import datetime, timezone
from classement import DEBUT, FIN, generer, inserer

texte = generer(actions, datetime(2026, 1, 5, 9, 0, tzinfo=timezone.utc))
assert "| 1 | Société Delta | +2,10 % |" in texte, texte
assert "| 1 | Société Bêta | 320,00 Md€ |" in texte
assert "Société Zêta" not in texte.split("PER les plus bas")[1]  # PER absent exclu
readme = inserer(f"avant\n{DEBUT}\nancien\n{FIN}\naprès", "nouveau")
assert readme == f"avant\n{DEBUT}\nnouveau\n{FIN}\naprès", readme
try:
    inserer("sans balises", "x")
    raise AssertionError("balises manquantes acceptées")
except ValueError:
    pass

print("Tous les tests passent.")
