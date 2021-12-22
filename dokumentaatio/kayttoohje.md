# Käyttöohje

## Ohjelman käynnistäminen

Ohjelman riippuvuudet asennetaan komennolla
```bash
poetry install
```

Ohjelman voi nyt käynnistää komennolla
```bash
poetry run invoke start
```
Ohjelman voi myös käynnistää ilman poetry-riippuvuuksia esim. komennolla
```bash
python3 -m src/index.py
```

## Ohjelman käyttö

### Tiedoston valitseminen

Ohjelman avautuessa ohjelma pyytää valitsemaan tiedoston, jonka metadata luetaan:  
![](/dokumentaatio/images/open.png)  
Uuden tiedoston voi tämän jälkeen avata "Open file" -painikkeella.

### Tietojen muokkaus

Kun tiedosto on valittu, ohjelma näyttää listan tiedoston metatiedoista:  
![](/dokumentaatio/images/main.png)  
Tietoja voi muokata muuttamalla kenttien tekstiä:  
![](/dokumentaatio/images/edit.png)  

### Tietojen tallennus

Muokatut tiedot voi tallentaa "Save edited metadata" -painikkeella.
Tällöin ohjelma näyttää yhteenvedon onnistuneista ja epäonnistuneista yrityksistä muokata metatietoja:  
![](/dokumentaatio/images/successdialog.png)  
Tiedot tallentuvat alkuperäiseen tiedostoon, ja ohjelma luo alkuperäisestä tiedostosta kopion, jonka nimi päättyy "\_original".
Jotkin tiedot hyväksyvät pelkkiä numeroarvoja. Esimerkiksi tekstin tallentaminen näihin tietoihin voi johtaa epäonnistuneisiin muokkausyrityksiin.
