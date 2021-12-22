# Vaatimusmäärittely
## Sovelluksen tarkoitus
Sovelluksen avulla käyttäjä voi lukea ja muokata erilaisten tiedostojen metadataa, eli esimerkiksi tietoa valokuvatiedoston kameran tiedoista tai äänitiedoston otsikosta tai kappaleen esittäjästä.
## Käyttöliittymä
![](/dokumentaatio/images/main.png)
- Käyttöliittymä näyttää tiedoston polun ja nimen.
- Painikkeet tiedostojen avaamiselle ja tallentamiselle
- Lista avatun tiedoston metadatasta
  - Tiedot tekstikenttiä, joiden avulla muokkaus tapahtuu
## Toiminnallisuus
- Käyttäjä voi lukea annetun tiedoston metadatan
  - Tiedosto valitaan käyttöjärjestlemän tiedostonhallinnan avulla
  - Metadata näytetään käyttöliittymässä kahden sarakkeen listana
- Käyttäjä voi muokata metadataa
  - Muokatessa muutokset eivät vielä tallennu, vaan ne tallennetaan erikseen
  - Sovellus ei anna muokata tietoja, joiden muutokset voivat tehdä tiedoston lukukelvottomaksi tai muuten korruptoida tiedoston
- Käyttäjä voi tallentaa muokatun tiedoston tiedot
  - Tallennus alkuperäiseen tiedostoon
  - Alkuperäisestä tiedostosta luodaan kopio
## Jatkokehitys (kurssin jälkeen)
- Sovelluksen laajentaminen Windowsille
