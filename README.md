Tässä projektissa luodaan pelaajaAPI Backend kurssin loppuharjoitukseksi. 


Tekoälyn käyttö projektia tehtäessä:

- .gitignore tiedoston sisällön tarkistus/varmistus ennen ensimmäistä committia
- Kysytty kuinka saada tietokantamallin Player osaksi events, joka on lista pelaajien tapahtumia. Muutaman kerran piti kysellä ennen kuin sain mitään omasta mielestäni järkevää ja sovellettavaa. Vastaus mihin tyydyin oli sqlmodelista importattavat Field ja Relationship ( näitä olen toteutuksessani käyttänyt ).
- Googlailun ohella pyysin selittämään ja tarkentamaan miksi käyttää Fields ja Relationship, sekä apua siihen kuinka käyttää niitä
- Kysyin tarkennusta back_populates jutusta kun en ymmärtänyt sitä, en ymmärtänyt keinoälyn vastauksestakaan joten palasin takaisin dokumentaatioon https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/back-populates/#the-value-of-back_populates
- Olin kirjoitellut playerin ja eventin routerit väärin, jolloin ohjelma rikkui --> copy pastesin virheviestin tekoälylle ja se kertoi routerin olevan kirjoitettu väärin ja antoi korjaus ehdotuksia. Tämä pohjalta tajusin muidenkin routerien olevan vajanaisesti/väärin kirjoiteltu, joten korjailin itsekseni loput routerit. Kerralla ei tietenkään mennyt nappiin loput, mutta trial and error niin saatiin toimimaan.
- 