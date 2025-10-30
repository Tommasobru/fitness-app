import streamlit as st

# Titolo generale
st.set_page_config(page_title="Fitness App", layout="wide")
st.title("🏋️ Fitness App")

# Barra laterale per navigazione
page = st.sidebar.radio("Vai a:", [
    "Genera scheda",
    "Modifica scheda",
    "Dashboard"
])

# Import dinamico delle pagine
if page == "Genera scheda":
    from pages import create_plan as genera
    genera.app()
elif page == "Modifica scheda":
    from pages import visualize_plan as modifica
    modifica.app()

