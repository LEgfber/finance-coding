# Tri d'actions

Petit outil en Python pour trier et filtrer une liste d'actions : variation du jour, capitalisation, PER ou rendement du dividende.

## Classement automatique du CAC 40

Ce tableau se met à jour tout seul : toutes les heures pendant la séance de Paris, GitHub récupère les vrais cours sur Yahoo Finance et refait le tri. Le programme est dans `classement.py`, et l'automatisation dans `.github/workflows/classement.yml`.

<!-- CLASSEMENT:DEBUT -->
_Mis à jour le 20/11/2026 à 16:14 (heure de Paris). Derniers cours : 20/11/2026 15:59, différés d'environ 15 min. Source : Yahoo Finance. 40 valeurs du CAC 40._

### Plus fortes hausses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | Sanofi | +1,71 % |
| 2 | Capgemini | +1,59 % |
| 3 | Danone | +0,74 % |
| 4 | Teleperformance | +0,69 % |
| 5 | Orange | +0,50 % |

### Plus fortes baisses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | STMicroelectronics | -6,49 % |
| 2 | ArcelorMittal | -4,12 % |
| 3 | Dassault Systèmes | -3,25 % |
| 4 | Renault | -3,20 % |
| 5 | Hermès | -3,07 % |

### Plus grandes capitalisations

| # | Société | Capitalisation |
|---:|---|---:|
| 1 | L'Oréal | 233,14 Md€ |
| 2 | LVMH | 189,41 Md€ |
| 3 | TotalEnergies | 172,68 Md€ |
| 4 | Airbus | 152,98 Md€ |
| 5 | Schneider Electric | 135,16 Md€ |
| 6 | Hermès | 128,98 Md€ |
| 7 | Safran | 123,53 Md€ |
| 8 | Air Liquide | 120,12 Md€ |
| 9 | Sanofi | 102,32 Md€ |
| 10 | BNP Paribas | 99,41 Md€ |

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
| 1 | Michelin | 3,05 |
| 2 | Orange | 3,72 |
| 3 | Carrefour | 6,30 |
| 4 | Crédit Agricole | 7,41 |
| 5 | Société Générale | 7,68 |
| 6 | BNP Paribas | 7,94 |
| 7 | Renault | 8,04 |
| 8 | Unibail-Rodamco-Westfield | 8,35 |
| 9 | Teleperformance | 8,43 |
| 10 | TotalEnergies | 9,15 |
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
