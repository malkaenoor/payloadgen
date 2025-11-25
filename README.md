# Payload Generator Project

A modular and extensible security payload generator designed to produce **XSS**, **SQL Injection**, and **encoded payloads** for testing web applications. The project includes a clean registry-based architecture, independent payload generators, and multiple encoding utilities.

---

## 🚀 Features

* **XSS Payload Generator**
* **SQL Injection Payload Generator**
* **Central Payload Registry**
* **Base64, URL, and HTML Encoders**
* **Easy-to-extend architecture**
* Organized & test‑friendly module structure

---

## 📂 Project Structure

```
payload-generator/
│
├── registry.py
├── generator_xss.py
├── generator_sqli.py
├── encoder.py
├── README.md
└── ... (future modules)
```

---

## 🧩 Modules Overview

### ✅ **registry.py**

Contains a global dictionary with all payload IDs and placeholder values.

### ✅ **generator_xss.py**

Lists available XSS payloads and returns payload by ID.

### ✅ **generator_sqli.py**

Lists SQL Injection payloads and returns payload by ID.

### ✅ **encoder.py**

Encodes payloads using Base64, URL encoding, or HTML escaping.

---
## ⚙️ Installation

```bash
git clone https://github.com/malkaenoor/payloadgen.git
cd payloadgen/src
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

🖥️ CLI Usage
# List available payload IDs
python3 cli.py list --type xss
python3 cli.py list --type sqli

# Generate a single payload by ID (returns placeholder string)
python3 cli.py list --type xss
python3 cli.py list --type sqli
python3 cli.py generate --type xss --id x37
python3 cli.py generate --type sqli --id s48



# Generate by category (XSS or SQLi)
python3 cli.py generate --type xss --category reflected
python3 cli.py generate --type sqli --category union

# Encode payloads
python3 cli.py encode --method base64 --payload "<PLACEHOLDER_PAYLOAD>"
python3 cli.py encode --method url --payload "<PLACEHOLDER_PAYLOAD>"

# Mutate payloads (case flip, reverse, unicode, random-insert)
python3 cli.py mutate run --method case-flip --payload "<PLACEHOLDER_PAYLOAD>"
python3 cli.py mutate run --method reverse --payload "ABC123"

 # pull and run DVWA container (isolated lab)
docker pull vulnerables/web-dvwa
docker run --rm -d --name dvwa -p 8080:80 vulnerables/web-dvwa

# open DVWA in browser: http://localhost:8080
# login (default DVWA credential or setup per image instructions)
# example: get a reflected XSS placeholder
python3 cli.py generate --id XSS_REFLECTED_001
# or a union SQLi placeholder
python3 cli.py generate --id SQLI_UNION_001
# export generated payloads
python3 cli.py generate --type sqli --category union --mode normal --export txt --out union_payloads.txt
# export payloads to JSON/TXT (if implemented)
python3 cli.py generate --type sqli --category union --export json --out union_payloads.json

# generate a simple PDF report (example script uses ReportLab)
python3 generate_report.py --out project_report.pdf


🔁 Mutate Payload
bash
Copy code
python3 cli.py mutate run --method reverse --payload "<script>alert(1)</script>"

🔏 Encode Payload
bash
Copy code
python3 cli.py encode --method base64 --payload "admin"

## 🛠 Usage Example

### List XSS Payloads

```python
from generator_xss import XSSGenerator
xss = XSSGenerator()
print(xss.list_ids())
```

### Generate a SQLi Payload

```python
from generator_sqli import SQLiGenerator
sqli = SQLiGenerator()
payload = sqli.generate_by_id("SQLI_UNION_001")
print(payload)
```

### Encode a Payload

```python
from encoder import Encoder
enc = Encoder()
print(enc.url_encode("A+B C&D"))
```

---

## 🔮 Future Enhancements

* Real payload signatures
* WAF bypass engines (XSS + SQLi)
* Payload fuzzing system
* PDF report generator
* Full menu-based CLI UI

---

## 🤝 Contributing

Pull requests are welcome! Suggestions for new payloads or modules are appreciated.

---

## 📜 License

This project is open-source. You may modify and extend it freely.
