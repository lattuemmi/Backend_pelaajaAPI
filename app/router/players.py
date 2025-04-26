from fastapi import APIRouter, status, Depends
from ..db.models import PlayerIn, EventIn
from ..db.players_crud import create_player, create_event_for_player, get_player_by_id, get_players, get_specific_player_events
from ..db.database import get_session
from sqlmodel import Session

# Pelaajien endpoint funktiot

router = APIRouter(prefix = "/players")

# Luo uuden pelaajan
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_new_player(player_in: PlayerIn, session: Session = Depends(get_session)):
    return create_player(session, player_in)

# Palauttaa pelaajien nimet ja id:t
@router.get("/", status_code=status.HTTP_200_OK)
def fetch_players(session: Session = Depends(get_session)):
    return get_players(session)


# Palauttaa tietyn pelaajan kaikki tiedot
@router.get("/{player_id}", status_code=status.HTTP_200_OK)
def fetch_player_by_id(id: int, session: Session = Depends(get_session)):
    return get_player_by_id(session, player_id = id)


# Palauttaa tietyn pelaajan kaikki eventit
@router.get("/{id}/events", status_code = status.HTTP_200_OK)
def fetch_player_by_id_and_their_events(id: int, session: Session = Depends(get_session)):
    return get_specific_player_events(session, player_id = id)


# Luo uuden eventin pelaajalle
@router.post("/{id}/events", status_code=status.HTTP_201_CREATED)
def create_new_event_for_player(id: int, event_in: EventIn, session: Session = Depends(get_session)):
    return create_event_for_player(session, player_id = id, event_in = event_in)