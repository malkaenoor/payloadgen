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
python3 cli.py generate --type xss --id 7
python3 cli.py generate --type sqli --id 11

# Generate by category (XSS or SQLi)
python3 cli.py generate --type xss --category reflected
python3 cli.py generate --type sqli --category union

# Encode payloads
python3 cli.py encode --method base64 --payload "<script>alert(1)</script>"
python3 cli.py encode --method url --payload "' OR 1=1 --"

# Mutate payloads (case flip, reverse, unicode, random-insert)
python3 cli.py mutate run --method case-flip --payload "<script>alert(1)</script>"
python3 cli.py mutate-sqli --type sqli --method comment --payload "' OR 1=1 --"


 # pull and run DVWA container (isolated lab)
docker pull vulnerables/web-dvwa

docker run -d \
  --name dvwa \
  -p 8080:80 \
  vulnerables/web-dvwa


# open DVWA in browser: http://localhost:8080
# login (default DVWA credential or setup per image instructions)
start testing ............

# EXPORT COMMANDS
python3 cli.py export --type sqli --export txt --out sqli_payloads.txt
python3 cli.py export --type xss --export json --out xss_payloads.json

#PDF REPORT
python3 generate_report.py


🔁 Mutate Payload
python3 cli.py mutate run --method reverse --payload "<script>alert(1)</script>"

🔏 Encode Payload
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
