# Ohjelmistotekniikka

Tämä repositorio sisältää sekä **laskarit** että *harjoitustyön* kurssia Ohjelmistotekniikka varten.

## Harjoitustyö: sudoku
### Uusin release
[loppupalautus](https://github.com/jnnhan/ot-sudoku/releases/tag/loppupalautus)

[release viikko 6](https://github.com/jnnhan/ot-sudoku/releases/tag/viikko6)

[release viikko 5](https://github.com/jnnhan/ot-sudoku/releases/tag/viikko5)

### Dokumentaatio
[käyttöohje](https://github.com/jnnhan/ot-sudoku/blob/main/dokumentaatio/kayttoohje.md)

[vaatimusmaarittely](https://github.com/jnnhan/ot-sudoku/blob/main/dokumentaatio/vaatimusmaarittely.md)

[testausdokumentti](https://github.com/jnnhan/ot-sudoku/blob/main/dokumentaatio/testausdokumentti.md)

[tuntikirjanpito](https://github.com/jnnhan/ot-sudoku/blob/main/dokumentaatio/tuntikirjanpito.md)

[changelog](https://github.com/jnnhan/ot-sudoku/blob/main/dokumentaatio/changelog.md)

[arkkitehtuuri](https://github.com/jnnhan/ot-sudoku/blob/main/dokumentaatio/arkkitehtuuri.md)


## Huomioita
Sovellus on tehty ja testattu käyttäen python-versiota `3.8` sekä poetry-versiota `1.4.1`. Erityisesti vanhempien poetry-versioiden kanssa voi tulla ongelmia.
 
### Asennus
1. Kloonaa repositorio ja asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita alustustoimenpiteet (tietokannan ja sudokujen haku) komennoilla:

```bash
poetry run invoke init
```

### Aloitus
Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

### Testaus

Sovelluksen testit käynnistyvät komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi luoda komennolla:

```bash
poetry run invoke coverage-report
```

Raportti löytyy sovelluksen juurihakemistosta *htmlcov*-hakemistosta. Graafinen raportti löytyy tiedostosta *index.html*

### Koodin laadun testaus

Koodin laadun voi tarkistaa komennolla:

```bash
poetry run invoke lint
```
