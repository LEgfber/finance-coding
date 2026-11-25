# Tri d'actions

Petit outil en Python pour trier et filtrer une liste d'actions : variation du jour, capitalisation, PER ou rendement du dividende.

## Classement automatique du CAC 40

Ce tableau se met à jour tout seul : toutes les heures pendant la séance de Paris, GitHub récupère les vrais cours sur Yahoo Finance et refait le tri. Le programme est dans `classement.py`, et l'automatisation dans `.github/workflows/classement.yml`.

<!-- CLASSEMENT:DEBUT -->
_Mis à jour le 25/11/2026 à 18:29 (heure de Paris). Derniers cours : 25/11/2026 17:39, différés d'environ 15 min. Source : Yahoo Finance. 40 valeurs du CAC 40._

### Plus fortes hausses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | Bureau Veritas | +6,60 % |
| 2 | Sanofi | +4,89 % |
| 3 | Stellantis | +3,75 % |
| 4 | Renault | +2,28 % |
| 5 | Unibail-Rodamco-Westfield | +1,41 % |

### Plus fortes baisses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | STMicroelectronics | -4,69 % |
| 2 | Schneider Electric | -4,18 % |
| 3 | Legrand | -3,27 % |
| 4 | Société Générale | -2,96 % |
| 5 | Edenred | -2,86 % |

### Plus grandes capitalisations

| # | Société | Capitalisation |
|---:|---|---:|
| 1 | L'Oréal | 235,73 Md€ |
| 2 | LVMH | 191,84 Md€ |
| 3 | TotalEnergies | 169,29 Md€ |
| 4 | Airbus | 149,94 Md€ |
| 5 | Hermès | 130,96 Md€ |
| 6 | Schneider Electric | 127,31 Md€ |
| 7 | Air Liquide | 120,27 Md€ |
| 8 | Safran | 120,19 Md€ |
| 9 | Sanofi | 117,85 Md€ |
| 10 | BNP Paribas | 96,69 Md€ |

### Rendements du dividende les plus élevés

| # | Société | Rendement |
|---:|---|---:|
| 1 | Crédit Agricole | 11,02 % |
| 2 | Renault | 8,09 % |
| 3 | Carrefour | 7,20 % |
| 4 | BNP Paribas | 7,06 % |
| 5 | Teleperformance | 6,85 % |
| 6 | Pernod Ricard | 6,60 % |
| 7 | Engie | 5,52 % |
| 8 | Edenred | 5,36 % |
| 9 | AXA | 5,11 % |
| 10 | Orange | 5,04 % |

### PER les plus bas (bénéfices positifs)

| # | Société | PER |
|---:|---|---:|
| 1 | Michelin | 3,04 |
| 2 | Orange | 3,76 |
| 3 | Carrefour | 6,40 |
| 4 | Crédit Agricole | 7,35 |
| 5 | Société Générale | 7,53 |
| 6 | BNP Paribas | 7,72 |
| 7 | Renault | 8,37 |
| 8 | Teleperformance | 8,50 |
| 9 | Unibail-Rodamco-Westfield | 8,55 |
| 10 | TotalEnergies | 8,97 |
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
