# analyzer.py

import re

def analyze_url(url):
    suspicious_keywords = ['login', 'verify', 'reset', 'secure', 'account', 'update', 'billing', 'confirm']
    suspicious_domains = ['paypal', 'apple', 'bank', 'secure', 'signin']
    risk_level = "Low"
    reasons = []

    for keyword in suspicious_keywords:
        if keyword in url.lower():
            reasons.append(f"Keyword '{keyword}' detected")
    
    for domain in suspicious_domains:
        if domain in url.lower():
            reasons.append(f"Possible spoof of '{domain}' detected")
    
    if url.count('.') > 3:
        reasons.append("Excessive subdomain depth")
    
    if any(char.isdigit() for char in url):
        reasons.append("Numeric slug detected")

    if "://" not in url or " " in url:
        reasons.append("Malformed URL structure")

    if reasons:
        risk_level = "High" if len(reasons) >= 3 else "Medium"
    
    return risk_level, reasons

def analyze_header_text(header_text):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    spf_fail_pattern = r"spf=fail"
    dmarc_fail_pattern = r"dmarc=fail"

    ips = re.findall(ip_pattern, header_text.lower())
    spf_dmarc_failures = []

    if re.search(spf_fail_pattern, header_text.lower()):
        spf_dmarc_failures.append("SPF failure detected")

    if re.search(dmarc_fail_pattern, header_text.lower()):
        spf_dmarc_failures.append("DMARC failure detected")

    return {
        'ips': ips,
        'spf_dmarc_failures': spf_dmarc_failures
    }
