import streamlit as st

def app():
    st.header("✏️ Modifica la tua scheda")

    if "ai_plan" not in st.session_state:
        st.warning("Genera prima una scheda dalla pagina precedente.")
        return

    plan = st.session_state["ai_plan"]

    for giorno in plan["giorni"]:
        with st.expander(f"Giorno {giorno['giorno']}"):
            for esercizio in giorno["esercizi"]:
                esercizio["nome"] = st.text_input("Esercizio", esercizio["nome"])
                esercizio["serie"] = st.number_input("Serie", 1, 10, esercizio["serie"])
                esercizio["ripetizioni"] = st.number_input("Ripetizioni", 1, 30, esercizio["ripetizioni"])
                esercizio["note"] = st.text_input("Note", esercizio["note"])

    if st.button("💾 Salva modifiche"):
        st.success("Scheda aggiornata ✅")
