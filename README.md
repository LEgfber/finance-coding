# Tri d'actions

Petit outil en Python pour trier et filtrer une liste d'actions : variation du jour, capitalisation, PER ou rendement du dividende.

## Classement automatique du CAC 40

Ce tableau se met à jour tout seul : toutes les heures pendant la séance de Paris, GitHub récupère les vrais cours sur Yahoo Finance et refait le tri. Le programme est dans `classement.py`, et l'automatisation dans `.github/workflows/classement.yml`.

<!-- CLASSEMENT:DEBUT -->
_Mis à jour le 26/11/2026 à 10:30 (heure de Paris). Derniers cours : 26/11/2026 10:15, différés d'environ 15 min. Source : Yahoo Finance. 40 valeurs du CAC 40._

### Plus fortes hausses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | Stellantis | +5,50 % |
| 2 | STMicroelectronics | +5,20 % |
| 3 | Safran | +4,02 % |
| 4 | ArcelorMittal | +3,88 % |
| 5 | Renault | +3,65 % |

### Plus fortes baisses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | Danone | -0,06 % |
| 2 | Carrefour | +0,33 % |
| 3 | Dassault Systèmes | +0,68 % |
| 4 | Pernod Ricard | +0,77 % |
| 5 | TotalEnergies | +0,84 % |

### Plus grandes capitalisations

| # | Société | Capitalisation |
|---:|---|---:|
| 1 | L'Oréal | 237,89 Md€ |
| 2 | LVMH | 197,55 Md€ |
| 3 | TotalEnergies | 170,71 Md€ |
| 4 | Airbus | 154,40 Md€ |
| 5 | Hermès | 134,05 Md€ |
| 6 | Schneider Electric | 129,60 Md€ |
| 7 | Safran | 125,02 Md€ |
| 8 | Air Liquide | 121,69 Md€ |
| 9 | Sanofi | 119,08 Md€ |
| 10 | BNP Paribas | 99,43 Md€ |

### Rendements du dividende les plus élevés

| # | Société | Rendement |
|---:|---|---:|
| 1 | Crédit Agricole | 11,06 % |
| 2 | Renault | 8,22 % |
| 3 | BNP Paribas | 7,16 % |
| 4 | Carrefour | 7,04 % |
| 5 | Teleperformance | 6,68 % |
| 6 | Pernod Ricard | 6,52 % |
| 7 | Engie | 5,48 % |
| 8 | Edenred | 5,22 % |
| 9 | AXA | 5,12 % |
| 10 | Bouygues | 4,96 % |

### PER les plus bas (bénéfices positifs)

| # | Société | PER |
|---:|---|---:|
| 1 | Michelin | 3,10 |
| 2 | Orange | 3,80 |
| 3 | Carrefour | 6,42 |
| 4 | Crédit Agricole | 7,46 |
| 5 | Société Générale | 7,51 |
| 6 | BNP Paribas | 7,75 |
| 7 | Unibail-Rodamco-Westfield | 8,66 |
| 8 | Teleperformance | 8,66 |
| 9 | TotalEnergies | 8,80 |
| 10 | Renault | 8,87 |
<!-- CLASSEMENT:FIN -->

## Tri d'un fichier CSV

```bash
python main.py exemple.csv --par rendement --top 3
python main.py exemple.csv --par per --croissant --min 5 --max 20
```

| Option | Rôle |
|---|---|
| `--par` | critère : `variation`, `capitalisation`, `per`, `rendement` |
| `--croissant` | du plus petit au plus grand (par défaut : du plus grand au plus petit) |
| `--min`, `--max` | ne garde que les actions dans cet intervalle |
| `--top N` | n'affiche que les N premières |

Une valeur absente s'affiche « — » et reste toujours en fin de liste.

## Données

Un fichier CSV avec les colonnes `nom,secteur,variation,capitalisation,per,rendement`. Le fichier `exemple.csv` contient des sociétés **fictives**, seulement pour essayer l'outil.

## Tests

```bash
python test_tri.py
```

Pour lancer le classement en direct sur ton ordinateur :

```bash
pip install -r requirements.txt
python classement.py
```

## Avertissement

Outil d'information uniquement, ce n'est pas un conseil d'achat ou de vente.

## Droits

© LEgfber. Tous droits réservés. Aucune licence n'est accordée : le code peut être lu, mais pas copié, modifié ni réutilisé sans autorisation écrite.
