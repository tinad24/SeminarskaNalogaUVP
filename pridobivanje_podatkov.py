import requests
import os
import time
import random

def main():
    for stran in range(1, 36):
        try:
            pridobi_html_kodo(stran)
        except Exception as e:
            print("Prišlo je do napake pri prenosu strani " + str(stran) + ": " + str(e))


def pridobi_html_kodo(stran):
    mapa = './surovi_podatki'
    if not os.path.exists(mapa):
        os.makedirs(mapa)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'sl-SI,sl;q=0.9,en;q=0.8',
    }

    url = 'https://www.bolha.com/pametni-mobilni-telefoni?page=' + str(stran)
    odgovor = requests.get(url, headers=headers)

    dokument = os.path.join(mapa, 'stran_' + str(stran) + '.html')
    with open(dokument, 'w', encoding='utf-8') as f:
        f.write(odgovor.text)

    print("Prenesena stran " + str(stran))
    time.sleep(random.uniform(1, 2))  

if __name__ == "__main__":
    main()
