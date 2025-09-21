from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def genereer_pdf(bestandsnaam, resultaat, advies):
    c = canvas.Canvas(bestandsnaam, pagesize=A4)
    c.setFont("Helvetica", 12)
    c.drawString(50, 800, "Vermogensdashboard 2025 — Rapport")
    c.drawString(50, 770, f"Vermogen: €{resultaat['vermogen']}")
    c.drawString(50, 750, f"Belastbaar: €{resultaat['belastbaar']}")
    c.drawString(50, 730, f"Belasting: €{resultaat['belasting']}")
    c.drawString(50, 700, f"Advies: {advies}")
    c.drawImage("scorekaart_dirk.png", 50, 500, width=200, height=200)
    c.save()

