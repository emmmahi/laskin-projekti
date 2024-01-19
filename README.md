# Laskin-projekti 

Tein projektin gitlabiin ja liitin siihen jäseneksi opettajan. Loin yhteensä 7 Issueta eli tehtävää. Milestonet eli sprintit määritellään myös (projektin etenemisen aikana ennen seuraavaa sprtintiä?) ja niihin liitetään tarvittavat issuet.  Kloonasin projektin omalle koneelle ja loin kaksi kansioita ja niihin tiedostot. 
`Kansio: laskin -> tiedosto: laskut.py.` 
`Kansio: tests -> tiedosto test_laskut.py`

_Muista vielä nämä komennot Gitlabiin liittyen:_
````
git clone
git add .
git commit -m "...."
git push 

git status
````

Alussa myös hyvä tehdä jo kaikkien tarvittavien asioiden asennus, lue tarkkaan mitä kaikkia kerralla asennettu:
````
# riippuvuuksien asentaminen
python3 -m pip install coverage pytest pylint mkdocs mkdocstrings mkdocstrings-python
```` 

# Sprint 1: Laskimen koodaus 

## Olio-ohjelmointi


Loin ensimmäisen Milestonen ja liitin siihen yhden issuen. Käytin laskimen koodaamisessa olio-ohjelmointia. Sain laskimen toimimaan mielestäni hyvin, nollalla jakamisen kanssa pieniä haasteita ilmeni. Sen suorittamat laskutoimituksen oli siis yhteen-, vähennys-, kerto- ja jakolasku.

# Sprint 2: 

**yksikkotestaus pytest-kirjaston avulla** \
Olemassa erilaisia frameworkeja (testauskehikkoja) ja nyt käytössä `pytest`-moduuli.
pytest manuaali:
https://docs.pytest.org/en/7.2.x/contents.html

**coverage analyysi testien kattavuudesta** \
Koodikattavuus työkalu: tarkistaa kuinka suuren osan moduulin ohjelmakoodista yksikkötestit testaa.
https://coverage.readthedocs.io/en/6.5.0/ 


**Aikaansaannokset ja komennot** \ 
Tein siis perustoiminnallisuuksien yksikkötestausta **pytest** kirjaston avulla. Hyödynsin tässä esimerkkiprojektia, jotta sain jonkinlaiset testit aikaiseksi. Testitiedoston alkuun tarvitsi seuraavia juttuja, jotta pytest saadaan toimimaan
````
import pytest
from laskin.laskut import Laskin   #tai import laskin.laskut

@pytest.fixture
def laskut():
    return Laskin()
````
# Yksikkötestien suorittaminen ilman koodikattavuuden analyysia
`py -m pytest -v`

# Koodikattavuuden tarkistaminen
`py -m coverage run -m pytest -v`

# Koodikattavuuden analyysi / raportti
`py -m coverage report -m # analysoi "koko roskan"`

# Koodikattavuus tiettyjen tiedostojen osalta
`py -m coverage report -m laskin/laskut.py tests/test_laskut.py`

Muuttelin testi- ja kooditiedostoja saadakseni parhaan koodikattavuuden.

 # Sprint 3:

**Pylint eli staattinen koodianalyysi** \
Jokin sovellus lukee kirjoittamasi ohjelmakoodin ja antaa siitä palautteen, jonka avulla voit kirjoittaa paremman tuoksuista koodia ("code smells"). Työkaluna nyt pylint
https://pylint.pycqa.org/en/latest/user_guide/usage/run.html

`py -m pylint laskin.laskut.py` ajettuna terminaalissa antoi palautteen, miten koodia voisi vielä parantaa ja teinkin jo joitakin muutoksia, mm. turhan välilyönnit otin pois ja muutin atribuuttien nimiä. 

**pytest + coverage + pylint automatisointi** \ 
Tämä liittynee Gitlabin `CI/CD pipeline` asiaan. Tästä pitää vielä saada lisää kokemusta.

Loin projektin juurikansioon tiedoston `.gitlab-ci.yml`. Kopioin sinne esimerkkiprojektista tarvittavaa tekstiä ja vaihdoin omien kansioiden ja tiedostojen nimet sinne. Tämän jälkeen sain testit automaattisesti pyörimään jokaisen projektin päivityksen myötä. 

# Sprint 4: 

**Koodin dokumentointi mkdocsin avulla**

Lisäsin laskin.py tiedoston koodin sekaan tarvittavat merkinnät ja kirjoitukset. Kirjoitukset tulee `""" tekstiä """` väliin. Ylhäälle voi kirjoittaa yleistä koodista. Sitten tarkentavat "kommentit" luokasta ja metodeista suoraan niiden alle. 

````
py -m mkdocs new .
py -m mkdocs build
py -m mkdocs serve
````
Sivupalkkiin tuli uusi tiedostoja `mkdocs.yml`. Sinne lisäsin seuraavaa: 
````
site_name: Laskin- projektin koodi

plugins: 
  - mkdocstrings

nav: 
  - Index: index.md
  - Laskin: reference.md
  ````
  Lisäksi tuli kansio `docs` mikä sisälsi tiedoston `index.md`. Tein `docs` kansioon tiedoston `reference.md` ja sinne merkinnän `::: laskin.laskut`.

# Sprint 5: 

**Yksikkötestien kirjoitus docstringeihin**

Tässä vaiheessa muutin koodia paljon. Lopulta sain vaikeuksian jälkeen hyvät luvut analyysistä ja linttauksesta! Opin ainakin paljon tätä tehdessä.

Alla esimerkki doctestin tekemisestä. En osannut ehkä käyttää tässä luokkaa ja sen metodeita parhaalla mahdollisella tavalla mutta sain asian hoidettua kuitenkin. 
````
""" Metodi kertolaskua varten

        Examples:
            >>> Laskin().kertolasku(3,5)
            15.0
            >>> Laskin().kertolasku(4,0)
            0.0
            >>> Laskin().kertolasku(2.5, 2)
            5.0
        """
````
Testaus ajetaan komennolla \
 ´py -m doctest laskin/laskut.py´






