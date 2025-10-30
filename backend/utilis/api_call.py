import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000/api/exercises"

@st.cache_data
def get_exercises():
    response = requests.get(BACKEND_URL)
    st.write("Status code:", response.status_code)
    st.write("Response preview:", response.text[:300])  # mostra i prim
    if response.status_code == 200:
        data = response.json()
        return [f"{exercise['name']} - {exercise['muscle']}" for exercise in data]
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return []   
