"""Trier et filtrer une liste d'actions selon un critère."""

CRITERES = {
    "variation": "Variation du jour (%)",
    "capitalisation": "Capitalisation (Md€)",
    "per": "PER",
    "rendement": "Rendement du dividende (%)",
}


def _verifier(critere):
    if critere not in CRITERES:
        raise ValueError(f"Critère inconnu : {critere}. Choix possibles : {', '.join(CRITERES)}")


def trier(actions, critere, decroissant=True):
    """Renvoie une nouvelle liste triée. Les valeurs absentes (None) restent toujours à la fin."""
    _verifier(critere)
    connues = [a for a in actions if a.get(critere) is not None]
    absentes = [a for a in actions if a.get(critere) is None]
    return sorted(connues, key=lambda a: a[critere], reverse=decroissant) + absentes


def filtrer(actions, critere, minimum=None, maximum=None):
    """Garde les actions dont le critère est entre minimum et maximum (bornes incluses)."""
    _verifier(critere)
    garder = []
    for a in actions:
        v = a.get(critere)
        if v is None:
            continue
        if minimum is not None and v < minimum:
            continue
        if maximum is not None and v > maximum:
            continue
        garder.append(a)
    return garder
