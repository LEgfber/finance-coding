# Tri d'actions

Petit outil en Python pour trier et filtrer une liste d'actions : variation du jour, capitalisation, PER ou rendement du dividende.

## Classement automatique du CAC 40

Ce tableau se met à jour tout seul : toutes les heures pendant la séance de Paris, GitHub récupère les vrais cours sur Yahoo Finance et refait le tri. Le programme est dans `classement.py`, et l'automatisation dans `.github/workflows/classement.yml`.

<!-- CLASSEMENT:DEBUT -->
_Mis à jour le 19/11/2026 à 14:40 (heure de Paris). Derniers cours : 19/11/2026 14:25, différés d'environ 15 min. Source : Yahoo Finance. 40 valeurs du CAC 40._

### Plus fortes hausses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | STMicroelectronics | +4,43 % |
| 2 | Kering | +1,53 % |
| 3 | Airbus | +1,40 % |
| 4 | Thales | +1,37 % |
| 5 | Legrand | +1,37 % |

### Plus fortes baisses du jour

| # | Société | Variation |
|---:|---|---:|
| 1 | Sanofi | -2,55 % |
| 2 | Danone | -2,49 % |
| 3 | Capgemini | -2,18 % |
| 4 | EssilorLuxottica | -1,77 % |
| 5 | Accor | -1,77 % |

### Plus grandes capitalisations

| # | Société | Capitalisation |
|---:|---|---:|
| 1 | L'Oréal | 233,14 Md€ |
| 2 | LVMH | 192,96 Md€ |
| 3 | TotalEnergies | 174,50 Md€ |
| 4 | Airbus | 158,26 Md€ |
| 5 | Schneider Electric | 141,06 Md€ |
| 6 | Hermès | 135,20 Md€ |
| 7 | Safran | 125,52 Md€ |
| 8 | Air Liquide | 121,06 Md€ |
| 9 | BNP Paribas | 101,90 Md€ |
| 10 | Sanofi | 100,91 Md€ |

### Rendements du dividende les plus élevés

| # | Société | Rendement |
|---:|---|---:|
| 1 | Crédit Agricole | 10,83 % |
| 2 | Renault | 7,95 % |
| 3 | Carrefour | 6,91 % |
| 4 | BNP Paribas | 6,89 % |
| 5 | Pernod Ricard | 6,50 % |
| 6 | Teleperformance | 6,50 % |
| 7 | Engie | 5,46 % |
| 8 | Edenred | 5,22 % |
| 9 | AXA | 5,03 % |
| 10 | Orange | 4,86 % |

### PER les plus bas (bénéfices positifs)

| # | Société | PER |
|---:|---|---:|
| 1 | Michelin | 3,11 |
| 2 | Orange | 3,70 |
| 3 | Carrefour | 6,33 |
| 4 | Crédit Agricole | 7,51 |
| 5 | Société Générale | 7,92 |
| 6 | BNP Paribas | 8,13 |
| 7 | Renault | 8,39 |
| 8 | Unibail-Rodamco-Westfield | 8,46 |
| 9 | Teleperformance | 8,48 |
| 10 | TotalEnergies | 9,23 |
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
