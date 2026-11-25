# Tri d'actions

Petit outil en Python pour trier et filtrer une liste d'actions : variation du jour, capitalisation, PER ou rendement du dividende.

## Classement automatique du CAC 40

Ce tableau se met à jour tout seul : toutes les heures pendant la séance de Paris, GitHub récupère les vrais cours sur Yahoo Finance et refait le tri. Le programme est dans `classement.py`, et l'automatisation dans `.github/workflows/classement.yml`.

<!-- CLASSEMENT:DEBUT -->
_Mis à jour le 25/11/2026 à 17:29 (heure de Paris). Derniers cours : 25/11/2026 17:14, différés d'environ 15 min. Source : Yahoo Finance. 40 valeurs du CAC 40._

### Plus fortes hausses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | Bureau Veritas | +7,11 % |
| 2 | Sanofi | +5,10 % |
| 3 | Stellantis | +3,78 % |
| 4 | Renault | +2,35 % |
| 5 | Unibail-Rodamco-Westfield | +1,65 % |

### Plus fortes baisses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | STMicroelectronics | -4,53 % |
| 2 | Schneider Electric | -4,40 % |
| 3 | Legrand | -2,79 % |
| 4 | Société Générale | -2,63 % |
| 5 | Safran | -2,47 % |

### Plus grandes capitalisations

| # | Société | Capitalisation |
|---:|---|---:|
| 1 | L'Oréal | 236,13 Md€ |
| 2 | LVMH | 192,47 Md€ |
| 3 | TotalEnergies | 170,69 Md€ |
| 4 | Airbus | 150,08 Md€ |
| 5 | Hermès | 130,96 Md€ |
| 6 | Schneider Electric | 127,02 Md€ |
| 7 | Safran | 120,52 Md€ |
| 8 | Air Liquide | 120,23 Md€ |
| 9 | Sanofi | 118,08 Md€ |
| 10 | BNP Paribas | 96,80 Md€ |

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
| 2 | Orange | 3,77 |
| 3 | Carrefour | 6,40 |
| 4 | Crédit Agricole | 7,35 |
| 5 | Société Générale | 7,55 |
| 6 | BNP Paribas | 7,73 |
| 7 | Renault | 8,38 |
| 8 | Teleperformance | 8,56 |
| 9 | Unibail-Rodamco-Westfield | 8,57 |
| 10 | TotalEnergies | 9,04 |
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
