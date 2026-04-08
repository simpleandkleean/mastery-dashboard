import httpx
from fastapi import HTTPException
from app.config import RIOT_API_KEY, REGION

BASE_URL = f"https://{REGION}.api.riotgames.com"

RIOT_ERROR_MESSAGES = {
    400: "Petición malformada a la API de Riot",
    401: "API key no enviada",
    403: "API key inválida o blacklisted",
    404: "Recurso no encontrado",
    415: "Tipo de contenido no soportado",
    429: "Rate limit alcanzado — espera antes de reintentar",
    500: "Error interno en los servidores de Riot",
    503: "Servidores de Riot no disponibles temporalmente",
}

async def riot_get(path: str) -> dict:
    url = f"{BASE_URL}{path}"
    headers = {"X-Riot-Token": RIOT_API_KEY}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()

    if response.status_code == 429:
        retry_after = response.headers.get("Retry-After", "desconocido")
        raise HTTPException(
            status_code=429,
            detail=f"Rate limit alcanzado. Reintenta en {retry_after} segundos."
        )

    message = RIOT_ERROR_MESSAGES.get(
        response.status_code,
        f"Error inesperado de Riot ({response.status_code})"
    )
    raise HTTPException(status_code=response.status_code, detail=message)