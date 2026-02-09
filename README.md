# PayloadGen – Offensive Security Payload Toolkit

**PayloadGen** is a modular payload generation toolkit for **XSS** and **SQLi**, designed for educational, lab, and penetration testing purposes.  
It supports **numeric payload generation**, **mutation**, **encoding**, and **export** features, along with **report generation** for lab documentation.

---

## 🔹 Features

- Generate **XSS & SQLi payloads** numerically (1–20)
- **List all payloads** for easy reference
- **Mutate payloads** (XSS & SQLi)
- **Encode payloads** (URL, Base64, HTML, HEX, Reverse, Wrap)
- **Export payloads** to TXT or JSON
- **Generate PDF reports**
- **DVWA Docker lab integration** for safe testing

---

## 📦 Installation

Clone the repository:
git clone git@github.com:malkaenoor/payloadgen.git
cd payloadgen

```bash
Create a Python virtual environment:
cd payloadgen/src
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

🐳 DVWA Lab Setup (Optional)
Pull and run DVWA using Docker:

docker pull vulnerables/web-dvwa
docker run -d --name dvwa -p 8080:80 vulnerables/web-dvwa
Open in browser: http://localhost:8080
Default credentials: admin / password
Click Create / Reset Database before testing.
.

🔹 CLI Usage
1️⃣ List available payloads
# XSS payloads
python3 cli.py list --type xss

# SQLi payloads
python3 cli.py list --type sqli
2️⃣ Generate a payload
# Generate XSS payload by ID (1–20)
python3 cli.py generate --type xss --id 1

# Generate SQLi payload by ID (1–20)
python3 cli.py generate --type sqli --id 5
3️⃣ Mutate payloads
# XSS mutation
python3 cli.py mutate run --method case-flip --payload "<script>alert(1)</script>"
# SQLi mutation
python3 cli.py mutate-sqli --type sqli --method comment --payload "' OR 1=1 --"
Available SQLi mutation methods:

case-flip

comment

keyword-split

null

random
4️⃣ Encode payloads
python3 cli.py encode --method url --payload "' OR 1=1 --"
python3 cli.py encode --method base64 --payload "<script>alert(1)</script>"


Supported methods: base64, url, html, hex, reverse, wrap
5️⃣ Export payloads
# Export SQLi payloads to TXT
python3 cli.py export --type sqli --export txt --out sqli_payloads.txt

# Export XSS payloads to JSON
python3 cli.py export --type xss --export json --out xss_payloads.json
6️⃣ Generate PDF report
python3 generate_report.py --out project_report.pdf

