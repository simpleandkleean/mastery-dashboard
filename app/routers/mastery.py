from fastapi import APIRouter
from app.riot_client import riot_get
from app.config import PUUID
from app.data_dragon import load_champions
from app.routers import champions

router = APIRouter()

@router.get("/mastery")
async def get_mastery(championId: int):
    path = f"/lol/champion-mastery/v4/champion-masteries/by-puuid/{PUUID}/by-champion/{championId}"
    data = await riot_get(path)
    return {
        "championId": data["championId"],
        "championLevel": data["championLevel"],
        "championPoints": data["championPoints"],
        "lastPlayTime": data["lastPlayTime"],
        "championPointsSinceLastLevel": data["championPointsSinceLastLevel"],
        "championPointsUntilNextLevel": data["championPointsUntilNextLevel"],
    }

@router.get("/mastery_by_name/{champion_name}")
async def get_mastery_by_name(champion_name: str):
    champions = load_champions()
    champ_name_lower = champion_name.lower()
    champ = next(
        (c for name, c in champions.items() if name.lower() == champ_name_lower),
        None
    )
    if not champ:
        return {"error": "Champion no encontrado"}

    champion_id = int(champ["key"])
    path = f"/lol/champion-mastery/v4/champion-masteries/by-puuid/{PUUID}/by-champion/{champion_id}"
    data = await riot_get(path)

    return {
        "championId": data["championId"],
        "championLevel": data["championLevel"],
        "championPoints": data["championPoints"],
        "lastPlayTime": data["lastPlayTime"],
        "championPointsSinceLastLevel": data["championPointsSinceLastLevel"],
        "championPointsUntilNextLevel": data["championPointsUntilNextLevel"],
    }
