Alright — let’s break this into **two pieces** for you cleanly:

# 𝘗𝘩𝘪𝘴𝘩𝘒𝘪𝘭𝘭𝘦𝘳

![Version](https://img.shields.io/badge/Version-v1-000000?style=for-the-badge&logo=github&logoColor=white)
[![Live](https://img.shields.io/badge/Live-Streamlit_App-000000?style=for-the-badge&logo=streamlit&logoColor=white)](https://phishkiller.streamlit.app)
[![Python](https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![MIT License](https://img.shields.io/badge/License-MIT-000000?style=for-the-badge)](LICENSE)
[![Made by Nessa Kodo](https://img.shields.io/badge/Made%20by-Nessa%20Kodo-000000?style=for-the-badge)](https://nessakodo.com)

---

## 𝘛𝘦𝘳𝘮𝘪𝘯𝘢𝘭-𝘪𝘯𝘴𝘱𝘪𝘳𝘦𝘥 𝘱𝘩𝘪𝘴𝘩𝘪𝘯𝘨 𝘥𝘦𝘵𝘦𝘤𝘵𝘪𝘰𝘯 𝘢𝘯𝘢𝘭𝘺𝘻𝘦𝘳 𝘸𝘪𝘵𝘩 𝘳𝘦𝘢𝘭-𝘵𝘪𝘮𝘦 𝘴𝘤𝘰𝘳𝘪𝘯𝘨.

> **Live App:** [phishkiller.streamlit.app](https://phishkiller.streamlit.app)

---

## 𝘍𝘦𝘢𝘵𝘶𝘳𝘦𝘴

- Real-time URL analysis with heuristic scoring
- Email header parsing for SPF/DMARC failures
- Retro terminal-themed Streamlit UI
- Report downloads in JSON and plain text formats

---

## 𝘗𝘭𝘢𝘯𝘯𝘦𝘥 𝘌𝘯𝘩𝘢𝘯𝘤𝘦𝘮𝘦𝘯𝘵𝘴

- Real-time Discord webhook alerts
- Signature matching engine with YAML config
- Threat intelligence feeds integration
- CLI version with export mode
- Public threat database and REST API

---

## 𝘘𝘶𝘪𝘤𝘬 𝘚𝘵𝘢𝘳𝘵

**Requirements:**
- Python 3.8+
- `streamlit`, `requests`

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 𝘚𝘢𝘮𝘱𝘭𝘦 𝘌𝘮𝘢𝘪𝘭 𝘏𝘦𝘢𝘥𝘦𝘳

```txt
Received: from suspicioushost.net (unknown [185.245.86.10])
Received-SPF: fail (example.com: domain of attacker@evilsite.ru does not designate 185.245.86.10 as permitted sender)
Authentication-Results: dmarc=fail (p=REJECT) header.from=evilsite.ru
```

Find test samples under `/test_samples`.

---

## 𝘛𝘦𝘴𝘵 𝘊𝘢𝘴𝘦𝘴

| Suspicious URL                             | Why It’s Suspicious                              |
|:-------------------------------------------|:-------------------------------------------------|
| `http://secure-login.mybank.co.uk`         | Banking domain spoof with login subdomain        |
| `http://verify-user.info/login`            | Social engineering bait                         |
| `http://paypal.com.userverify.ru`          | PayPal spoof with `.ru` domain                   |
| `http://update-billing-946238.com`         | Numeric slug with billing keyword               |
| `http://apple.support-reset.live`          | Fake Apple support portal                       |
| `http://198.167.0.245/login?user=me`       | Bare IP address phishing link                   |
| `http://ebay.account.confirm-id908.com`    | Brand spoofing via subdomain overload           |

---

## 𝘋𝘦𝘵𝘦𝘤𝘵𝘪𝘰𝘯 𝘊𝘳𝘪𝘵𝘦𝘳𝘪𝘢

- Heuristic keyword matching (`login`, `verify`, `reset`)
- Brand spoof detection (`paypal`, `apple`)
- Subdomain and URL structure complexity
- Numeric slug pattern detection
- Blacklist fallback (OpenPhish)

---

## 𝘐𝘯𝘵𝘦𝘳𝘧𝘢𝘤𝘦 𝘗𝘳𝘦𝘷𝘪𝘦𝘸𝘴

**URL Input & Header Risk Detection:**

![URL Analysis Results](/assets/screenshots/url.png)

**Email Header Analyzer:**

![SPF Failure Analysis](/assets/screenshots/email.png)

---

## 𝘊𝘳𝘦𝘥𝘪𝘵𝘴

Created and maintained by [Nessa Kodo](https://nessakodo.com).  
MIT License.

---
