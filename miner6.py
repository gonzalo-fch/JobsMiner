import requests
import json
import time
import os  # 👈 NUEVO

API_URL = "https://remoteok.com/api"

MAX_REQUESTS = 10
SLEEP_TIME = 1


class RequestLimiter:
    def __init__(self, max_requests):
        self.max_requests = max_requests
        self.count = 0

    def can_request(self):
        return self.count < self.max_requests

    def add_request(self):
        self.count += 1


limiter = RequestLimiter(MAX_REQUESTS)


def obtener_trabajos():
    if not limiter.can_request():
        print(" Límite alcanzado")
        return None

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    response = requests.get(API_URL, headers=headers)
    limiter.add_request()

    print(f"Request #{limiter.count} → {API_URL}")

    if response.status_code != 200:
        print(f" Error: {response.status_code}")
        return None

    time.sleep(SLEEP_TIME)
    return response.json()


def limpiar_datos(data):
    trabajos = []

    for item in data[1:]:
        job = {
            "id": item.get("id"),
            "titulo": item.get("position"),
            "empresa": item.get("company"),
            "ubicacion": item.get("location"),
            "tags": item.get("tags"),
            "salario": item.get("salary_min"),
            "url": item.get("url"),
            "fecha": item.get("date")
        }

        trabajos.append(job)

    return trabajos


import os

def guardar_json(data, archivo="remote_jobs.json"):
    import os

    # Ruta correcta (tu caso)
    desktop_path = os.path.join(os.environ["USERPROFILE"], "OneDrive", "Escritorio")

    # Crear carpeta si no existe (por seguridad)
    os.makedirs(desktop_path, exist_ok=True)

    file_path = os.path.join(desktop_path, archivo)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"\n Guardado en: {file_path}")


if __name__ == "__main__":
    raw_data = obtener_trabajos()

    if raw_data:
        trabajos = limpiar_datos(raw_data)
        guardar_json(trabajos)

        print(f"\n Requests usados: {limiter.count}/{MAX_REQUESTS}")
        print(f" Trabajos guardados: {len(trabajos)}")