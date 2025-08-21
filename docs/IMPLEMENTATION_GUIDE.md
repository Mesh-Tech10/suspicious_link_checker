# Suspicious Link Early Warning System — Detailed Implementation Guide

This guide walks you from **zero to shipped**. You’ll set up a Python project,
implement the URL analyzer, add threat-intel integration, build a simple GUI,
write tests, and publish a portfolio-ready repository.

---

## 0) Prerequisites
- Python 3.9+ installed
- Git installed
- A free VirusTotal API key (optional but recommended)
- (Windows) PowerShell or CMD; (macOS/Linux) Terminal

---

## 1) Project Setup
```bash
git init suspicious-link-checker && cd suspicious-link-checker
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Copy the scaffolded files from the download into this folder, then:
pip install -r requirements.txt
```

**Environment variables**
- Copy `.env.example` to `.env`
- Put your VirusTotal key in `VT_API_KEY`

---

## 2) Architecture Overview
**Flow:**
1. Normalize URL
2. Extract domain
3. Pattern checks (hyphens, long digits, URL length, suspicious TLDs)
4. Keyword heuristics (login, verify, account, etc.)
5. VirusTotal domain reputation (optional)
6. Combine scores → classify (Safe/Suspicious/Dangerous)
7. Log to CSV

**Key modules**
- `utils/extract.py` → `extract_domain`, `normalize_url`
- `utils/patterns.py` → `pattern_score`
- `utils/keywords.py` → `keyword_score`
- `utils/vt.py` → `vt_penalty`
- `utils/score.py` → `combine_scores`, `classify`
- `utils/logger.py` → `log_result`
- `main.py` → CLI entrypoint
- `gui.py` → Tkinter UI

---

## 3) Implement Core Functions
These are already scaffolded for you in `/utils`. Read each file and skim the docstrings.

### a) URL normalization & domain extraction
- Ensure URLs have a scheme (http/https)
- Extract the registrable domain using `tldextract` (fallback to `urlparse`)

### b) Pattern checks
- Many hyphens → +20
- Long digit sequence (4+) → +10
- URL length > 75 → +10
- Suspicious TLD → +10
- Returns both **score** and **details**

### c) Keyword heuristics
- Keyword list in `utils/keywords.py`
- +15 per hit, capped at +45 by default
- Returns score and which keywords matched

### d) VirusTotal (optional)
- Reads `VT_API_KEY` from environment
- Calls `/domains/{domain}` endpoint
- If `malicious > 0` → +50 penalty

---

## 4) Scoring & Classification
- `combine_scores(url, vt_penalty)` merges all points and returns a breakdown
- `classify(score)`:
    - 0–29 → Safe
    - 30–59 → Suspicious
    - 60+ → Dangerous

You can tweak thresholds and weights to suit your risk appetite.

---

## 5) CLI Usage (main.py)
**Run a single URL**
```bash
python main.py --url "https://secure-login-example.com/path"
```

**Run a batch from file**
```bash
python main.py --file samples/example_urls.txt
```

**Disable VirusTotal lookups**
```bash
python main.py --url "http://example.com" --no-vt
```

**Quiet mode**
```bash
python main.py --url "http://example.com" --quiet
```

Output includes the total score, classification, and a breakdown of pattern/keyword/VT contributions.
Results are appended to `link_results.csv` (customizable with `--logfile`).

---

## 6) GUI (optional)
```bash
python gui.py
```
- Enter a URL, click **Check Link**.
- A popup shows Status, Score, and Domain.
- This uses the same `analyze_url` function as the CLI.

---

## 7) Testing
We include a simple pytest suite.
```bash
pip install pytest
pytest -q
```
Tests cover:
- Domain extraction & normalization
- Pattern & keyword scoring
- Score combination and classification

---

## 8) Logging & Data
- CSV logs include timestamp, URL, domain, score, status, and details
- Keep sample logs for your README/screenshots
- Ensure you **do not** upload any sensitive URLs from your workplace or personal inbox

---

## 9) Documentation & Portfolio
- Use your README to explain **why** this helps users (non-technical language)
- Add screenshots:
    - Architecture diagram
    - Mock CLI output
- Include a short demo GIF (10–20 seconds)

**Suggested README sections:**
- Overview (problem + solution)
- Features
- How to run (CLI + GUI)
- Scoring logic
- Threat intel notes
- Roadmap
- License

---

## 10) Packaging & Sharing
**Create a GitHub repo**
```bash
git remote add origin https://github.com/<you>/suspicious-link-checker.git
git add .
git commit -m "Initial release"
git push -u origin main
```

**(Optional) Make a standalone binary (PyInstaller)**
```bash
pip install pyinstaller
pyinstaller --onefile main.py
# Dist binary at dist/main (or main.exe on Windows)
```

**(Optional) Dockerize**
```Dockerfile
# Dockerfile (quick start)
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONUNBUFFERED=1
CMD ["python", "main.py", "--file", "samples/example_urls.txt", "--no-vt"]
```

Build & run:
```bash
docker build -t link-checker .
docker run --rm link-checker
```

---

## 11) Validation Plan (Make It Real)
- **Unit tests** (already included)
- **Manual tests** with a mix of benign & sketchy URLs
- **Edge cases**: localhost, IP literals (http://1.2.3.4), long query strings, data: URIs
- **Performance**: batch 100–1,000 URLs from a file (disable VT to avoid rate limits)

---

## 12) Security & Ethics Notes
- This is a **heuristic early warning** tool, not a definitive verdict
- Never auto-visit unknown URLs on the host system
- Respect API terms; do not share private data publicly
- Document limitations and encourage user caution

---

## 13) Roadmap Ideas
- Browser extension to score hovered links
- Email client add-on
- More threat feeds: URLScan.io, PhishTank, OpenPhish
- Typosquatting detector (Levenshtein distance vs. top brands)
- Streamlit dashboard for visual history

---

## 14) Troubleshooting
- **tldextract fetch errors**: works offline with bundled PSL in newer versions; otherwise it falls back.
- **VT API errors**: run with `--no-vt` or set `VT_API_KEY` in `.env`
- **Unicode errors on Windows**: run `chcp 65001` or use PowerShell

---

## 15) Milestones Checklist
- [ ] Create repo & virtualenv
- [ ] Install requirements
- [ ] Add VT key (optional)
- [ ] Run CLI on sample URLs
- [ ] Run GUI
- [ ] Pass tests
- [ ] Polish README with images & demo GIF
- [ ] Publish & post on LinkedIn
