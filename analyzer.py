# analyzer.py - Core phishing detection logic with scoring and signature heuristics

import re
import requests
from urllib.parse import urlparse

# --- Signature Rules ---
signatures = {
    "url_keywords": ["secure", "login", "verify", "update", "account", "reset", "support"],
    "spoofed_brands": ["apple", "paypal", "google", "bank", "chase"],
    "ip_blocks": ["185.", "194.", "46.23."],
    "spf_dmarc_failures": True
}

# --- OpenPhish Feed ---
FREE_BLACKLIST = "https://openphish.com/feed.txt"

# Checks if a URL is found in the OpenPhish blacklist
def is_blacklisted(url):
    try:
        response = requests.get(FREE_BLACKLIST, timeout=10)
        if response.status_code == 200:
            blacklist = response.text.splitlines()
            return any(url.startswith(bad) for bad in blacklist)
    except Exception:
        return False
    return False

# Heuristic scoring function that returns a threat score and reasoning
def score_suspicious_url(url):
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    full_url = url.lower()

    score = 0
    reasons = []

    # Subdomain overload
    if len(domain.split('.')) > 3:
        score += 1
        reasons.append("Too many subdomains")

    # Encoded characters or suspicious symbols
    if any(char in url for char in ['@', '%', '&', '$']):
        score += 1
        reasons.append("Contains encoded or obfuscation characters")

    # Long number strings (e.g., account reset links)
    if re.search(r'\d{6,}', url):
        score += 1
        reasons.append("Contains long numeric pattern")

    # Keyword matches (e.g., login, reset, update)
    for keyword in signatures["url_keywords"]:
        if keyword in full_url:
            score += 1
            reasons.append(f"Keyword match: '{keyword}'")
            break

    # Spoofed brand names in the domain
    for brand in signatures["spoofed_brands"]:
        if brand in domain:
            score += 1
            reasons.append(f"Brand spoofing detected: '{brand}'")
            break

    return score, reasons

# Email header analysis
def analyze_email_header(header_text):
    lines = header_text.split('\n')
    received_lines = [l for l in lines if l.lower().startswith("received")]
    ip_matches = re.findall(r'[0-9]+(?:\.[0-9]+){3}', '\n'.join(received_lines))

    spf_fails = [l for l in lines if "spf=fail" in l.lower() or "dmarc=fail" in l.lower()]

    return {
        "ips": list(set(ip_matches)),
        "spf_dmarc_failures": spf_fails
    }

# URL analyzer: combines blacklist + signature score
def analyze_url(url):
    if is_blacklisted(url):
        return "Malicious", ["URL found in phishing blacklist"]

    score, reasons = score_suspicious_url(url)
    if score >= 3:
        return "Malicious", reasons
    elif score >= 1:
        return "Suspicious", reasons
    else:
        return "Safe", reasons

# Header dispatcher
def analyze_header_text(text):
    return analyze_email_header(text)
