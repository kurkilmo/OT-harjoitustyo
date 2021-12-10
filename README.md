# Metadataeditori
Sovelluksen avulla käyttäjä voi lukea ja muokata erilaisten tiedostojen metadataa.
## Käyttöympäristö
Sovellus toimii Linux-koneilla, joihin on asennettu Exiftool-ohjelmisto. (Exiftool-ohjelma löytyy valmiina laitoksen koneilta)
## Dokumentaatio
[Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)  
[Työaikakirjanpito](dokumentaatio/tyoaikakirjanpito.md)

## Asennus
Ohjelman riippuvuudet asennetaan komennolla `poetry install`
## Komentorivitoiminnot

### Ohjelman suoritus
Ohjelman voi suorittaa komennolla `poetry run invoke start`
### Testaus
Testit suoritetaan komennolla `poetry run invoke test`
### Testikattavuus
Testikattavuusraportin generointi komennolla `poetry run invoke coverage-report`
### Pylint
Pylint-tarkistukset komennolla `poetry run invoke lint`

