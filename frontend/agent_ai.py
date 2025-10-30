from datapizza.clients.openai import OpenAIClient
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAIClient(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4o-mini")
print(os.getenv("OPENAI_API_KEY"))
def generate_plan(user_input):
    prompt = f"""
        Sei un personal trainer virtuale. Crea una scheda di allenamento settimanale per un utente con queste caratteristiche:
        - Obiettivo: {user_input['goal']}
        - Livello: {user_input['level']}
        - Giorni a settimana: {user_input['days_per_week']}
        - Attrezzatura disponibile: {', '.join(user_input['equipment'])}
        - Preferenze: {user_input['preferences']}

        Restituisci un JSON con questo formato:
        {{
            "giorni": [
                {{
                    "giorno": 1,
                    "esercizi": [
                        {{
                            "nome": "Panca piana",
                            "serie": 4,
                            "ripetizioni": 10,
                            "note": "Usa carico medio"
                        }}
                    ]
                }}
            ]
        }}
    """

    result =client.invoke(prompt).text
    print(result)