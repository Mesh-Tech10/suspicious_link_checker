import os
import requests

def vt_penalty(domain: str) -> tuple[int, dict]:
    """
    Queries VirusTotal domain endpoint. Returns (penalty, details).
    Penalty is +50 if malicious_count > 0, else 0.
    """
    api_key = os.getenv("VT_API_KEY")
    if not api_key:
        return 0, {"enabled": False, "reason": "No VT_API_KEY set"}
    try:
        r = requests.get(
            f"https://www.virustotal.com/api/v3/domains/{domain}",
            headers={"x-apikey": api_key},
            timeout=10,
        )
        if r.status_code != 200:
            return 0, {"enabled": True, "http_status": r.status_code}
        data = r.json()
        stats = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
        malicious = int(stats.get("malicious", 0))
        suspicious = int(stats.get("suspicious", 0))
        penalty = 50 if malicious > 0 else 0
        return penalty, {
            "enabled": True,
            "malicious": malicious,
            "suspicious": suspicious,
            "penalty": penalty,
        }
    except Exception as e:
        return 0, {"enabled": True, "error": str(e)}
