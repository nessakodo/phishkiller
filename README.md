# 𝘗𝘩𝘪𝘴𝘩𝘒𝘪𝘭𝘭𝘦𝘳

![Version](https://img.shields.io/badge/Version-v2-000000?style=for-the-badge&logo=github&logoColor=white)

[![Python](https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MIT License](https://img.shields.io/badge/License-MIT-000000?style=for-the-badge)](LICENSE)
[![Made by Nessa Kodo](https://img.shields.io/badge/Made%20by-Nessa%20Kodo-000000?style=for-the-badge)](https://nessakodo.com)

---

## 𝘜𝘱𝘥𝘢𝘵𝘦𝘴

PhishKiller v2 represents a major upgrade:

- Rebuilt from **Streamlit** ➔ **Flask Web Server**
- **OCR** (Optical Character Recognition) added to extract email headers from screenshots (`.png`, `.jpg`)
- **Fully modular**, **mobile responsive**, **hacker-themed UI** with polished UX
- **Deployment ready** (Render, Railway, Fly.io)
- **Faster** performance and scalable backend

[![View Demo](https://img.shields.io/badge/View_Phiskiller_Demo-000000?style=for-the-badge&logo=githubpages&logoColor=white)](https://phishkiller.onrender.com)

---

## 𝘍𝘦𝘢𝘵𝘶𝘳𝘦𝘴

- Real-time phishing URL analysis with heuristic scoring
- Email header parsing (text file or screenshot image OCR)
- Retro-modern terminal UI (dark hacker theme)
- Modular card layout (URL & Email separated cleanly)
- Mobile-friendly and cloud-deployable
- Download analysis reports (JSON/TXT) *(Planned)*

---

## 𝘝𝘦𝘳𝘴𝘪𝘰𝘯 𝘊𝘰𝘮𝘱𝘢𝘳𝘪𝘴𝘰𝘯

| Feature | v1 (Streamlit) | v2 (Flask + OCR) |
|:---|:---|:---|
| UI | Streamlit app, full page | Modular Flask web app, centered |
| Header Upload | Only `.txt` files | `.txt`, `.png`, `.jpg` with OCR |
| Deployment | Streamlit Cloud | Render |
| Design | Basic terminal feel | Hacker-modern, responsive |
| Performance | Good for small demos | Faster, scalable |

---

## 𝘘𝘶𝘪𝘤𝘬 𝘚𝘵𝘢𝘳𝘵 (𝘓𝘰𝘤𝘢𝘭 𝘙𝘶𝘯)

**Requirements:**

- Python 3.8+
- Flask
- Requests
- Pillow
- Pytesseract

Install dependencies:

```bash
pip3 install -r requirements.txt
```

Run locally:

```bash
python3 app.py
```

Visit:

```
http://localhost:8000
```

---

## 𝘋𝘦𝘱𝘭𝘰𝘺 𝘖𝘯𝘭𝘪𝘯𝘦

PhishKiller v2 has been directly hosted on:

- [Render](https://render.com/)

You need:

- `requirements.txt`
- `Procfile`
- GitHub Repository

Example `Procfile`:

```
web: gunicorn app:app
```

---

## 𝘚𝘢𝘮𝘱𝘭𝘦 𝘜𝘱𝘭𝘰𝘢𝘥𝘴

### 𝘛𝘦𝘹𝘵

Example `.txt`:

```text
Received: from suspicioushost.net (unknown [185.245.86.10])
Received-SPF: fail (example.com: domain of attacker@evilsite.ru does not designate 185.245.86.10 as permitted sender)
Authentication-Results: dmarc=fail (p=REJECT) header.from=evilsite.ru
```

### 𝘚𝘤𝘳𝘦𝘦𝘯𝘴𝘩𝘰𝘵

Example `.png`:

![Sample Email OCR Screenshot](/assets/screenshots/email_ocr_example.png)

*(Simulated screenshot for OCR extraction, however real email headers will work.)*

---

## 𝘛𝘦𝘴𝘵 𝘊𝘢𝘴𝘦𝘴 (𝘍𝘰𝘳 𝘜𝘙𝘓 𝘈𝘯𝘢𝘭𝘺𝘴𝘪𝘴)

*Do NOT click these, they are for testing purposes only.*

| Suspicious URL                             | Detection Reason                                  |
|:-------------------------------------------|:--------------------------------------------------|
| `http://secure-login.mybank.co.uk`         | Banking domain spoof with 'secure-login' keyword  |
| `http://verify-user.info/login`            | Common social engineering bait                   |
| `http://paypal.com.userverify.ru`          | PayPal brand spoof + Russian domain (.ru)         |
| `http://update-billing-946238.com`         | Numeric pattern + 'billing' keyword               |
| `http://apple.support-reset.live`          | Fake Apple support domain                        |
| `http://198.167.0.245/login?user=me`       | Bare IP address exploitation                     |
| `http://ebay.account.confirm-id908.com`    | Subdomain overload spoof                         |

---

## 𝘐𝘯𝘵𝘦𝘳𝘧𝘢𝘤𝘦 𝘗𝘳𝘦𝘷𝘪𝘦𝘸𝘴

### URL Analysis Card

Displays threat level and reason flags.

![URL Analysis](/assets/screenshots/url_analysis.png)

---

### Email Header (Text or Image)

Parses SPF/DMARC fails from text or OCR scanned images.

![Header Analysis Card](/assets/screenshots/header_analysis.png)

---

## 𝘗𝘭𝘢𝘯𝘯𝘦𝘥 𝘌𝘯𝘩𝘢𝘯𝘤𝘦𝘮𝘦𝘯𝘵𝘴 (V2.5+)

- Report download buttons (JSON, TXT)
- Signature-based detection rules
- Public phishing database API
- CLI version
- Webhook alerts (Discord, Slack)

---

## 𝘚𝘶𝘱𝘱𝘰𝘳𝘵 𝘵𝘩𝘦 𝘉𝘶𝘪𝘭𝘥

[![Buy Me A Coffee](https://img.shields.io/badge/Buy_Me_A_Coffee-000000?style=for-the-badge&logo=buy-me-a-coffee&logoColor=white)](https://www.buymeacoffee.com/nessakodo)

---

## 𝘊𝘳𝘦𝘥𝘪𝘵𝘴


Created and maintained by [Nessa Kodo](https://nessakodo.com)  
Licensed under the MIT License.

### 𝘚𝘵𝘢𝘺 𝘷𝘪𝘨𝘪𝘭𝘢𝘯𝘵. 𝘚𝘵𝘢𝘺 𝘴𝘦𝘤𝘶𝘳𝘦.

---

