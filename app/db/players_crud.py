from fastapi import HTTPException, status
from .models import Player, PlayerIn, EventIn, Event
from sqlmodel import Session, select
from datetime import datetime

# Pelaajiin liittyvät CRUD funktiot tulevat tänne 


#POST/players - uuden pelaajan luominen
#   Onnistuess statuskoodi: 201
#   Jos request sisältää virheellistä dataa, palauta 422

def create_player(session: Session, player_in: PlayerIn):
    pelaaja = Player.model_validate(player_in)
    session.add(pelaaja)
    session.commit()
    session.refresh(pelaaja)
    return pelaaja


#GET/players - palauttaa pelaajien nimet ja id:t
#   Statuskoodi: 200
#   Jos ei pelaajia, palauta tyhjä lista
#   Tarkista response speksauksesta

def get_players(session: Session):
    return session.exec(select(Player)).all()


#GET/players/{id} - palauttaa tietyn pelaajan kaikki tiedot
#   Statuskoodi: 200
#   Jos kysellään tuntematonta pelaajaa, palauta 404
def get_player_by_id(session: Session, player_id: int):
    player = session.get(Player, player_id)
    if not player:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail=f"Player with id {player_id} not found."
        )
    return player


#GET/players/{id}/events - palauttaa tietyn pelaajan kaikki eventit
#   Statuskoodi:200
#   Tuntemattoman pelaajan kysely, palauta 404
#   Jos ei eventtejä --> palauta tyhjä lista
def get_specific_player_events(session: Session, player_id: int, event_type: str = None):
    player = session.get(Player, player_id)
    if not player:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = f"Player with id {player_id} not found."
        )
    events = player.events
    if event_type:
        known_types = ["level_started", "level_solved"]
        if event_type not in known_types:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = f"Unkown event type: {event_type}"
            )
        events = [event for event in events if event.type == event_type]
    return events


#POST/players/{id}/events - luo uuden eventin pelaajalle
#   Tuntematon pelaaja --> 404
#   Tuntematon event --> 400
#   Requestissa virheellistä dataa --> 422
#   Onnistuessa --> 201
def create_event_for_player(session: Session, player_id: int, event_in: EventIn):
    player = session.get(Player, player_id)
    if not player:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Player with id {player_id} not found."
        )
    
    known_types = ["level_started", "level_solved"]
    if event_in.type not in known_types:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"Unkown event type: {event_in.type}"
        )
    
    new_event = Event(
        type= event_in.type,
        detail= event_in.detail,
        timestamp=datetime.now(),
        player_id=player_id
    )
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return new_event