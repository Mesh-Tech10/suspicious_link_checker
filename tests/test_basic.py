from utils.extract import extract_domain, normalize_url
from utils.patterns import pattern_score
from utils.keywords import keyword_score
from utils.score import combine_scores, classify

def test_extract_domain():
    assert extract_domain("https://sub.example.co.uk/path") == "example.co.uk"
    assert extract_domain("http://localhost") == "localhost"

def test_normalize_url():
    assert normalize_url("example.com").startswith("http://")
    assert normalize_url("https://example.com").startswith("https://")

def test_pattern_score():
    s, det = pattern_score("http://a---b---c.example.xyz/path1234")
    assert s >= 20  # hyphens
    assert det["hyphens"] >= 0

def test_keyword_score():
    s, det = keyword_score("http://example.com/login/reset")
    assert s > 0
    assert "login" in det["kw_hits"]

def test_combine_and_classify():
    total, br = combine_scores("http://example.com/login", vt_penalty=0)
    assert total >= 15
    status = classify(total)
    assert status in {"Safe", "Suspicious", "Dangerous"}
