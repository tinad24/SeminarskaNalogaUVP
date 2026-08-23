ANALIZA PODATKOV O OGLASIH ZA PRODAJO PAMETNIH TELEFONOV

OPIS PROJEKTA

Ta projekt vsebuje analizo podatkov o oglasih za prodajo pametnih telefonov, zbranih s spletne strani Bolha.com, iz kategorije Pametni mobilni telefoni. Projekt vključuje zbiranje podatkov, njihovo obdelavo in statistično analizo z vizualizacijami.

FUNKCIONALNOSTI:

1. Zbiranje podatkov
- pridobivanje_podatkov.py: Avtomatsko prenaša HTML vsebino s spletne strani Bolha.com
- Zbira podatke o oglasih za pametne telefone z 35 strani z rezultati

2. Obdelava podatkov
- priprava_podatkov.py: Obdeluje in čisti zbrane podatke
- Iz naslova oglasa razbere znamko telefona in shranjevalno kapaciteto
- Izloči oglase, kjer nekdo telefon išče oz. odkupuje, ter podvojene, izpostavljene oglase
- Shranjuje podatke v CSV in JSON formatih

3. Analiza podatkov
- analiza_podatkov.ipynb: Jupyter notebook z analizo
- Vključuje različne tipe vizualizacij:
  - Box plot-i
  - Tortni diagram
  - Stolpčni diagram
  - Lollipop chart
  - Scatter plot z regresijskim modelom

4. Statistične analize
- Pearsonov korelacijski koeficient
- Linearna regresija
- Analiza distribucije cen
- Primerjava povprečnih cen med znamkami in kraji

PODATKI

Projekt analizira naslednje podatke o oglasih za pametne telefone:
- Naslov oglasa: Naslov, kot ga je vnesel prodajalec
- Znamka: Znamka telefona, določena iz naslova oglasa (Apple, Samsung, Xiaomi, ...)
- Kapaciteta (GB): Shranjevalna kapaciteta telefona, določena iz naslova oglasa
- Cena: Cena telefona v evrih
- Kraj: Kraj, kjer prodajalec ponuja telefon
- Datum objave: Datum objave oglasa

NAMESTITEV IN ZAGON

- Na svoj računalnik si naloži Python verzije 3.9+
- Prestavi se v mapo TinaDujc_Seminarska_Naloga z ukazom cd TinaDujc_Seminarska_Naloga
- Ustvari virtualno okolje z ukazom python -m venv venv
- Zaženi virtualno okolje z ukazom source venv/bin/activate  #Na Windows: venv\\Scripts\\activate
- Namesti potrebne knjižnice z ukazom pip install -r requirements.txt

Sedaj ima uporabnik na voljo več možnosti:

1. Odprite analiza_podatkov.ipynb in poženite celice za pregled analize

2. Prenesite aktualne podatke iz interneta in jih uredite za analizo:
- z ukazom python pridobivanje_podatkov.py prenesete vsebino strani in jo shranite v mapo surovi_podatki
- z ukazom python priprava_podatkov.py to vsebino uredite in jo pretvorite v .json in .csv format

Če na novo prenesete vsebino in jo uredite ter poženete celice v Jupyter notebooku, se opisi rezultatov morda ne bodo popolnoma ujemali z vizualizacijami, saj se opisi nanašajo na podatke, ki so bili zbrani ob izdelavi te naloge, oglasi na strani pa se ves čas spreminjajo.

REZULTATI

Projekt omogoča:
- Vpogled v porazdelitev cen na trgu pametnih telefonov
- Primerjavo zastopanosti in cen med posameznimi znamkami
- Analizo povezave med shranjevalno kapaciteto in ceno telefona
- Primerjavo povprečnih cen po krajih

AVTOR

Tina Dujc


