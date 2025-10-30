import streamlit as st
from agent_ai import generate_plan

def app():
    st.header("🤖 Genera la tua scheda con AI")

    goal = st.selectbox("Obiettivo", ["Forza", "Massa", "Definizione", "Resistenza"])
    level = st.selectbox("Livello", ["Principiante", "Intermedio", "Avanzato"])
    days = st.slider("Giorni di allenamento", 1, 7, 3)
    equipment = st.multiselect("Attrezzatura disponibile", ["Manubri", "Bilanciere", "Elastici", "Macchine", "Corpo libero"])
    preferences = st.text_area("Preferenze speciali (es. più spalle, niente gambe)")

    if st.button("Genera scheda"):
        user_input = {
            "goal": goal,
            "level": level,
            "days_per_week": days,
            "equipment": equipment,
            "preferences": preferences
        }


        with st.spinner("Generazione scheda in corso..."):
            plan = generate_plan(user_input)
            if plan:
                st.session_state["ai_plan"] = plan
                st.success("Scheda generata ✅")
                st.json(plan)