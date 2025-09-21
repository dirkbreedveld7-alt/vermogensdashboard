import streamlit as st
from box3 import bereken_box3, genereer_matrix, genereer_profieladvies
from pdf_export import genereer_pdf
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(page_title="Vermogensdashboard", page_icon="💼", layout="centered")

st.title("💼 Vermogensdashboard 2025")

# Invoer
spaargeld = st.number_input("Spaargeld (€)", min_value=0.0, value=50000.0, step=1000.0)
beleggingen = st.number_input("Beleggingen (€)", min_value=0.0, value=100000.0, step=1000.0)
schulden = st.number_input("Schulden (€)", min_value=0.0, value=0.0, step=1000.0)
vrijstelling = st.number_input("Vrijstelling (€)", min_value=0.0, value=57000.0, step=500.0)
risicoprofiel = st.radio("Risicoprofiel", ["Defensief", "Neutraal", "Offensief"])

# Berekening
resultaat = bereken_box3(spaargeld, beleggingen, schulden, vrijstelling)
fig_matrix = genereer_matrix()
profieladvies = genereer_profieladvies(risicoprofiel)

# Visualisatie
st.subheader("📊 Risico-rendement matrix")
st.plotly_chart(fig_matrix, use_container_width=True)

st.subheader("🧠 Advies")
st.success(profieladvies)

# Scorekaart
st.subheader("⭐ Scorekaart")
st.image("scorekaart_dirk.png", caption="Persoonlijke scorekaart")

# PDF-export
if st.button("📄 Genereer PDF-rapport"):
    genereer_pdf("dashboard_rapport.pdf", resultaat, profieladvies)
    with open("dashboard_rapport.pdf", "rb") as f:
        st.download_button("Download rapport", f.read(), file_name="dashboard_rapport.pdf")

