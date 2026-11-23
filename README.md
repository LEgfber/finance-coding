# Tri d'actions

Petit outil en Python pour trier et filtrer une liste d'actions : variation du jour, capitalisation, PER ou rendement du dividende.

## Classement automatique du CAC 40

Ce tableau se met à jour tout seul : toutes les heures pendant la séance de Paris, GitHub récupère les vrais cours sur Yahoo Finance et refait le tri. Le programme est dans `classement.py`, et l'automatisation dans `.github/workflows/classement.yml`.

<!-- CLASSEMENT:DEBUT -->
_Mis à jour le 23/11/2026 à 10:42 (heure de Paris). Derniers cours : 23/11/2026 10:27, différés d'environ 15 min. Source : Yahoo Finance. 40 valeurs du CAC 40._

### Plus fortes hausses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | ArcelorMittal | +2,83 % |
| 2 | STMicroelectronics | +2,14 % |
| 3 | Legrand | +2,04 % |
| 4 | Safran | +2,02 % |
| 5 | Schneider Electric | +1,86 % |

### Plus fortes baisses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | Dassault Systèmes | -1,26 % |
| 2 | Publicis | -1,16 % |
| 3 | Stellantis | -1,07 % |
| 4 | Carrefour | -0,74 % |
| 5 | Orange | -0,63 % |

### Plus grandes capitalisations

| # | Société | Capitalisation |
|---:|---|---:|
| 1 | L'Oréal | 232,87 Md€ |
| 2 | LVMH | 186,88 Md€ |
| 3 | TotalEnergies | 171,46 Md€ |
| 4 | Airbus | 152,41 Md€ |
| 5 | Schneider Electric | 135,60 Md€ |
| 6 | Hermès | 127,41 Md€ |
| 7 | Safran | 123,37 Md€ |
| 8 | Air Liquide | 119,20 Md€ |
| 9 | Sanofi | 102,16 Md€ |
| 10 | BNP Paribas | 99,22 Md€ |

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
| 2 | Orange | 3,70 |
| 3 | Carrefour | 6,23 |
| 4 | Crédit Agricole | 7,40 |
| 5 | Société Générale | 7,67 |
| 6 | BNP Paribas | 7,92 |
| 7 | Renault | 8,09 |
| 8 | Teleperformance | 8,42 |
| 9 | Unibail-Rodamco-Westfield | 8,47 |
| 10 | TotalEnergies | 8,83 |
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
