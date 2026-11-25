# Tri d'actions

Petit outil en Python pour trier et filtrer une liste d'actions : variation du jour, capitalisation, PER ou rendement du dividende.

## Classement automatique du CAC 40

Ce tableau se met à jour tout seul : toutes les heures pendant la séance de Paris, GitHub récupère les vrais cours sur Yahoo Finance et refait le tri. Le programme est dans `classement.py`, et l'automatisation dans `.github/workflows/classement.yml`.

<!-- CLASSEMENT:DEBUT -->
_Mis à jour le 25/11/2026 à 15:35 (heure de Paris). Derniers cours : 25/11/2026 15:19, différés d'environ 15 min. Source : Yahoo Finance. 40 valeurs du CAC 40._

### Plus fortes hausses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | Bureau Veritas | +7,07 % |
| 2 | Sanofi | +4,96 % |
| 3 | Stellantis | +4,05 % |
| 4 | Renault | +3,21 % |
| 5 | Unibail-Rodamco-Westfield | +1,82 % |

### Plus fortes baisses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | STMicroelectronics | -2,57 % |
| 2 | Eurofins Scientific | -2,31 % |
| 3 | Schneider Electric | -1,95 % |
| 4 | Edenred | -1,81 % |
| 5 | Société Générale | -1,76 % |

### Plus grandes capitalisations

| # | Société | Capitalisation |
|---:|---|---:|
| 1 | L'Oréal | 236,07 Md€ |
| 2 | LVMH | 195,52 Md€ |
| 3 | TotalEnergies | 170,69 Md€ |
| 4 | Airbus | 151,81 Md€ |
| 5 | Hermès | 132,22 Md€ |
| 6 | Schneider Electric | 130,28 Md€ |
| 7 | Safran | 123,00 Md€ |
| 8 | Air Liquide | 120,24 Md€ |
| 9 | Sanofi | 117,92 Md€ |
| 10 | BNP Paribas | 98,21 Md€ |

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
| 1 | Michelin | 3,07 |
| 2 | Orange | 3,78 |
| 3 | Carrefour | 6,41 |
| 4 | Crédit Agricole | 7,38 |
| 5 | Société Générale | 7,62 |
| 6 | BNP Paribas | 7,84 |
| 7 | Renault | 8,45 |
| 8 | Teleperformance | 8,49 |
| 9 | Unibail-Rodamco-Westfield | 8,58 |
| 10 | TotalEnergies | 8,79 |
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
