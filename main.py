import argparse
from dotenv import load_dotenv

from utils.extract import extract_domain, normalize_url
from utils.vt import vt_penalty
from utils.score import combine_scores, classify
from utils.logger import log_result

DEFAULT_LOG = "link_results.csv"

def analyze_url(url: str, vt_enabled: bool = True) -> tuple[str, int, dict]:
    url = normalize_url(url)
    domain = extract_domain(url)
    vt_points, vt_details = vt_penalty(domain) if vt_enabled else (0, {"enabled": False})
    total, breakdown = combine_scores(url, vt_points)
    status = classify(total)
    details = {**breakdown, "domain": domain, "vt": vt_details}
    return status, total, details

def run_cli():
    load_dotenv()  # load VT_API_KEY if present

    ap = argparse.ArgumentParser(description="Suspicious Link Early Warning System")
    ap.add_argument("--url", help="URL to analyze")
    ap.add_argument("--file", help="File with one URL per line")
    ap.add_argument("--no-vt", action="store_true", help="Disable VirusTotal lookup")
    ap.add_argument("--logfile", default=DEFAULT_LOG, help=f"CSV log file (default: {DEFAULT_LOG})")
    ap.add_argument("--quiet", action="store_true", help="Only print final status + score")
    args = ap.parse_args()

    vt_enabled = not args.no_vt

    if not args.url and not args.file:
        ap.error("Provide --url or --file")

    urls = []
    if args.url:
        urls.append(args.url)
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            urls.extend([line.strip() for line in f if line.strip()])

    for u in urls:
        status, score, details = analyze_url(u, vt_enabled=vt_enabled)
        domain = details.get("domain", "")
        if args.quiet:
            print(f"{status} ({score}) - {u}")
        else:
            print(f"[{('ALERT' if status=='Dangerous' else 'OK')}] Status: {status} | Score: {score}")
            print(f"Domain: {domain}")
            p = details.get("patterns", {})
            k = details.get("keywords", {})
            vt = details.get("vt", {})
            vt_points = vt.get("penalty", vt.get("points", 0))

            # New display
            vt_status = "N/A" if not vt.get("enabled") else f"Malicious: {vt.get('malicious',0)}, Suspicious: {vt.get('suspicious',0)}"
            print(f"Details: patterns={p.get('points',0)}, keywords={k.get('points',0)}, VT points={vt_points} ({vt_status})")
            print(f"Breakdown: patterns={p}, keywords={k}, vt={vt}")
            print(f"Log: {args.logfile} (appended)")
        log_result(args.logfile, u, domain, score, status, details)

if __name__ == '__main__':
    run_cli()
