from fastapi import FastAPI

from src.api.routes import api_routes

app = FastAPI()

app.include_router(api_routes)
