PHISH_KWS = {
    "login", "verify", "account", "update", "urgent",
    "bank", "password", "invoice", "reset", "unlock",
    "security", "confirm", "limited", "expire", "cancel"
}

def keyword_score(url: str, cap: int = 45) -> tuple[int, dict]:
    """
    Adds +15 per keyword hit, capped by `cap`.
    Returns (score, {kw_hits:list, points:int})
    """
    u = url.lower()
    hits = [kw for kw in PHISH_KWS if kw in u]
    points = min(15 * len(hits), cap)
    return points, {"kw_hits": hits, "points": points}
