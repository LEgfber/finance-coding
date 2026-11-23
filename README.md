# Tri d'actions

Petit outil en Python pour trier et filtrer une liste d'actions : variation du jour, capitalisation, PER ou rendement du dividende.

## Classement automatique du CAC 40

Ce tableau se met à jour tout seul : toutes les heures pendant la séance de Paris, GitHub récupère les vrais cours sur Yahoo Finance et refait le tri. Le programme est dans `classement.py`, et l'automatisation dans `.github/workflows/classement.yml`.

<!-- CLASSEMENT:DEBUT -->
_Mis à jour le 23/11/2026 à 16:27 (heure de Paris). Derniers cours : 23/11/2026 16:12, différés d'environ 15 min. Source : Yahoo Finance. 40 valeurs du CAC 40._

### Plus fortes hausses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | STMicroelectronics | +10,02 % |
| 2 | ArcelorMittal | +4,53 % |
| 3 | Legrand | +4,44 % |
| 4 | Schneider Electric | +4,32 % |
| 5 | Société Générale | +3,55 % |

### Plus fortes baisses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | Orange | -1,92 % |
| 2 | Danone | -1,44 % |
| 3 | Dassault Systèmes | -1,12 % |
| 4 | EssilorLuxottica | -1,00 % |
| 5 | Carrefour | -0,96 % |

### Plus grandes capitalisations

| # | Société | Capitalisation |
|---:|---|---:|
| 1 | L'Oréal | 232,13 Md€ |
| 2 | LVMH | 190,24 Md€ |
| 3 | TotalEnergies | 170,23 Md€ |
| 4 | Airbus | 153,76 Md€ |
| 5 | Schneider Electric | 138,89 Md€ |
| 6 | Hermès | 130,65 Md€ |
| 7 | Safran | 124,90 Md€ |
| 8 | Air Liquide | 119,11 Md€ |
| 9 | Sanofi | 101,91 Md€ |
| 10 | BNP Paribas | 100,77 Md€ |

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
| 1 | Michelin | 3,07 |
| 2 | Orange | 3,65 |
| 3 | Carrefour | 6,22 |
| 4 | Crédit Agricole | 7,46 |
| 5 | Société Générale | 7,84 |
| 6 | BNP Paribas | 8,04 |
| 7 | Renault | 8,27 |
| 8 | Teleperformance | 8,36 |
| 9 | Unibail-Rodamco-Westfield | 8,42 |
| 10 | TotalEnergies | 9,02 |
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
