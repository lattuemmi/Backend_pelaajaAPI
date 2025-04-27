from fastapi import HTTPException, status
from .models import Player, PlayerIn, EventIn, Event
from sqlmodel import Session, select
from datetime import datetime
from typing import List



# Pelaajiin liittyvät CRUD funktiot tulevat tänne 


#   Funktio uuden pelaajan luomiseele
#   Oetaan sisään session eli tietokantayhteys ja player_in eli käyttäjän syöttämä tieto uudesta pelaajasta
def create_player(session: Session, player_in: PlayerIn):
    #   Muutetaan syöte tietokantaobjektiksi
    pelaaja = Player.model_validate(player_in)
    #   Valmistellaan tietokantaan lisääminen
    session.add(pelaaja)
    #   Tallennetaan muutokset tietokantaan
    session.commit()
    #   Päivitetään pelaaja-objekti niin on kaikki tiedot
    session.refresh(pelaaja)
    #   Palautetaan luotu pelaaja
    return pelaaja


#   Funktio pelaajien hakemiseksi
#   session --> Tietokantayhteys
def get_players(session: Session):
    #   Suoritetaan kysely tietokantaan joka palauttaa listan kaikista pelaajista
    return session.exec(select(Player)).all()


#   Funktio pelaajan hakemiseksi id:n perusteella
#   session -> tietokantayhteys
#   otetaan sisään player_id -> voidaan suodattaa sen perusteella
def get_player_by_id(session: Session, player_id: int):
    player = session.get(Player, player_id)
    #   Jos pelaajaa ei löydy, heitetään virhe ja kerrotaan ettei pelaajaa ole
    if not player:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail=f"Player with id {player_id} not found."
        )
    #   Jos pelaaja löytyy, palautetaan pelaaja
    return player


#   Funktio pelaajan eventtien löytämiseksi
#   session --> Tietokantayhteys
#   Otetaan sisään player_id -> voidaan suodattaa sen perusteella
#   Otetaan sisään event_type -> voidaan suodattaa tietyn typen mukaan, ei kuitenkaan ole pakko
def get_specific_player_events(session: Session, player_id: int, event_type: List[str] = None):
    #   Haetaan pelaaja id:n perusteella
    player = session.get(Player, player_id)
    #   Jos pelaajaa ei löydy, heitetään 404
    if not player:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = f"Player with id {player_id} not found."
        )
    #   Haetaan pelaajan kaikki eventit
    events = player.events
    #   Tarkistetaan löytyykö eventtejä
    if event_type:
        #   Tarkistetaan löytyykö tunnettuja event tyyppejä, jos ei heitetään 400
        known_types = ["level_started", "level_solved"]
        if event_type not in known_types:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Unkown event type: {event_type}"
            )
        #   Käydäään läpi kaikki eventit, valitaan sieltä ne jotka täyttävät ehdon ja tehdään niistä uusilista
        events = [event for event in events if event.type in event.type == event_type]
    #   Palautetaan lista eventeistä
    return events


#   Funktio pelaajan eventin luomiselle
#   session -> Tietokantayhteys
#   Otetaan sisään player_id -> tiedetään kelle pelaajalle uusi eventti tulee
#   Otetaan sisään even_in -> käyttäjän syöttämä tieto uudesta tapahtumasta
def create_event_for_player(session: Session, player_id: int, event_in: EventIn):
    player = session.get(Player, player_id)
    #   Yritetään hakea pelaaja id:n peruteella, jos ei löydy niin heitetään 404
    if not player:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Player with id {player_id} not found."
        )
    
    #   Määritellään tunnetut eventit ja tarkistetaan ne, jos ei ole tunnettu annetaan 400
    known_types = ["level_started", "level_solved"]
    if event_in.type not in known_types:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"Unkown event type: {event_in.type}"
        )
    #   Luodaan uusi eventti, type ja detail tulevat käyttäjän syötteestä
    #   timedate hakee juuri sen hetken ajan ja player_id yhdistaa oikean pelaajan
    new_event = Event(
        type= event_in.type,
        detail= event_in.detail,
        timestamp=datetime.now(),
        player_id=player_id
    )

    #   Valmistellaan tietokantaan lisääminen
    session.add(new_event)
    #   Tallennetaan muutokset tietokantaan
    session.commit()
    #   Päivitetään event-objekti jotta saadaan tietokannan generoimatkin tiedot siihe
    session.refresh(new_event)
    #   Palautetaan luotu event
    return new_event