# Tri d'actions

Petit outil en Python pour trier et filtrer une liste d'actions : variation du jour, capitalisation, PER ou rendement du dividende.

## Classement automatique du CAC 40

Ce tableau se met à jour tout seul : toutes les heures pendant la séance de Paris, GitHub récupère les vrais cours sur Yahoo Finance et refait le tri. Le programme est dans `classement.py`, et l'automatisation dans `.github/workflows/classement.yml`.

<!-- CLASSEMENT:DEBUT -->
_Mis à jour le 24/11/2026 à 12:12 (heure de Paris). Derniers cours : 24/11/2026 11:57, différés d'environ 15 min. Source : Yahoo Finance. 40 valeurs du CAC 40._

### Plus fortes hausses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | Sanofi | +5,97 % |
| 2 | Orange | +1,65 % |
| 3 | Edenred | +1,17 % |
| 4 | Thales | +1,15 % |
| 5 | Teleperformance | +1,10 % |

### Plus fortes baisses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | ArcelorMittal | -4,71 % |
| 2 | STMicroelectronics | -4,10 % |
| 3 | Stellantis | -3,37 % |
| 4 | Legrand | -1,73 % |
| 5 | Kering | -1,43 % |

### Plus grandes capitalisations

| # | Société | Capitalisation |
|---:|---|---:|
| 1 | L'Oréal | 233,03 Md€ |
| 2 | LVMH | 190,93 Md€ |
| 3 | TotalEnergies | 168,76 Md€ |
| 4 | Airbus | 153,69 Md€ |
| 5 | Schneider Electric | 136,77 Md€ |
| 6 | Hermès | 130,18 Md€ |
| 7 | Safran | 124,44 Md€ |
| 8 | Air Liquide | 120,05 Md€ |
| 9 | Sanofi | 108,47 Md€ |
| 10 | BNP Paribas | 100,05 Md€ |

### Rendements du dividende les plus élevés

| # | Société | Rendement |
|---:|---|---:|
| 1 | Crédit Agricole | 11,11 % |
| 2 | Renault | 8,42 % |
| 3 | BNP Paribas | 7,21 % |
| 4 | Carrefour | 7,19 % |
| 5 | Teleperformance | 6,78 % |
| 6 | Pernod Ricard | 6,60 % |
| 7 | Engie | 5,56 % |
| 8 | Edenred | 5,47 % |
| 9 | AXA | 5,14 % |
| 10 | Unibail-Rodamco-Westfield | 5,00 % |

### PER les plus bas (bénéfices positifs)

| # | Société | PER |
|---:|---|---:|
| 1 | Michelin | 3,06 |
| 2 | Orange | 3,73 |
| 3 | Carrefour | 6,31 |
| 4 | Crédit Agricole | 7,43 |
| 5 | Société Générale | 7,81 |
| 6 | BNP Paribas | 7,99 |
| 7 | Renault | 8,22 |
| 8 | Teleperformance | 8,39 |
| 9 | Unibail-Rodamco-Westfield | 8,42 |
| 10 | TotalEnergies | 8,94 |
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
