from sqlmodel import SQLModel, Field


class PlayerBase(SQLModel):
    id: int
    name: set
    events: list


class EventBase(SQLModel):
    id: int
    type: str
    detail: str
    timestamp: str
    player_id: int