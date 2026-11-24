# Tri d'actions

Petit outil en Python pour trier et filtrer une liste d'actions : variation du jour, capitalisation, PER ou rendement du dividende.

## Classement automatique du CAC 40

Ce tableau se met à jour tout seul : toutes les heures pendant la séance de Paris, GitHub récupère les vrais cours sur Yahoo Finance et refait le tri. Le programme est dans `classement.py`, et l'automatisation dans `.github/workflows/classement.yml`.

<!-- CLASSEMENT:DEBUT -->
_Mis à jour le 24/11/2026 à 14:39 (heure de Paris). Derniers cours : 24/11/2026 14:24, différés d'environ 15 min. Source : Yahoo Finance. 40 valeurs du CAC 40._

### Plus fortes hausses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | Sanofi | +6,87 % |
| 2 | Orange | +1,55 % |
| 3 | Thales | +1,23 % |
| 4 | Teleperformance | +1,10 % |
| 5 | Danone | +1,03 % |

### Plus fortes baisses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | STMicroelectronics | -5,50 % |
| 2 | ArcelorMittal | -5,04 % |
| 3 | Stellantis | -3,40 % |
| 4 | Legrand | -2,15 % |
| 5 | Schneider Electric | -1,89 % |

### Plus grandes capitalisations

| # | Société | Capitalisation |
|---:|---|---:|
| 1 | L'Oréal | 233,17 Md€ |
| 2 | LVMH | 190,44 Md€ |
| 3 | TotalEnergies | 168,87 Md€ |
| 4 | Airbus | 153,61 Md€ |
| 5 | Schneider Electric | 135,98 Md€ |
| 6 | Hermès | 129,13 Md€ |
| 7 | Safran | 125,06 Md€ |
| 8 | Air Liquide | 120,07 Md€ |
| 9 | Sanofi | 109,40 Md€ |
| 10 | BNP Paribas | 99,54 Md€ |

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
| 1 | Michelin | 3,05 |
| 2 | Orange | 3,72 |
| 3 | Carrefour | 6,30 |
| 4 | Crédit Agricole | 7,43 |
| 5 | Société Générale | 7,80 |
| 6 | BNP Paribas | 7,95 |
| 7 | Renault | 8,23 |
| 8 | Teleperformance | 8,39 |
| 9 | Unibail-Rodamco-Westfield | 8,40 |
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
