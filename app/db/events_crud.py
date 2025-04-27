from fastapi import HTTPException, status #Käytetään palauttamaan esimerkiski virhe, status antaa numerokoodit valmiiksi
from .models import Event   #Tuodaan malli joka kuvaa tietokannan Events taulun rakennetta
from sqlmodel import Session, select  #Työkaluja tietokanta kyselyihin, avataan yhteys ja rakennetaan kysely

# Eventteihin liittyvä CRUD operaatio tulee tänne


# get_events funktio ottaa sisään session (tietokanta yhteys?) ja event_typen joka on suodatin 
def get_events(session: Session, event_type: str = None):
    #   known_types --> määritelään lista tunnetuista eventtityypeistä
    known_types = ["level_started", "level_solved"]
    
    # Tarkistetaan onko annettu event_type, jos ei ole niin palautetaan kaikki eventit myöhemmin
    if event_type:
        #   Jos käyttäjää antaa tuntemattonan eventtyypin, palautetaan 404
        if event_type not in known_types:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Unknown event type: {event_type}"
            )
        #   Jos eventtype on tunnettu, tehdään tietokantakysely
        #   Haetaan Event-taulusta ja suodatetaan eventit jotka vastaa tunnettua tyyppiä
        #   Suoritetaan ja palautetaan kaikki löytynyt listana
        return session.exec(select(Event).where(Event.type == event_type)).all()
    
    #   Jos käyttäjä ei antanut mitän event_typeä, tehdään kysely jossa kysellään kaikki eventit ja palautetaan ne listana
    return session.exec(select(Event)).all()

