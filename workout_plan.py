import streamlit as st
from  backend.utilis.api_call import get_exercises

exercises = get_exercises()
st.title("🏋️ Crea la tua scheda di allenamento")

plan_name = st.text_input("Nome della scheda")
goal = st.selectbox("Obiettivo", ["Forza", "Massa muscolare", "Resistenza"])
n_day = int(st.number_input("Numero di giorni", min_value=1, max_value=7, value=3))

if plan_name:  # mostri la parte successiva solo dopo aver inserito un nome
    for giorno in range(1, n_day + 1):
        with st.expander(f"Giorno {giorno}"):
            st.subheader(f"Allenamento Giorno {giorno}")
            num_esercizi = int(st.number_input(f"Numero di esercizi per Giorno {giorno}", 1, 10, 3, key=f"ex_{giorno}"))

            esercizi = []
            for i in range(num_esercizi):
                col1, col2, col3, col4 = st.columns([3, 1, 1, 2])
                with col1:
                    esercizio = st.selectbox(f"Esercizio {i+1}", exercises, key=f"ex_name_{giorno}_{i}")
                with col2:
                    serie = st.number_input("Serie", 1, 10, 3, key=f"serie_{giorno}_{i}")
                with col3:
                    ripetizioni = st.number_input("Ripetizioni", 1, 30, 10, key=f"rep_{giorno}_{i}")
                with col4:
                    note = st.text_input("Note", key=f"note_{giorno}_{i}")

                esercizi.append({
                    "giorno": giorno,
                    "esercizio": esercizio,
                    "serie": serie,
                    "ripetizioni": ripetizioni,
                    "note": note
                })
