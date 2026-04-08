import requests
import os
from dotenv import load_dotenv

load_dotenv()

DATA_DRAGON_URL = os.getenv("DATA_DRAGON_URL")

_champions_cache = None

def load_champions():
    global _champions_cache
    if _champions_cache is None:
        print("📥 Cargando Data Dragon...")
        response = requests.get(DATA_DRAGON_URL)
        response.raise_for_status()
        data = response.json()
        _champions_cache = data["data"] 
        print("✅ Data Dragon cargado en caché")
    return _champions_cache