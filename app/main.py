from fastapi import FastAPI
from app.db.database import create_db
from app.router import players, events
from contextlib import asynccontextmanager


#   Lifespan funktio
#   Määrittelee mitä tapahtuu sovelluksen elinkaaren alussa ja lopussa
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield

#   Luodaan FastAPI sovellus ja annetaan sille lifespanfunktio
#   Lifespan funktio kertoo sille mitä tehdä käynnistykessä ja sulkiessa
app = FastAPI(lifespan=lifespan)


#   Liitetään reitit sovellukseen, niiin ne toimii
app.include_router(players.router)
app.include_router(events.router)