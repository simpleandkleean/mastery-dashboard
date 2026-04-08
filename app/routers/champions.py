from fastapi import APIRouter
from app.data_dragon import load_champions

router = APIRouter()

@router.get("/champion/{champion_name}")
def get_champion(champion_name: str):
    champions = load_champions()
    champ = champions.get(champion_name)
    if not champ:
        return {"error": "Champion no encontrado"}
    return {
        "key": champ["key"],
        "name": champ["name"],
        "title": champ["title"],
        "image": champ["image"]["full"]
    }