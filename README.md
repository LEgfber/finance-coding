# Tri d'actions

Petit outil en Python pour trier et filtrer une liste d'actions : variation du jour, capitalisation, PER ou rendement du dividende.

## Classement automatique du CAC 40

Ce tableau se met à jour tout seul : toutes les heures pendant la séance de Paris, GitHub récupère les vrais cours sur Yahoo Finance et refait le tri. Le programme est dans `classement.py`, et l'automatisation dans `.github/workflows/classement.yml`.

<!-- CLASSEMENT:DEBUT -->
_Mis à jour le 24/11/2026 à 10:30 (heure de Paris). Derniers cours : 24/11/2026 10:15, différés d'environ 15 min. Source : Yahoo Finance. 40 valeurs du CAC 40._

### Plus fortes hausses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | Sanofi | +5,91 % |
| 2 | Edenred | +1,61 % |
| 3 | Thales | +1,37 % |
| 4 | Orange | +0,94 % |
| 5 | Carrefour | +0,89 % |

### Plus fortes baisses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | ArcelorMittal | -3,09 % |
| 2 | STMicroelectronics | -2,69 % |
| 3 | Kering | -1,15 % |
| 4 | Stellantis | -1,04 % |
| 5 | Dassault Systèmes | -0,72 % |

### Plus grandes capitalisations

| # | Société | Capitalisation |
|---:|---|---:|
| 1 | L'Oréal | 232,85 Md€ |
| 2 | LVMH | 190,41 Md€ |
| 3 | TotalEnergies | 168,72 Md€ |
| 4 | Airbus | 154,01 Md€ |
| 5 | Schneider Electric | 138,21 Md€ |
| 6 | Hermès | 129,97 Md€ |
| 7 | Safran | 125,06 Md€ |
| 8 | Air Liquide | 119,92 Md€ |
| 9 | Sanofi | 108,41 Md€ |
| 10 | BNP Paribas | 100,31 Md€ |

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
| 1 | Michelin | 3,09 |
| 2 | Orange | 3,70 |
| 3 | Carrefour | 6,32 |
| 4 | Crédit Agricole | 7,45 |
| 5 | Société Générale | 7,85 |
| 6 | BNP Paribas | 8,18 |
| 7 | Teleperformance | 8,25 |
| 8 | Unibail-Rodamco-Westfield | 8,53 |
| 9 | Renault | 8,61 |
| 10 | TotalEnergies | 8,69 |
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
