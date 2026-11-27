# Tri d'actions

Petit outil en Python pour trier et filtrer une liste d'actions : variation du jour, capitalisation, PER ou rendement du dividende.

## Classement automatique du CAC 40

Ce tableau se met à jour tout seul : toutes les heures pendant la séance de Paris, GitHub récupère les vrais cours sur Yahoo Finance et refait le tri. Le programme est dans `classement.py`, et l'automatisation dans `.github/workflows/classement.yml`.

<!-- CLASSEMENT:DEBUT -->
_Mis à jour le 27/11/2026 à 10:30 (heure de Paris). Derniers cours : 27/11/2026 10:15, différés d'environ 15 min. Source : Yahoo Finance. 40 valeurs du CAC 40._

### Plus fortes hausses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | STMicroelectronics | +5,26 % |
| 2 | ArcelorMittal | +3,58 % |
| 3 | Legrand | +2,72 % |
| 4 | Thales | +1,92 % |
| 5 | Safran | +1,84 % |

### Plus fortes baisses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | Pernod Ricard | -2,65 % |
| 2 | Sanofi | -2,16 % |
| 3 | Danone | -1,50 % |
| 4 | L'Oréal | -1,22 % |
| 5 | Accor | -1,18 % |

### Plus grandes capitalisations

| # | Société | Capitalisation |
|---:|---|---:|
| 1 | L'Oréal | 234,50 Md€ |
| 2 | LVMH | 195,25 Md€ |
| 3 | TotalEnergies | 172,62 Md€ |
| 4 | Airbus | 155,02 Md€ |
| 5 | Hermès | 133,73 Md€ |
| 6 | Schneider Electric | 130,43 Md€ |
| 7 | Safran | 125,89 Md€ |
| 8 | Air Liquide | 121,39 Md€ |
| 9 | Sanofi | 116,10 Md€ |
| 10 | BNP Paribas | 100,51 Md€ |

### Rendements du dividende les plus élevés

| # | Société | Rendement |
|---:|---|---:|
| 1 | Crédit Agricole | 11,18 % |
| 2 | Renault | 8,04 % |
| 3 | BNP Paribas | 7,32 % |
| 4 | Carrefour | 7,05 % |
| 5 | Pernod Ricard | 6,70 % |
| 6 | Teleperformance | 6,70 % |
| 7 | Engie | 5,53 % |
| 8 | Edenred | 5,25 % |
| 9 | AXA | 5,17 % |
| 10 | Orange | 4,91 % |

### PER les plus bas (bénéfices positifs)

| # | Société | PER |
|---:|---|---:|
| 1 | Michelin | 3,07 |
| 2 | Orange | 3,77 |
| 3 | Carrefour | 6,42 |
| 4 | Crédit Agricole | 7,51 |
| 5 | Société Générale | 7,84 |
| 6 | BNP Paribas | 8,24 |
| 7 | Unibail-Rodamco-Westfield | 8,60 |
| 8 | Teleperformance | 8,71 |
| 9 | TotalEnergies | 8,89 |
| 10 | Renault | 9,39 |
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
