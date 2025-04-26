from fastapi import APIRouter, status, Depends
from ..db.models import EventOut
from ..db.events_crud import get_events
from ..db.database import get_session
from sqlmodel import Session
from typing import List

#Eventtien endpoint funktiot tänne

#   Luodaan uusi router
#   Prefix -> kaikki polut jotka liittyvät tähän routeriin alkavat polulla "/events"
router = APIRouter(prefix="/events")


#   Määritetään GET pyyntö polkuun /events/
#   response_model -> FastAPI antaa palautettavat tiedot listana EventOut-objekteja
#   Funktio ottaa sisään kaksi parametriä
#   event_type -> Voi olla tyhjä, jos annetaan haetaan vain tietyn tyyppisiä tapahtumia
#   Session -> kerrotaan että otetaan tietokantayhteys
#   return get_events -> kutsuu crud funktiota ja käyttää sisään otettuja parametrejä
@router.get("/", response_model= List[EventOut], status_code=status.HTTP_200_OK)
def fetch_events(event_type: str = None, session: Session = Depends(get_session)):
    return get_events(session, event_type)
