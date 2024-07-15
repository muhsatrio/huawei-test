import requests

def send():
    result = requests.get("https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json").json()
    info = result["Infogempa"]["gempa"]
    print("=======INFORMASI GEMPA========")
    print(f"Tanggal: {info["Tanggal"]}")
    print(f"Jam: {info["Jam"]}")
    print(f"Koordinat: {info["Coordinates"]}")
    print(f"Lintang: {info["Lintang"]}")
    print(f"Bujur: {info["Bujur"]}")
    print(f"Magnitude: {info["Magnitude"]}")
    print(f"Kedalaman: {info["Kedalaman"]}")
    print(f"Wilayah: {info["Wilayah"]}")
    print(f"Potensi: {info["Potensi"]}")
    print("==============================")