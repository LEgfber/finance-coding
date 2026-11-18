"""Récupérer les vrais chiffres des actions sur Yahoo Finance (gratuit, sans clé)."""

import csv

import yfinance as yf


def lire_symboles(chemin="cac40.csv"):
    with open(chemin, newline="", encoding="utf-8") as f:
        return [(l["symbole"], l["nom"]) for l in csv.DictReader(f)]


def recuperer(symboles):
    """Une action par symbole, au format de tri.py. Chiffre absent chez Yahoo = None (jamais inventé)."""
    actions = []
    for symbole, nom in symboles:
        try:
            info = yf.Ticker(symbole).info
        except Exception as e:  # une valeur en panne ne doit pas bloquer tout le classement
            print(f"{symbole} : indisponible ({e})")
            continue
        cap = info.get("marketCap")
        actions.append({
            "nom": nom,
            "secteur": info.get("sector") or "",
            "variation": info.get("regularMarketChangePercent"),
            "capitalisation": cap / 1e9 if cap else None,
            "per": info.get("trailingPE"),
            "rendement": info.get("dividendYield"),  # déjà en % avec yfinance 1.x
            "heure": info.get("regularMarketTime"),
        })
    return actions
