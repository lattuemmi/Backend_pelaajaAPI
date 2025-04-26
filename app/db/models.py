from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
# Ylempää importtia tarvii, jotta saadaan Eventtejä käsiteltyä listana.
from datetime import datetime
#Ylempi importti tarvitaan jotta saadaan timedate, speksattua kirjausta varten


# Tietokanta mallien määrittelyt

class Player(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    events: List["Event"] = Relationship(back_populates="player")


class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type: str
    detail: str
    timestamp: datetime
    player_id: int = Field(foreign_key="player.id")
    player: Optional[Player] = Relationship(back_populates="events")


class PlayerIn(SQLModel):
    name: str


class EventIn(SQLModel):
    type: str
    detail: str
