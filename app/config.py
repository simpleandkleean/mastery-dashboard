from dotenv import load_dotenv
import os

load_dotenv()

RIOT_API_KEY = os.getenv("RIOT_API_KEY")
PUUID = os.getenv("PUUID")
REGION = os.getenv("REGION")

if not all([RIOT_API_KEY, PUUID, REGION]):
    raise RuntimeError("Faltan variables de entorno obligatorias")