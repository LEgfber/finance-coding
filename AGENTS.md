# Instructions pour les assistants IA

> **Ce fichier n'est utile que si tu travailles sur ce projet avec un assistant IA de programmation.** Sinon, tu peux l'ignorer : il ne change rien au fonctionnement de l'outil. Pour utiliser l'outil, lis le [README](README.md).

## Le projet

Outil Python qui trie et filtre des actions (variation du jour, capitalisation, PER, rendement du dividende), avec un classement du CAC 40 mis à jour automatiquement par GitHub Actions.

| Fichier | Rôle |
|---|---|
| `tri.py` | tri et filtre ; liste des critères dans `CRITERES` |
| `donnees.py` | lecture d'un fichier CSV |
| `main.py` | ligne de commande |
| `marche.py` | cours réels depuis Yahoo Finance (`yfinance`) |
| `classement.py` | génère le classement et l'écrit dans le README entre les balises `CLASSEMENT:DEBUT` et `CLASSEMENT:FIN` |
| `cac40.csv` | symboles Yahoo et noms des 40 valeurs |
| `.github/workflows/classement.yml` | lancement automatique toutes les heures en séance |

## Commandes

```bash
pip install -r requirements.txt
python test_tri.py          # tests, sans Internet
python classement.py        # classement avec les vrais cours
python main.py exemple.csv --par rendement --top 3
```

## Règles

- Aucun chiffre inventé : une donnée absente vaut `None` et s'affiche « — ». Chaque classement indique sa source, son heure et le différé des cours.
- Information seulement : jamais de conseil d'achat ou de vente, ni de recommandation.
- Python standard ; seule dépendance : `yfinance`. N'en ajoute pas sans raison.
- Ne modifie pas à la main le tableau entre les balises du README : il est réécrit à chaque mise à jour.
- Lance `python test_tri.py` après chaque modification.
- Textes et messages en français.
