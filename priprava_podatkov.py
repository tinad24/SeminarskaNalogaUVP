from bs4 import BeautifulSoup
import os
import re
import json
import csv

ZNAMKE = {
    "iphone": "Apple",
    "apple": "Apple",
    "samsung": "Samsung",
    "galaxy": "Samsung",
    "xiaomi": "Xiaomi",
    "redmi": "Xiaomi",
    "poco": "Xiaomi",
    "huawei": "Huawei",
    "honor": "Honor",
    "oneplus": "OnePlus",
    "google": "Google",
    "pixel": "Google",
    "nokia": "Nokia",
    "motorola": "Motorola",
    "sony": "Sony",
    "oppo": "Oppo",
    "realme": "Realme",
    "asus": "Asus",
    "vivo": "Vivo",
}


def main():
    try:
        vsi_oglasi = izberi_vse_oglase()
        urejeni_oglasi = uredi_podatke_oglasov(vsi_oglasi)
        shrani_podatke(urejeni_oglasi)
    except Exception as e:
        print("Prišlo je do napake pri urejanju podatkov: " + str(e))


def izberi_vse_oglase():
    vsi_oglasi = []
    for stran in os.listdir('./surovi_podatki'):
        with open('./surovi_podatki/' + stran, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            # med rezultati so poleg pravih oglasov o telefonih vmešani tudi
            # oglaševani "SuperVau" oglasi (brez cene/lokacije, ponavljajo se)
            # in "Latest" oglasi (novi oglasi iz čisto drugih kategorij), zato
            # vzamemo le prave oglase iz skupin Regular in VauVau
            elementi = soup.find_all('li', class_=['EntityList-item--Regular', 'EntityList-item--VauVau'])
            for element in elementi:
                oglas = element.find('article', class_='entity-body')
                if oglas is not None:
                    vsi_oglasi.append(oglas)
    return vsi_oglasi


def uredi_podatke_oglasov(vsi_oglasi):
    seznam_telefonov = []
    ze_dodani_oglasi = set()
    for oglas in vsi_oglasi:
        naslov_element = oglas.find('h3', class_='entity-title')
        if naslov_element is None:
            continue
        naslov_oglasa = naslov_element.get_text(strip=True)

        # med oglasi za prodajo telefonov se najde tudi kar nekaj oglasov, kjer
        # nekdo telefon išče oz. odkupuje - te oglase izpustimo, saj njihova
        # "cena" ni prodajna cena telefona
        naslov_male_crke = naslov_oglasa.lower()
        if "odkup" in naslov_male_crke or "kupim" in naslov_male_crke:
            continue

        znamka = najdi_znamko(naslov_oglasa)
        kapaciteta_gb = najdi_kapaciteto(naslov_oglasa)

        cena_element = oglas.find('div', class_='entity-prices')
        cena = uredi_ceno(cena_element.get_text(strip=True) if cena_element else "")

        kraj_element = oglas.find('div', class_='entity-description')
        kraj = uredi_kraj(kraj_element.get_text(strip=True) if kraj_element else "")

        datum_element = oglas.find('time')
        datum_objave = datum_element.get_text(strip=True).rstrip('.') if datum_element else "Brez podatka"

        # nekateri (predvsem izpostavljeni) oglasi se med stranmi ponovijo, zato jih preskočimo
        oznaka_oglasa = (naslov_oglasa, kraj, datum_objave)
        if oznaka_oglasa in ze_dodani_oglasi:
            continue
        ze_dodani_oglasi.add(oznaka_oglasa)

        telefon = {
            "naslov_oglasa": naslov_oglasa,
            "znamka": znamka,
            "kapaciteta_gb": kapaciteta_gb,
            "cena": cena,
            "kraj": kraj,
            "datum_objave": datum_objave,
        }
        seznam_telefonov.append(telefon)
    return seznam_telefonov


def najdi_znamko(naslov_oglasa):
    naslov_male_crke = naslov_oglasa.lower()
    for kljucna_beseda, znamka in ZNAMKE.items():
        if kljucna_beseda in naslov_male_crke:
            return znamka
    return "Drugo"


def najdi_kapaciteto(naslov_oglasa):
    # v naslovu poiščemo številke, ki jim sledi "GB" (npr. 128GB, 256 GB)
    najdene_kapacitete = re.findall(r'(\d{2,4})\s*GB', naslov_oglasa, re.IGNORECASE)
    if not najdene_kapacitete:
        return None
    return max(int(vrednost) for vrednost in najdene_kapacitete)


def uredi_ceno(besedilo_cene):
    if "dogovoru" in besedilo_cene.lower() or besedilo_cene == "":
        return None
    besedilo_cene = besedilo_cene.replace("€", "").strip()
    besedilo_cene = besedilo_cene.replace(".", "").replace(",", ".")
    try:
        cena = float(besedilo_cene)
    except ValueError:
        return None
    if cena == 0:
        return None
    return cena


def uredi_kraj(besedilo_kraja):
    besedilo_kraja = besedilo_kraja.replace("Lokacija:", "").strip()
    if besedilo_kraja == "":
        return "Brez podatka"
    return besedilo_kraja.split(",")[0].strip()


def shrani_podatke(urejeni_oglasi):
    with open('podatki_telefonov.json', 'w', encoding='utf-8') as f:
        json.dump(urejeni_oglasi, f, ensure_ascii=False, indent=2)

    with open('podatki_telefonov.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Naslov oglasa", "Znamka", "Kapaciteta (GB)", "Cena", "Kraj", "Datum objave"])
        for telefon in urejeni_oglasi:
            writer.writerow([
                telefon["naslov_oglasa"],
                telefon["znamka"],
                telefon["kapaciteta_gb"],
                telefon["cena"],
                telefon["kraj"],
                telefon["datum_objave"],
            ])


if __name__ == "__main__":
    main()
