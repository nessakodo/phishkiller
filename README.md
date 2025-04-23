# PhishKiller

[![Python](https://img.shields.io/badge/Python-black?style=flat-square&logo=python&logoColor=white)](https://www.python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-black?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![MIT License](https://img.shields.io/badge/License-MIT-black?style=flat-square)](LICENSE)
[![Made by Nessa Kodo](https://img.shields.io/badge/Made%20by-Nessa%20Kodo-black?style=flat-square)](https://nessakodo.com)

**PhishKiller** is a terminal-inspired phishing threat analyzer built with Python and Streamlit. It detects suspicious characteristics in URLs and raw email headers using heuristic rules, scoring logic, and blacklist integration.

> Deployed at: [phishkiller.streamlit.app](https://phishkiller.streamlit.app) *(Demo instance)*

## Features

- Real-time URL analysis with heuristic scoring and blacklist lookup
- Email header parsing for SPF/DMARC failure detection
- Streamlit interface with mobile-friendly retro terminal theme
- Report downloads in JSON and plain text formats

## Planned Enhancements

- Real-time Discord webhook alerts
- Signature matching engine with YAML config
- Enriched threat intelligence feeds integration
- CLI version with terminal export mode
- Public threat database and REST API

---

## Quick Start

**Requirements:**
- Python 3.8+
- `streamlit`, `requests`

```bash
pip install -r requirements.txt
streamlit run app.py
```

1. Paste a suspicious URL into the input box.
2. Upload a raw `.txt` email header.
3. View threat level and detection reasons.
4. Download your analysis report.

---

## Sample Email Header

You can find example `.txt` files under `/test_samples`.

```txt
Received: from suspicioushost.net (unknown [185.245.86.10])
Received-SPF: fail (example.com: domain of attacker@evilsite.ru does not designate 185.245.86.10 as permitted sender)
Authentication-Results: dmarc=fail (p=REJECT) header.from=evilsite.ru
```

---

## Test Cases

*Use the examples below in PhishKiller to simulate detection capabilities.*

| Suspicious URL                             | Why It’s Suspicious                              |
|--------------------------------------------|--------------------------------------------------|
| `http://secure-login.mybank.co.uk`         | Uses `secure-login` with a banking domain        |
| `http://verify-user.info/login`            | Common social engineering bait                   |
| `http://paypal.com.userverify.ru`          | Spoofs PayPal, hosted in `.ru`                   |
| `http://update-billing-946238.com`         | Contains numeric slug with 'billing' keyword     |
| `http://apple.support-reset.live`          | Mimics Apple support with reset action           |
| `http://198.167.0.245/login?user=me`       | Bare IP address with login query                 |
| `http://ebay.account.confirm-id908.com`    | Subdomain overload + spoofed brand               |

### Detection Criteria:
- Keyword heuristics (`login`, `reset`, `verify`, etc.)
- Spoofed brand detection (`paypal`, `apple`, etc.)
- Subdomain complexity / URL structure
- Numeric pattern detection
- OpenPhish blacklist fallback (if available)

---

## Interface Previews

### URL Input & Risk Detection
> Shows real-time analysis output and why the site is flagged.
![URL analysis results with threat level and reasoning](/assets/screenshots/url.png)

### Email Header Analyzer
> Parses raw email headers, extracts IPs, flags SPF/DMARC issues.
![Email header analysis with SPF failure output](/assets/screenshots/email.png)

### Report Export
> Download results as JSON or plain text.
![JSON-formatted threat data](/assets/screenshots/json.png)

---

## Credits

Created and maintained by [Nessa Kodo](https://nessakodo.com) — for security education and operational defense tooling.

MIT License.