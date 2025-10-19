from fastapi import APIRouter
import os
import requests


router = APIRouter()
rapid_api_key = os.getenv("RAPID_API_KEY")

@router.get("/exercises")
async def get_exercises():
    url = "https://exercisedb.p.rapidapi.com/exercises"
    headers = {
        "X-RapidAPI-Key": rapid_api_key,
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch exercises"}
    