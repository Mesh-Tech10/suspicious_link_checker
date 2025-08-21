**Suspicious Link Checker** 
A Python-based cybersecurity tool that analyzes suspicious URLs for potential phishing, typosquatting, and malicious indicators.
It combines pattern detection, keyword-based scoring, and VirusTotal API integration to assess whether a link is Safe, Suspicious, or Malicious.

**Features**
Extracts and normalizes domains from input URLs
Detects suspicious patterns (digits, hyphens, length anomalies, TLD checks)
Scores based on phishing-related keywords (e.g., login, reset, account, secure)
Integrates with VirusTotal API for real-time reputation lookups
Logs results into CSV files for incident response & forensic tracking
Simple CLI interface for scanning links
Extendable for malware hash scanning and SIEM integration

**Technologies Used**
Python 3.11+
requests → API calls to VirusTotal
csv → For structured incident logging
re, urllib.parse → Pattern recognition & URL parsing
VirusTotal API for domain/file reputation

**Installation**
Clone the repo (or unzip folder if downloaded):
git clone https://github.com/yourusername/suspicious-link-checker.git
cd suspicious-link-checker

**Install dependencies:**
pip install -r requirements.txt

**Usage**
Single URL scan:
python suspicious_link_checker.py "http://example-login-reset.com"

**Multiple URLs from a file:**
python suspicious_link_checker.py urls.txt

**Project Structure**
suspicious_link_checker/
│── suspicious_link_checker.py   # Main script
│── config.py                    # API key & settings
│── test.py                      # Test VirusTotal API connection
│── requirements.txt             # Dependencies
│── link_results.csv             # Logs of scans (auto-created)
│── README.md                    # Project documentation

**How It Works**
Extracts and normalizes domain from the given URL.
Checks for suspicious patterns (digits, length, TLDs, hyphens).
Matches keywords commonly used in phishing (e.g., secure-login, reset, account).
Queries VirusTotal API for domain reputation.
Assigns a risk score → Safe / Suspicious / Malicious.
Logs results into CSV for tracking and future analysis.

**Security Concepts Covered**
Networking Basics: DNS, URL parsing, HTTP/HTTPS
Threat Types: Phishing, Typosquatting, Malicious domains
Threat Intelligence: VirusTotal API integration
Indicators of Compromise (IoCs): Suspicious keywords & patterns
Logging & Forensics: CSV-based reporting for SIEM/IR

**Future Improvements**
GUI dashboard for real-time monitoring
Email/Slack alerts on malicious findings
Hash scanning for file-based malware detection
Integration with threat intelligence feeds (MISP, AbuseIPDB)

Author - Meshwa Patel
🐙 GitHub: [your repo link]

👉 This project is part of my Cybersecurity Portfolio, showcasing hands-on knowledge in networking, threat detection, threat intelligence, and incident response.
