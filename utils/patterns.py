import re

def pattern_score(url: str) -> tuple[int, dict]:
    """
    Heuristic pattern checks. Returns (score, details).
    """
    score = 0
    details = {"hyphens": 0, "digits": 0, "length": 0, "suspicious_tld": 0}

    # Many hyphens are suspicious
    hyphens = url.count("-")
    if hyphens > 2:
        details["hyphens"] = 20
        score += 20

    # Long uninterrupted digit sequences
    if re.search(r"\d{4,}", url):
        details["digits"] = 10
        score += 10

    # Very long URLs
    if len(url) > 75:
        details["length"] = 10
        score += 10

    # Suspicious TLDs list (basic; extend as needed)
    suspicious_tlds = {"zip", "xyz", "top", "country", "click", "work", "link"}
    m = re.search(r"\.([a-zA-Z0-9\-]+)(?:[\/\?:#]|$)", url)
    if m and m.group(1).lower() in suspicious_tlds:
        details["suspicious_tld"] = 10
        score += 10

    return score, details
