from fastapi import APIRouter, status, Depends
from ..db.models import Event, EventIn
from ..db.events_crud import *
from ..db.database import get_session
from sqlmodel import Session

#Eventtien endpoint funktiot tänne

router = APIRouter(prefix="/events")

@router.get("/", response_model=list[Event])
def get_events(event_type: str = None, session: Session = Depends(get_session)):
    return get_events(session, event_type)
