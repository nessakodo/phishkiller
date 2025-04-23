# PhishKiller

**PhishKiller** is a phishing threat analyzer built with Python and Streamlit. It helps detect phishing attempts by analyzing suspicious URLs and email headers.

## Features

- URL analysis with phishing heuristics and blacklist checking
- Email header parsing for SPF/DMARC failure detection
- Streamlit web interface for clean and interactive analysis
- Downloadable reports in JSON and TXT formats

## Requirements

- Python 3.8+
- Streamlit
- Requests

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Start the app locally:

```bash
streamlit run app.py
```

Once running:

1. Paste a suspicious URL into the form
2. Upload a `.txt` email header file
3. View real-time analysis results
4. Download the report for your records

## Sample Header

*You can find the example .txt files used below in the `/test_samples` folder*
```txt
Received: from suspicioushost.net (unknown [185.245.86.10])
Received-SPF: fail (example.com: domain of attacker@evilsite.ru does not designate 185.245.86.10 as permitted sender)
Authentication-Results: dmarc=fail (p=REJECT) header.from=evilsite.ru
```

## Test Cases

*Use the examples below in PhishKiller's URL input to test its detection capabilities. These URLs mimic known phishing patterns or contain synthetic traits used in real-world attacks.*

> **Warning**: These URLs are for testing only. Do **not** click or visit them.

| Suspicious URL                             | Why It’s Suspicious                              |
|--------------------------------------------|--------------------------------------------------|
| `http://secure-login.mybank.co.uk`         | Uses `secure-login` with a banking domain        |
| `http://verify-user.info/login`            | Common social engineering bait                   |
| `http://paypal.com.userverify.ru`          | Spoofs PayPal, hosted in `.ru`                   |
| `http://update-billing-946238.com`         | Contains numeric slug with 'billing' keyword     |
| `http://apple.support-reset.live`          | Mimics Apple support with reset action           |
| `http://198.167.0.245/login?user=me`       | Bare IP address with login query                 |
| `http://ebay.account.confirm-id908.com`    | Subdomain overload + spoofed brand               |

### What These URLs Trigger

- Heuristic pattern matching (e.g., `login`, `verify`, `reset`)
- Subdomain count detection
- Numeric slug identification
- Brand impersonation checks
- Optional OpenPhish blacklist validation (if connected)

---

### Interface Previews

#### URL Input & Risk Detection

> Example showing detection of phishing-like patterns and spoofed branding in a submitted URL.

![URL analysis results with threat level and reasoning](/assets/screenshots/url.png)

---

#### Email Header Analyzer

> Example of parsed email headers, extracted IPs, and SPF/DMARC failure detection.

![Email header analysis with SPF failure output](/assets/screenshots/email.png)

---

### Report Exporting

> Users can download full analysis reports as JSON or plain text for sharing or documentation.

#### JSON Example Report Output
![JSON-formatted threat data](/assets/screenshots/json.png)

## Credits

*Built with love by Nessa Kodo for cybersecurity education and operational defense learning.*

---
