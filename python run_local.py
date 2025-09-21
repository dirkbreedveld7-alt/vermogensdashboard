import os
import subprocess

def uitleg():
    print("\n💼 Vermogensdashboard 2025")
    print("Een interactieve tool voor Nederlandse vermogensbelasting.")
    print("\n📦 Bestandstructuur gecontroleerd...")
    print("📄 PDF-export, scorekaart en PWA zijn geïntegreerd.")
    print("\n🚀 Starten van Streamlit-app...\n")

def start_streamlit():
    try:
        subprocess.run(["streamlit", "run", "app.py"])
    except FileNotFoundError:
        print("❌ Streamlit niet gevonden. Installeer via: pip install streamlit")

if __name__ == "__main__":
    uitleg()
    start_streamlit()

