from service import weather_service
import pytest
from fastapi import HTTPException

def test__get__success():
    response = weather_service.get("jawa-barat", "bandung")
    assert len(response) > 0

def test__get__city_is_empty__success():
    response = weather_service.get("jawa-barat", None)
    assert len(response) > 0

def test__get__province_not_found__error():
    with pytest.raises(HTTPException) as excinfo:
        weather_service.get("asdasd", "")
    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "province is Not Found"

def test__get__city_not_found__error():
    with pytest.raises(HTTPException) as excinfo:
        weather_service.get("jawa-barat", "asdasdasd")
    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "city is Not Found"

def test__get_provinces_key__success():
    response = weather_service.get_list_provinces()
    assert len(response) > 0