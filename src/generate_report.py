from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_report(outfile):
    c = canvas.Canvas(outfile, pagesize=A4)
    text = c.beginText(40, 800)

    lines = [
        "PayloadGen – Security Testing Report",
        "",
        "✔ XSS Payloads: Numeric based (1–20)",
        "✔ SQLi Payloads: Numeric based (1–20)",
        "✔ Mutation: XSS + SQLi",
        "✔ Encoding: URL, Base64, HTML, HEX",
        "✔ Export: TXT / JSON",
        "",
        "Test Environment:",
        "DVWA (Docker)",
        "http://localhost:8080",
        "",
        "For educational & lab use only."
    ]

    for line in lines:
        text.textLine(line)

    c.drawText(text)
    c.save()

if __name__ == "__main__":
    generate_report("project_report.pdf")
