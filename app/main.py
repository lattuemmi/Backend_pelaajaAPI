from fastapi import FastAPI #Importataan FastAPI, jotta voidaan luoda API-sovellus
from app.db.database import create_db   #Tuodaan funktio jolla luodaan tietokanta ja yhteys
from app.router import players, events  #Tuodaan players ja events, jotta voidaan käyttää niihin tehtyjä router määrityksiä 
from contextlib import asynccontextmanager  #Tämän avulla saadaan hallittua tietokannan käynnistys ja sulkemista, jotta ne tapahtuvat oikein
from fastapi.middleware.cors import CORSMiddleware  #Tätä käyttäen voimme määritellä mistä sovelluksellemme voi puhua


#   Lifespan funktio
#   Määrittelee mitä tapahtuu sovelluksen elinkaaren alussa ja lopussa
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield

#   Luodaan FastAPI sovellus ja annetaan sille lifespanfunktio
#   Lifespan funktio kertoo sille mitä tehdä käynnistykessä ja sulkiessa
app = FastAPI(lifespan=lifespan)


#   Luon listan sallistuista origineista, ja koska en tiedä mitä niistä sallia
#   Sallin kaikki, joten nyt pystyisi juttelemaan mistä vaan
origins = ["*"]


#   Luodaan uusi välikappale FastAPI-sovellukseen, tämä middleware mahdollistaa CORS-pyynnöt
#   allow_origins -> mitkä originit sallittuja ( käytämme aiemmin luotua listaa)
#   allow_credentials -> Saako pyyntöjen mukana lähettää cookies, authorization headers etc
#   allow_methods -> Mitä kaikkia HTTP metodeja saa käytttää, ollaan annettu * eli kaikki sallittu
#   allow_headers -> Mitä headereita sallitaan ja tuetaan, ollaan annettu * eli kaikki sallittu
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#   Liitetään reitit sovellukseen, niiin ne toimii
app.include_router(players.router)
app.include_router(events.router)