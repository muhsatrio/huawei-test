## Requirements

- Python `>=3.8`

## How to Run
1. Activate virtual environment ([click here for reference](https://docs.python.org/3/library/venv.html))
2. Run `pip3 install -r requirements.txt`
3. Run `fastapi dev main.py`
4. API will run in `http://localhost:8000`

## How to Test

1. Run `pytest`

## API Documentation

### Get Provinces Key

#### URL
```
GET /weather/_provinces-key
```

#### Response
```
{
    "provinces": [
        "aceh",
        "bali",
        "bangka-belitung",
        "banten",
        "bengkulu",
        "di-yogyakarta",
        "dki-jakarta",
        "gorontalo",
        "jambi",
        "jawa-barat",
        "jawa-tengah",
        "jawa-timur",
        "kalimantan-barat",
        "kalimantan-selatan",
        "kalimantan-tengah",
        "kalimantan-timur",
        "kalimantan-utara",
        "kepulauan-riau",
        "lampung",
        "maluku",
        "maluku-utara",
        "nusa-tenggara-barat",
        "nusa-tenggara-timur",
        "papua",
        "papua-barat",
        "riau",
        "sulawesi-barat",
        "sulawesi-selatan",
        "sulawesi-tengah",
        "sulawesi-tenggara",
        "sulawesi-utara",
        "sumatera-barat",
        "sumatera-selatan",
        "sumatera-utara"
    ]
}
```

### Get Weather

#### URL
```
GET /weather?province=(province)&city=(city)
```

### Query Param Description
- `province` Inputed province with prefix `-` and lower case. This query param is REQUIRED
- `city` Inputed city with prefix `-` and lower case. If this input is empty, will return all the cities data from inputed province

#### Response
```
{
    "datas": {
        "city": "Bandung",
        "key": "bandung",
        "max_temperature": [
            {
                "date_time": "2024-07-15 00:00:00",
                "temperature_in_celcius": 30
            },
            {
                "date_time": "2024-07-16 00:00:00",
                "temperature_in_celcius": 30
            },
            {
                "date_time": "2024-07-17 00:00:00",
                "temperature_in_celcius": 26
            }
        ],
        "weather": [
            {
                "date_time": "2024-07-15 00:00:00",
                "weather": "Cerah"
            },
            {
                "date_time": "2024-07-15 06:00:00",
                "weather": "Cerah Berawan"
            },
            {
                "date_time": "2024-07-15 12:00:00",
                "weather": "Cerah Berawan"
            },
            {
                "date_time": "2024-07-15 18:00:00",
                "weather": "Cerah Berawan"
            },
            {
                "date_time": "2024-07-16 00:00:00",
                "weather": "Cerah"
            },
            {
                "date_time": "2024-07-16 06:00:00",
                "weather": "Cerah"
            },
            {
                "date_time": "2024-07-16 12:00:00",
                "weather": "Cerah Berawan"
            },
            {
                "date_time": "2024-07-16 18:00:00",
                "weather": "Cerah Berawan"
            },
            {
                "date_time": "2024-07-17 00:00:00",
                "weather": "Cerah Berawan"
            },
            {
                "date_time": "2024-07-17 06:00:00",
                "weather": "Cerah"
            },
            {
                "date_time": "2024-07-17 12:00:00",
                "weather": "Cerah Berawan"
            },
            {
                "date_time": "2024-07-17 18:00:00",
                "weather": "Cerah Berawan"
            }
        ]
    }
}
```