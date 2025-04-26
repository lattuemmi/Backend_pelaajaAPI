from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime


# Tietokanta mallien määrittelyt


#   Malli jolla saadaan luotua pelaaja tietojantaan
#   SQLModel, table = True --> tehdään oikea taulu tietokantaan
class Player(SQLModel, table=True):
    #   Id voi olla tyhjä, jolloin tietokanta automaattisesti generoi sen
    #   Id toimii pääavaimena
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    #   Lista  eventeistä jotka liittyvät yhteen pelaajaan
    #   Relationshipin arvo on kokonainen objekti, tässä tapauksessa Event
    #   back_populates --> String: player referoi player attribuuttiin luokassa Event
    #   En ihan 100% ymmärrä back_poplates, opettajaa referoiden sanoisin että SQLModel magiikkaa :)
    events: List["Event"] = Relationship(back_populates="player")


class Event(SQLModel, table=True):
    # Id voi olla tyhjä, jolloin tietokanta autoomattisesti generoi sen
    # Id toimii pääavaimena
    id: Optional[int] = Field(default=None, primary_key=True)
    type: str
    detail: str
    timestamp: datetime
    #   Liittyy johonkin pelaajaan
    #   Vierasavain --> viittaa Player taulun id kohtaan
    #   Tämä kohta ei saa olla tyhjä
    player_id: int = Field(foreign_key="player.id", nullable=False)
    #   Player objekti johon tämä Event liittyy
    #   back_populates pitää ytheyden molempiin suuntiin (?)
    player: Player = Relationship(back_populates="events")

#   Malli uuden eventin luontia varten 
#   Käyttäjä antaa vain type ja detail kentätä
#   Loput kentät määrittelee crud funktio tiedostossa players_crud.py
class EventIn(SQLModel):
    type: str
    detail: str

class EventOut(SQLModel):
    id: int
    type: str
    detail: str
    timestamp: datetime
    player_id: int

#   Malli uuden pelaajan luontia varten
#   Tietokanta luo id:n joten ei tarve kuin vain nimelle
class PlayerIn(SQLModel):
    name: str



#   Malli vastauksen muotoon
class PlayerOut(SQLModel):
    id: int
    name:str


class PlayerAllInfoOut(SQLModel):
    id: int
    name: str
    events: List[EventOut] = []