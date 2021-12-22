# Arkkitehtuurikuvaus

## Rakenne

Koodin pakkausrakenne on seuraava:  
![](/dokumentaatio/images/package.jpg)  
pakkaus _ui_ sisältää käyttöliittymän, _services_ työkalut metadatan hallintaan ja _data_ tietokannan, joka sisältää tietoa erilaisista metatiedoista.  

## Sovelluslogiikka

![](/dokumentaatio/images/class1.jpg)  
Luokka [metadata_tool](/src/services/metadata_tool.py) vastaa metadatan lukemisesta ja kirjoittamisesta metodeilla `get_metadata(file)` ja `set_metadata(file, tag, value)`.  
Luokka [metadata_info](/src/services/metadata_info.py) vastaa kommunikoinnista metatietojen ominaisuuksia sisältävän tietokannan kanssa. Metodi `check_writable(tag)` tarkistaa,
onko tietty metatieto kirjoitettavissa.

## Päätoiminnallisuus

Sovellus etenee seuraavasti:  
![](/dokumentaatio/images/sequence1.jpg)  

### Tiedoston avaaminen ja metatietojen näyttäminen

Kun käyttäjä avaa tiedoston, käyttöliittymä kutsuu `metadata_tool`-luokan metodia `get_metadata(file)`, joka palauttaa metatiedot sisältävän sanakirjan.
Käyttöliittymä tarkistaa `metadata_info`-luokan
metodin `check_writable(tag)` avulla, voiko kutakin metatietoa muokata. Muokattavissa olevat tiedot näytetään käyttäjälle.  

### Metatietojen tallentaminen

Kun käyttäjä tallentaa muokatut tiedot, käyttöliittymä käy läpi muuttuneet metatiedot ja tallentaa ne `set_metadata(file, tag, item)`-metodin avulla. Käyttäjälle näytetään
yhteenveto tietojen tallennuksesta.

## Rakenteen heikkoudet
Osan käyttöliittymän vastuulla olevasta toiminnallisuudesta voisi siirtää uuteen luokkaan.
