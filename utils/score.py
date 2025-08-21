from .patterns import pattern_score
from .keywords import keyword_score

def combine_scores(url: str, vt_penalty: int) -> tuple[int, dict]:
    """
    Combines heuristic scores + VT penalty. Returns (total, breakdown).
    """
    p_score, p_det = pattern_score(url)
    k_score, k_det = keyword_score(url)
    total = p_score + k_score + vt_penalty
    breakdown = {
        "patterns": {**p_det, "points": p_score},
        "keywords": k_det,
        "virustotal": {"points": vt_penalty},
        "total": total,
    }
    return total, breakdown

def classify(score: int) -> str:
    if score >= 60:
        return "Dangerous"
    if score >= 30:
        return "Suspicious"
    return "Safe"
