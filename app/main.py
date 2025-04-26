from fastapi import FastAPI
from app.db.database import create_db
from app.router import players, events
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("startataan")
    create_db()
    yield
    print("lopetetaan")

app = FastAPI(lifespan=lifespan)

app.include_router(players.router)
app.include_router(events.router)