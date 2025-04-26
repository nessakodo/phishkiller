# 𝘗𝘩𝘪𝘴𝘩𝘒𝘪𝘭𝘭𝘦𝘳

![Version](https://img.shields.io/badge/Version-v1-000000?style=for-the-badge&logo=github&logoColor=white)

[![Python](https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-000000?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![MIT License](https://img.shields.io/badge/License-MIT-000000?style=for-the-badge)](LICENSE)
[![Made by Nessa Kodo](https://img.shields.io/badge/Made%20by-Nessa%20Kodo-000000?style=for-the-badge)](https://nessakodo.com)

---

## 𝘛𝘦𝘳𝘮𝘪𝘯𝘢𝘭-𝘪𝘯𝘴𝘱𝘪𝘳𝘦𝘥 𝘗𝘩𝘪𝘴𝘩𝘪𝘯𝘨 𝘈𝘯𝘢𝘭𝘺𝘻𝘦𝘳 𝘸𝘪𝘵𝘩 𝘙𝘦𝘢𝘭-𝘛𝘪𝘮𝘦 𝘚𝘤𝘰𝘳𝘪𝘯𝘨

> **Live Demo**: [phishkiller.streamlit.app](https://phishkiller.streamlit.app)

PhishKiller is a phishing threat detection tool designed to analyze suspicious URLs and raw email headers. It uses heuristic analysis, pattern matching, and blacklists to flag potential phishing attempts with detailed scoring.

---

## 𝘍𝘦𝘢𝘵𝘶𝘳𝘦𝘴

- URL analysis with heuristic scoring
- Email header parsing (SPF/DMARC detection)
- Retro terminal-themed Streamlit UI
- Report download (JSON and plain text formats)
- Mobile responsive and cloud-deployable

---

## 𝘘𝘶𝘪𝘤𝘬 𝘚𝘵𝘢𝘳𝘵

**Requirements:**

- Python 3.8+
- Streamlit
- Requests

Install dependencies:

```bash
pip install -r requirements.txt
```

Run locally:

```bash
streamlit run app.py
```

---

## 𝘋𝘦𝘱𝘭𝘰𝘺 𝘗𝘦𝘳𝘮𝘢𝘯𝘦𝘯𝘵𝘭𝘺

PhishKiller can be permanently deployed on platforms like:

- [Streamlit Community Cloud (free hosting)](https://streamlit.io/cloud)
- [Railway](https://railway.app/)
- [Render](https://render.com/)
- [Fly.io](https://fly.io/)

For deployment, create a `requirements.txt` and (optionally) a `Procfile`:

Example `Procfile` (if needed):

```
web: streamlit run app.py
```

---

## 𝘚𝘢𝘮𝘱𝘭𝘦 𝘌𝘮𝘢𝘪𝘭 𝘏𝘦𝘢𝘥𝘦𝘳

Sample `.txt` files are available under `/test_samples`.

Example:

```text
Received: from suspicioushost.net (unknown [185.245.86.10])
Received-SPF: fail (example.com: domain of attacker@evilsite.ru does not designate 185.245.86.10 as permitted sender)
Authentication-Results: dmarc=fail (p=REJECT) header.from=evilsite.ru
```

---

## 𝘛𝘦𝘴𝘵 𝘊𝘢𝘴𝘦𝘴

Use these examples to simulate detection capabilities:

| Suspicious URL                             | Detection Reason                                  |
|:-------------------------------------------|:--------------------------------------------------|
| `http://secure-login.mybank.co.uk`         | Banking domain spoof with 'secure-login' keyword  |
| `http://verify-user.info/login`            | Common social engineering bait                   |
| `http://paypal.com.userverify.ru`          | PayPal brand spoof + Russian domain (.ru)         |
| `http://update-billing-946238.com`         | Numeric pattern + 'billing' keyword               |
| `http://apple.support-reset.live`          | Fake Apple support domain                        |
| `http://198.167.0.245/login?user=me`       | Bare IP address exploitation                     |
| `http://ebay.account.confirm-id908.com`    | Subdomain overload spoof                         |

**Detection criteria include:**
- Keyword heuristics (`login`, `verify`, `reset`, etc.)
- Brand spoof detection (`paypal`, `apple`, etc.)
- Subdomain complexity analysis
- Numeric slug patterns
- OpenPhish blacklist matching (optional integration)

---

## 𝘐𝘯𝘵𝘦𝘳𝘧𝘢𝘤𝘦 𝘗𝘳𝘦𝘷𝘪𝘦𝘸𝘴

### URL Analysis

Displays URL threat levels, detected phishing patterns, and reasons for flagging.

![URL analysis results with threat level and reasoning](/assets/screenshots/url.png)


---

### Email Header Analysis

Parses uploaded email headers, extracts originating IP addresses, and detects SPF/DMARC authentication failures.

![Email header analysis with SPF failure output](/assets/screenshots/email.png)

---

## 𝘗𝘭𝘢𝘯𝘯𝘦𝘥 𝘌𝘯𝘩𝘢𝘯𝘤𝘦𝘮𝘦𝘯𝘵𝘴

- Webhook alerting to Discord channels
- Signature-based matching with YAML configs
- Integration with live threat intelligence feeds
- Command-line interface (CLI) mode
- Public phishing incident database with REST API

---

## 𝘊𝘳𝘦𝘥𝘪𝘵𝘴

Created and maintained by [Nessa Kodo](https://nessakodo.com)  
Licensed under the MIT License.

---

# 

---

### 𝘚𝘵𝘢𝘺 𝘢𝘭𝘦𝘳𝘵. 𝘚𝘵𝘢𝘺 𝘴𝘦𝘤𝘶𝘳𝘦.