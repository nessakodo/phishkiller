# analyzer.py - Core phishing threat detection logic for PhishKiller
# Written by Nessa Kodo
import re
import requests
from urllib.parse import urlparse

# Signature-based rule set to enrich threat matching
signatures = {
    "url_keywords": ["secure", "login", "verify", "update", "account", "reset"],
    "ip_blocks": ["185.", "194.", "46.23."],  # Known bad IP prefixes
    "spf_dmarc_failures": True  # Trigger alert if SPF or DMARC fails
}

# Free open-source phishing blacklist feed from OpenPhish
FREE_BLACKLIST = "https://openphish.com/feed.txt"

# -- Blacklist Check --
# Verifies whether a given URL appears on the known phishing blacklist.
def is_blacklisted(url):
    try:
        response = requests.get(FREE_BLACKLIST, timeout=10)
        if response.status_code == 200:
            blacklist = response.text.splitlines()
            return any(url.startswith(bad) for bad in blacklist)
    except Exception as e:
        # In production, log the error (e.g., to Sentry or Streamlit's error log)
        return False
    return False

# -- URL Suspicion Heuristics --
# Looks for red flags in a URL’s structure or patterns
def is_suspicious_url(url):
    parsed = urlparse(url)
    domain = parsed.netloc

    suspicious_signals = [
        len(domain.split('.')) > 3,  # Too many subdomains (e.g., phishing.fake.example.com)
        any(char in url for char in ['@', '%', '&', '$']),  # Encoded characters often used to mask links
        re.search(r'\d{6,}', url),  # Long strings of numbers
        re.search(r'(login|verify|secure|account)', url, re.IGNORECASE)  # Social engineering keywords
    ]
    return any(suspicious_signals)

# -- Email Header Analysis --
# Extracts metadata from email headers including IPs and failed authentication attempts
def analyze_email_header(header_text):
    lines = header_text.split('\n')
    received_lines = [l for l in lines if l.lower().startswith("received")]
    
    # Collect all IP addresses in 'Received' lines
    ip_matches = re.findall(r'[0-9]+(?:\.[0-9]+){3}', '\n'.join(received_lines))

    # Detect SPF and DMARC failures
    spf_fails = [l for l in lines if "spf=fail" in l.lower() or "dmarc=fail" in l.lower()]
    
    return {
        "ips": list(set(ip_matches)),
        "spf_dmarc_failures": spf_fails
    }

# -- Main URL Dispatcher --
def analyze_url(url):
    if is_blacklisted(url):
        return "Malicious: Found in phishing blacklist"
    elif is_suspicious_url(url):
        return "Suspicious: Unusual structure or keywords detected"
    else:
        return "Likely Safe: No immediate red flags"

# -- Dispatcher for email header text input --
def analyze_header_text(text):
    return analyze_email_header(text)
