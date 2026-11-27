# Tri d'actions

Petit outil en Python pour trier et filtrer une liste d'actions : variation du jour, capitalisation, PER ou rendement du dividende.

## Classement automatique du CAC 40

Ce tableau se met à jour tout seul : toutes les heures pendant la séance de Paris, GitHub récupère les vrais cours sur Yahoo Finance et refait le tri. Le programme est dans `classement.py`, et l'automatisation dans `.github/workflows/classement.yml`.

<!-- CLASSEMENT:DEBUT -->
_Mis à jour le 27/11/2026 à 16:17 (heure de Paris). Derniers cours : 27/11/2026 16:02, différés d'environ 15 min. Source : Yahoo Finance. 40 valeurs du CAC 40._

### Plus fortes hausses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | ArcelorMittal | +3,70 % |
| 2 | Thales | +2,14 % |
| 3 | STMicroelectronics | +2,00 % |
| 4 | Société Générale | +1,57 % |
| 5 | Dassault Systèmes | +1,52 % |

### Plus fortes baisses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | Pernod Ricard | -1,35 % |
| 2 | Sanofi | -1,04 % |
| 3 | Michelin | -0,95 % |
| 4 | Accor | -0,81 % |
| 5 | Edenred | -0,67 % |

### Plus grandes capitalisations

| # | Société | Capitalisation |
|---:|---|---:|
| 1 | L'Oréal | 236,69 Md€ |
| 2 | LVMH | 196,25 Md€ |
| 3 | TotalEnergies | 172,64 Md€ |
| 4 | Airbus | 154,29 Md€ |
| 5 | Hermès | 134,15 Md€ |
| 6 | Schneider Electric | 128,40 Md€ |
| 7 | Safran | 125,14 Md€ |
| 8 | Air Liquide | 122,50 Md€ |
| 9 | Sanofi | 117,42 Md€ |
| 10 | BNP Paribas | 100,57 Md€ |

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
| 1 | Michelin | 3,06 |
| 2 | Orange | 3,81 |
| 3 | Carrefour | 6,44 |
| 4 | Crédit Agricole | 7,50 |
| 5 | Société Générale | 7,86 |
| 6 | BNP Paribas | 8,03 |
| 7 | Unibail-Rodamco-Westfield | 8,65 |
| 8 | Teleperformance | 8,68 |
| 9 | TotalEnergies | 8,90 |
| 10 | Renault | 8,94 |
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
