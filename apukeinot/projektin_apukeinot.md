<h2>Tekoälyn käyttö projektia tehtäessä:</h2>

- .gitignore tiedoston sisällön tarkistus/varmistus ennen ensimmäistä committia
- Kysytty kuinka saada tietokantamallin Player osaksi events, joka on lista pelaajien tapahtumia. Muutaman kerran piti kysellä ennen kuin sain mitään omasta mielestäni järkevää ja sovellettavaa. Vastaus mihin tyydyin oli sqlmodelista importattavat Field ja Relationship ( näitä olen toteutuksessani käyttänyt ).
- Googlailun ohella pyysin selittämään ja tarkentamaan miksi käyttää Fields ja Relationship, sekä apua siihen kuinka käyttää niitä
- Kysyin tarkennusta back_populates jutusta kun en ymmärtänyt sitä, en ymmärtänyt keinoälyn vastauksestakaan joten palasin takaisin dokumentaatioon https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/back-populates/#the-value-of-back_populates
- Olin kirjoitellut playerin ja eventin routerit väärin, jolloin ohjelma rikkui --> copy pastesin virheviestin tekoälylle ja se kertoi routerin olevan kirjoitettu väärin ja antoi korjaus ehdotuksia. Tämä pohjalta tajusin muidenkin routerien olevan vajanaisesti/väärin kirjoiteltu, joten korjailin itsekseni loput routerit. Kerralla ei tietenkään mennyt nappiin loput, mutta trial and error niin saatiin toimimaan. ( Ei itseasias tullu edes vielä oikeesti korjatuiksi tässä kohtaa, palasin korjaamaan vielä kun tein uudet Mallit vastauksille )
- Asennus ohjeet ( näkyvät etusivulla ) ja kysytty että saako näillä ohjelman käyntiin, antoi siihen vielä jotain palautetta mutta en noudattanut "parannus"ohjeita vaan laitoin eteenpäin sillai ku olin kirjottanu koska sillä pitäisi saada ohjelma käyntiin


<h2>Googlen käyttö projektissa:</h2>

- Googlailtu back_populates --> https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/back-populates/#the-value-of-back_populates
- Googlailtu Content-Type header application/json
    - Goolailu ei oikein johtanut mihinkään, ohjelmani palautti ne ymmärtääkseni jo oikeassa muodossa


<h2>Luettuja/Käytettyjä dokumentaatioita:</h2>

- FastAPI dokumentaatio https://fastapi.tiangolo.com/
- SQLModel dokumentaatio https://sqlmodel.tiangolo.com/



<h2>Musiikkina toimi Medieval lofi radio, suosittelen lämpimästi (❁´◡`❁)</h2>
https://www.youtube.com/watch?v=IxPANmjPaek