from fastapi import APIRouter
from api.routes import weather

api_router = APIRouter()

api_router.include_router(weather.router, prefix="/weather", tags=["weather"])