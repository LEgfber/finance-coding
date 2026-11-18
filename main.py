"""Trier des actions en ligne de commande.

Exemple : python main.py exemple.csv --par rendement --top 5
"""

import argparse

from donnees import lire_csv
from tri import CRITERES, filtrer, trier


def afficher(actions):
    entete = f"{'Nom':<20}{'Secteur':<16}" + "".join(f"{c:>16}" for c in CRITERES)
    print(entete)
    print("-" * len(entete))
    for a in actions:
        valeurs = "".join(f"{'—' if a[c] is None else f'{a[c]:.2f}':>16}" for c in CRITERES)
        print(f"{a['nom']:<20}{a['secteur']:<16}{valeurs}")


def main():
    p = argparse.ArgumentParser(description="Trier une liste d'actions.")
    p.add_argument("fichier", help="fichier CSV des actions")
    p.add_argument("--par", choices=CRITERES, default="variation", help="critère de tri")
    p.add_argument("--croissant", action="store_true", help="du plus petit au plus grand")
    p.add_argument("--min", type=float, help="valeur minimum du critère")
    p.add_argument("--max", type=float, help="valeur maximum du critère")
    p.add_argument("--top", type=int, help="n'afficher que les N premières")
    args = p.parse_args()

    actions = lire_csv(args.fichier)
    if args.min is not None or args.max is not None:
        actions = filtrer(actions, args.par, args.min, args.max)
    actions = trier(actions, args.par, decroissant=not args.croissant)
    afficher(actions[: args.top] if args.top else actions)


if __name__ == "__main__":
    main()
