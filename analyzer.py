import re
import os
import pytesseract

# Set correct tesseract path based on environment
if os.getenv('RUNNING_IN_DOCKER') == '1':
    # Inside Docker — tesseract is available system-wide
    pass
else:
    # Local MacBook — set Homebrew path manually
    pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
def analyze_url(url):
    pass
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

    if not reasons:
        reasons.append("No suspicious elements detected in URL")
        risk_level = "Low"
    else:
        if len(reasons) >= 3:
            risk_level = "High"
        elif len(reasons) >= 2:
            risk_level = "Medium"
        else:
            risk_level = "Low"
    
    return risk_level, reasons

def analyze_header_text(header_text):
    pass
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    spf_fail_pattern = r"spf=fail"
    dmarc_fail_pattern = r"dmarc=fail"

    ips = re.findall(ip_pattern, header_text.lower())
    spf_dmarc_failures = []

    if re.search(spf_fail_pattern, header_text.lower()):
        spf_dmarc_failures.append("SPF failure detected")
    else:
        spf_dmarc_failures.append("SPF: None")

    if re.search(dmarc_fail_pattern, header_text.lower()):
        spf_dmarc_failures.append("DMARC failure detected")
    else:
        spf_dmarc_failures.append("DMARC: None")

    if not ips and not any("failure" in failure.lower() for failure in spf_dmarc_failures):
        spf_dmarc_failures.append("No suspicious elements detected in email headers")

    return {
        'ips': ips,
        'spf_dmarc_failures': spf_dmarc_failures
    }
