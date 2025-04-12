from fastapi import APIRouter
from service import weather_service

router = APIRouter()

@router.get("/")
def get(province: str, city: str | None = None):
    result = weather_service.get(province, city)

    return {
        "datas": result
    }

@router.get("/_provinces-key")
def get_list_provinces():
    result = weather_service.get_list_provinces()

    return {
        "provinces": result
    }