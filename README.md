# Tri d'actions

Petit outil en Python pour trier et filtrer une liste d'actions : variation du jour, capitalisation, PER ou rendement du dividende.

## Classement automatique du CAC 40

Ce tableau se met à jour tout seul : toutes les heures pendant la séance de Paris, GitHub récupère les vrais cours sur Yahoo Finance et refait le tri. Le programme est dans `classement.py`, et l'automatisation dans `.github/workflows/classement.yml`.

<!-- CLASSEMENT:DEBUT -->
_Mis à jour le 18/11/2026 à 23:06 (heure de Paris). Derniers cours : 18/11/2026 17:39, différés d'environ 15 min. Source : Yahoo Finance. 40 valeurs du CAC 40._

### Plus fortes hausses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | STMicroelectronics | +1,80 % |
| 2 | Legrand | +1,61 % |
| 3 | Bureau Veritas | +1,44 % |
| 4 | EssilorLuxottica | +1,12 % |
| 5 | Schneider Electric | +0,61 % |

### Plus fortes baisses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | Accor | -4,23 % |
| 2 | Dassault Systèmes | -3,89 % |
| 3 | Teleperformance | -2,86 % |
| 4 | TotalEnergies | -2,65 % |
| 5 | Société Générale | -2,51 % |

### Plus grandes capitalisations

| # | Société | Capitalisation |
|---:|---|---:|
| 1 | L'Oréal | 236,29 Md€ |
| 2 | LVMH | 190,41 Md€ |
| 3 | TotalEnergies | 175,03 Md€ |
| 4 | Airbus | 156,08 Md€ |
| 5 | Schneider Electric | 139,89 Md€ |
| 6 | Hermès | 133,73 Md€ |
| 7 | Safran | 125,76 Md€ |
| 8 | Air Liquide | 121,09 Md€ |
| 9 | Sanofi | 103,55 Md€ |
| 10 | BNP Paribas | 100,83 Md€ |

### Rendements du dividende les plus élevés

| # | Société | Rendement |
|---:|---|---:|
| 1 | Crédit Agricole | 10,73 % |
| 2 | Renault | 7,89 % |
| 3 | Carrefour | 6,82 % |
| 4 | BNP Paribas | 6,77 % |
| 5 | Pernod Ricard | 6,41 % |
| 6 | Teleperformance | 6,23 % |
| 7 | Engie | 5,38 % |
| 8 | Edenred | 5,14 % |
| 9 | AXA | 4,96 % |
| 10 | Orange | 4,80 % |

### PER les plus bas (bénéfices positifs)

| # | Société | PER |
|---:|---|---:|
| 1 | Michelin | 3,15 |
| 2 | Orange | 3,75 |
| 3 | Carrefour | 6,39 |
| 4 | Société Générale | 7,86 |
| 5 | Crédit Agricole | 7,94 |
| 6 | BNP Paribas | 8,05 |
| 7 | Renault | 8,39 |
| 8 | Teleperformance | 8,50 |
| 9 | Unibail-Rodamco-Westfield | 8,56 |
| 10 | TotalEnergies | 9,26 |
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
