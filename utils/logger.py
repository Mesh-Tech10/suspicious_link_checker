import csv
from datetime import datetime
from pathlib import Path

def log_result(path: str, url: str, domain: str, score: int, status: str, details: dict) -> None:
    """
    Appends a record to CSV, creating header if needed.
    """
    p = Path(path)
    header = ["timestamp", "url", "domain", "score", "status", "details"]
    exists = p.exists()
    with p.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if not exists:
            w.writerow(header)
        w.writerow([datetime.now().isoformat(timespec="seconds"), url, domain, score, status, str(details)])
