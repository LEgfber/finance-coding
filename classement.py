"""Classement automatique du CAC 40, écrit dans le README entre deux balises.

Lancé toutes les heures en séance par GitHub (voir .github/workflows/classement.yml).
"""

import re
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

from marche import lire_symboles, recuperer
from tri import filtrer, trier

DEBUT, FIN = "<!-- CLASSEMENT:DEBUT -->", "<!-- CLASSEMENT:FIN -->"
PARIS = ZoneInfo("Europe/Paris")


def _n(v, suffixe=""):
    return "—" if v is None else f"{v:,.2f}".replace(",", " ").replace(".", ",") + suffixe


def _signe(v):
    return "—" if v is None else ("+" if v > 0 else "") + _n(v, " %")


def tableau(titre, actions, colonne, format_):
    lignes = [f"### {titre}", "", f"| # | Société | {colonne} |", "|---:|---|---:|"]
    lignes += [f"| {i} | {a['nom']} | {format_(a)} |" for i, a in enumerate(actions, 1)]
    return "\n".join(lignes)


def generer(actions, maintenant):
    heures = [a["heure"] for a in actions if a.get("heure")]
    cours = datetime.fromtimestamp(max(heures), PARIS).strftime("%d/%m/%Y %H:%M") if heures else "—"
    blocs = [
        f"_Mis à jour le {maintenant.astimezone(PARIS).strftime('%d/%m/%Y à %H:%M')} (heure de Paris). "
        f"Derniers cours : {cours}, différés d'environ 15 min. "
        f"Source : Yahoo Finance. {len(actions)} valeurs du CAC 40._",
        tableau("Plus fortes hausses du jour", trier(actions, "variation")[:5], "Variation", lambda a: _signe(a["variation"])),
        tableau("Plus fortes baisses du jour", trier(actions, "variation", decroissant=False)[:5], "Variation", lambda a: _signe(a["variation"])),
        tableau("Plus grandes capitalisations", trier(actions, "capitalisation")[:10], "Capitalisation", lambda a: _n(a["capitalisation"], " Md€")),
        tableau("Rendements du dividende les plus élevés", trier(actions, "rendement")[:10], "Rendement", lambda a: _n(a["rendement"], " %")),
        tableau("PER les plus bas (bénéfices positifs)", trier(filtrer(actions, "per", minimum=0.01), "per", decroissant=False)[:10], "PER", lambda a: _n(a["per"])),
    ]
    return "\n\n".join(blocs)


def inserer(readme, contenu):
    motif = re.compile(re.escape(DEBUT) + ".*?" + re.escape(FIN), re.S)
    if not motif.search(readme):
        raise ValueError("Balises du classement introuvables dans le README")
    return motif.sub(lambda _: f"{DEBUT}\n{contenu}\n{FIN}", readme)


def main():
    actions = recuperer(lire_symboles())
    if len(actions) < 20:  # Yahoo en panne : on garde l'ancien classement plutôt qu'un tableau vide
        sys.exit(f"Seulement {len(actions)} valeurs récupérées, README inchangé.")
    with open("README.md", encoding="utf-8") as f:
        readme = f.read()
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(inserer(readme, generer(actions, datetime.now(PARIS))))
    print(f"Classement mis à jour : {len(actions)} valeurs.")


if __name__ == "__main__":
    main()
