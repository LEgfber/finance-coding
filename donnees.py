"""Lire une liste d'actions depuis un fichier CSV."""

import csv

from tri import CRITERES


def _nombre(texte):
    texte = (texte or "").strip().replace(",", ".")
    if texte in ("", "-", "—"):
        return None
    return float(texte)


def lire_csv(chemin):
    """Une ligne par action : colonnes nom, secteur et les critères de tri. Case vide = valeur absente."""
    with open(chemin, newline="", encoding="utf-8") as f:
        actions = []
        for ligne in csv.DictReader(f):
            action = {"nom": ligne["nom"].strip(), "secteur": (ligne.get("secteur") or "").strip()}
            for critere in CRITERES:
                action[critere] = _nombre(ligne.get(critere))
            actions.append(action)
    return actions
