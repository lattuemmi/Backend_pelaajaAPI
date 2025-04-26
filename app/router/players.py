from typing import List, Optional
from fastapi import APIRouter, status, Depends
from ..db.models import PlayerIn, PlayerOut, PlayerAllInfoOut,  EventIn, EventOut
from ..db.players_crud import create_player, create_event_for_player, get_player_by_id, get_players, get_specific_player_events
from ..db.database import get_session
from sqlmodel import Session

# Pelaajien endpoint funktiot

#   Luodaan uusi router
#   Prefix -> Kaikki polut jotka liittyvät tähän routeriin alkavat polulla "/players"
router = APIRouter(prefix = "/players")


#   Määritetään POST pyyntö polkuun /players/
#   Jos saadaan pelaaja luotua, palautetaan 201
#   Funkstio kutsuu create_player funktiota
#   ja antaa sille tietokantayhteyden ja käyttäjän syöttämät pelaajatiedot
@router.post("/", response_model=PlayerOut,status_code=status.HTTP_201_CREATED)
def create_new_player(player_in: PlayerIn, session: Session = Depends(get_session)):
    return create_player(session, player_in)


#   Määritetään GET pyyntö polkuun /players/
#   Jos onnistuu annetaan 200
#   Funktio ottaa sisään vain tietokantayhteyden
#   Kutsuu funktiota get_players ja hakee kaikki pelaajat
@router.get("/", response_model=List[PlayerOut], status_code=status.HTTP_200_OK)
def fetch_players(session: Session = Depends(get_session)):
    return get_players(session)


#   Määritetään GET pyyntö polkuun /players/{id}
#   Jos onnistuu annetaan 200 
#   Funktio oottaa sisään session(tietokantayhteys) ja id:n
#   Kutsuu funktiota get_player_by_id joka hakee pelaajan id:n perusteella
@router.get("/{id}", response_model= PlayerAllInfoOut, status_code=status.HTTP_200_OK)
def fetch_player_by_id(id: int, session: Session = Depends(get_session)):
    return get_player_by_id(session, player_id = id)


#   Määritetään GET pyytnö polkuun /players/{id}/events
#   Jos onnistuu annetaan 200
#   Funktio ottaa sisään session (tietokantayhteys) ja id:n
#   Kutsuu funktiota get_specific_player_events joka hakee kaikki id:n perusteella tietn pelaajan tapahtumat
@router.get("/{id}/events", response_model=List[EventOut], status_code = status.HTTP_200_OK)
def fetch_player_by_id_and_their_events(id: int, type: Optional[str] = None, session: Session = Depends(get_session)):
    return get_specific_player_events(session, player_id = id, event_type=type)


#   Määritetään POST pyyntö polkuun /players/{id}/events
#   Jos onnistuu annetaan 201
#   Funktio ottaa sisään session(tietokantaytheys), id:n ja eventin
#   Kutsuu create_event_for_player funktiota joka tallentaa uuden tapahtuman id:n perusteella oikealle pelaajalle
@router.post("/{id}/events", response_model= EventOut, status_code=status.HTTP_201_CREATED)
def create_new_event_for_player(id: int, event_in: EventIn, session: Session = Depends(get_session)):
    return create_event_for_player(session, player_id = id, event_in = event_in)