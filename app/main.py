from fastapi import FastAPI
from app.data_dragon import load_champions
from app.routers import mastery
from contextlib import asynccontextmanager
from app.routers import champions

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_champions()
    yield

app = FastAPI(title="Mastery Dashboard API", lifespan=lifespan)  
app.include_router(mastery.router, prefix="/api")
app.include_router(champions.router, prefix="/api")

@app.get("/health")
async def health():
    return {"status": "ok"}