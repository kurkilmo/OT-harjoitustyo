# Vaatimusmäärittely
## Sovelluksen tarkoitus
Sovelluksen avulla käyttäjä voi lukea ja muokata erilaisten tiedostojen metadataa, eli esimerkiksi tietoa valokuvatiedoston kameran tiedoista tai äänitiedoston otsikosta tai kappaleen esittäjästä.
## Käyttöliittymäluonnos
![](https://github.com/kurkilmo/OT-harjoitustyo/blob/master/laskarit/viikko1/IMG_20211116_135243.jpg)
- Käyttöliittymä näyttää tiedoston polun ja nimen, ja esim. kuvatiedostojen tapauksessa esikatselun kuvasta
- Napit tiedostojen avaamiselle ja tallentamiselle
- Lista avatun tiedoston metadatasta
  - Tiedot tekstikenttiä, joiden avulla muokkaus tapahtuu
## Toiminnallisuus
- Käyttäjä voi lukea annetun tiedoston metadatan (tehty)
  - Graafisessa käyttöliittymässä tiedosto valitaan käyttöjärjestelmän tiedostonhallinnan avulla, tekstikäyttöliittymässä antamalla komento ja tiedoston polku
  - Metadata näytetään käyttöliittymässä kahden sarakkeen listana
- Käyttäjä voi muokata metadataa (tehty osittain)
  - Muokatessa muutokset eivät vielä tallennu, vaan ne tallennetaan erikseen (tehty)
  - Sovellus ei anna muokata tietoja, joiden muutokset voivat tehdä tiedoston lukukelvottomaksi tai muuten korruptoida tiedoston
    - Mahdollinen "Safe Mode", josta poistuessa myös muita tietoja voidaan muokata
- Käyttäjä voi tallentaa muokatun tiedoston (tehty osittain, tällä hetkellä tallennus vain samaan tiedostoon)
  - Mahdollisuus tallentaa joko samaan tai uuteen tiedostoon (save / save as)
  - Tallennus käyttöjärjestelmän tiedostonhallinnan kautta (tekstikäyttöliittymässä komennolla ja tiedoston polulla)
