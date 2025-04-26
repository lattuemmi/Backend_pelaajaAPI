from sqlmodel import Session, create_engine, SQLModel

# Databasen alustaminen tapahtuu täällä


#   Googlen mukaan tämä on erityisesti SQLite tietokantaa varten
#   Google: Sallii sen että useampi saie voi käyttää samaa tietokantayhteyttä
#   Täytyy myöntää että menee snadisti yli hilseen juuri nyt
connect_args = {"check_same_thread": False}


#   Luodaan tietokantayhteyden moottori
#   echo=True --> Näyttää SQL-kyselyt joita sovellus tekee konsolissa
engine = create_engine("sqlite:///./players.db", echo=True, connect_args=connect_args)


#   Luo taulut tietokantaan
def create_db():
    SQLModel.metadata.create_all(engine)


#   Tätä kohtaa en 100% sisäistä
#   Luodaan tietokantayhteys ja suljetaan se (?)
def get_session():
    with Session(engine) as session:
        yield session