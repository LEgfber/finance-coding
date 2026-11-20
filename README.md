# Tri d'actions

Petit outil en Python pour trier et filtrer une liste d'actions : variation du jour, capitalisation, PER ou rendement du dividende.

## Classement automatique du CAC 40

Ce tableau se met à jour tout seul : toutes les heures pendant la séance de Paris, GitHub récupère les vrais cours sur Yahoo Finance et refait le tri. Le programme est dans `classement.py`, et l'automatisation dans `.github/workflows/classement.yml`.

<!-- CLASSEMENT:DEBUT -->
_Mis à jour le 20/11/2026 à 14:32 (heure de Paris). Derniers cours : 20/11/2026 14:17, différés d'environ 15 min. Source : Yahoo Finance. 40 valeurs du CAC 40._

### Plus fortes hausses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | Sanofi | +1,71 % |
| 2 | Danone | +0,80 % |
| 3 | Teleperformance | +0,60 % |
| 4 | Orange | +0,47 % |
| 5 | Pernod Ricard | +0,11 % |

### Plus fortes baisses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | STMicroelectronics | -6,70 % |
| 2 | ArcelorMittal | -4,70 % |
| 3 | Hermès | -4,28 % |
| 4 | Legrand | -4,12 % |
| 5 | Schneider Electric | -3,78 % |

### Plus grandes capitalisations

| # | Société | Capitalisation |
|---:|---|---:|
| 1 | L'Oréal | 232,61 Md€ |
| 2 | LVMH | 187,67 Md€ |
| 3 | TotalEnergies | 171,98 Md€ |
| 4 | Airbus | 150,68 Md€ |
| 5 | Schneider Electric | 133,01 Md€ |
| 6 | Hermès | 127,35 Md€ |
| 7 | Safran | 121,59 Md€ |
| 8 | Air Liquide | 119,32 Md€ |
| 9 | Sanofi | 102,32 Md€ |
| 10 | BNP Paribas | 98,63 Md€ |

### Rendements du dividende les plus élevés

| # | Société | Rendement |
|---:|---|---:|
| 1 | Crédit Agricole | 10,92 % |
| 2 | Renault | 8,01 % |
| 3 | Carrefour | 7,06 % |
| 4 | BNP Paribas | 7,02 % |
| 5 | Teleperformance | 6,69 % |
| 6 | Pernod Ricard | 6,55 % |
| 7 | Engie | 5,48 % |
| 8 | Edenred | 5,25 % |
| 9 | AXA | 5,07 % |
| 10 | Orange | 4,93 % |

### PER les plus bas (bénéfices positifs)

| # | Société | PER |
|---:|---|---:|
| 1 | Michelin | 3,04 |
| 2 | Orange | 3,72 |
| 3 | Carrefour | 6,28 |
| 4 | Crédit Agricole | 7,36 |
| 5 | Société Générale | 7,62 |
| 6 | BNP Paribas | 7,87 |
| 7 | Renault | 8,03 |
| 8 | Unibail-Rodamco-Westfield | 8,25 |
| 9 | Teleperformance | 8,42 |
| 10 | TotalEnergies | 8,86 |
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
