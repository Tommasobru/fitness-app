from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import exercises

app = FastAPI(title = "Fitness App Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(exercises.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Fitness App Backend"}



