from urllib.parse import urlparse
import tldextract

def extract_domain(url: str) -> str:
    """
    Extracts the registrable domain (e.g., 'example.com') from a URL.
    Falls back to urlparse if tldextract fails.
    """
    try:
        e = tldextract.extract(url)
        if e.suffix:
            return f"{e.domain}.{e.suffix}"
        # If no suffix (e.g., localhost), fall back
    except Exception:
        pass
    # Fallback: try urlparse
    netloc = urlparse(url).netloc or url
    # Strip credentials and port if present
    if "@" in netloc:
        netloc = netloc.split("@", 1)[1]
    if ":" in netloc:
        netloc = netloc.split(":", 1)[0]
    # Return last two labels if possible
    parts = [p for p in netloc.split(".") if p]
    if len(parts) >= 2:
        return ".".join(parts[-2:])
    return netloc

def normalize_url(url: str) -> str:
    """
    Ensure the URL has a scheme and trim whitespace.
    """
    url = url.strip()
    if not url.lower().startswith(("http://", "https://")):
        url = "http://" + url
    return url
