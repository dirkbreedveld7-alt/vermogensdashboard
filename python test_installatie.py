def test_dependencies():
    try:
        import streamlit
        import reportlab
        import plotly
        from PIL import Image
        print("✅ Alle dependencies zijn correct geïnstalleerd.")
    except ImportError as e:
        print("❌ Ontbrekende dependency:", e.name)

def test_bestanden():
    import os
    bestanden = [
        "app.py", "box3.py", "pdf_export.py", "requirements.txt",
        "scorekaart_dirk.png", "logo.png",
        "static/favicon.png", "static/icon-192.png", "static/icon-512.png", "static/manifest.json"
    ]
    ontbrekend = [f for f in bestanden if not os.path.exists(f)]
    if ontbrekend:
        print("❌ Ontbrekende bestanden:", ontbrekend)
    else:
        print("✅ Alle benodigde bestanden zijn aanwezig.")

if __name__ == "__main__":
    print("🔍 Testen van installatie en projectstructuur...\n")
    test_dependencies()
    test_bestanden()

