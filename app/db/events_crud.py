from fastapi import HTTPException, status
from .models import Event
from sqlmodel import Session, select

# Eventteihin liittyvät CRUD operaatiot tulevat tänne


#GET/events - palauttaa kaikki eventit
# statuskoodi: 200
# Jos ei eventtejä, palauttaa tyhjän listan ( tarkista response spekseistä)
# Jos kysellään tuntematonta evettyyppiä, palautuu Bad request

def get_events(session: Session, event_type: str = None):
    known_types = ["level_started", "level_solved"]
    if event_type:
        if event_type not in known_types:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Unknown event type: {event_type}"
            )
        return session.exec(select(Event).where(Event.type == event_type)).all()
    return session.exec(select(Event)).all()