"""
Scraper pro získávání rozvrhu z Bakalářů
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re
import json
import html


def scrape_rozvrh_kva():
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/22"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_pa():
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/2B"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_tb():
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/26"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_pb():
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/2C"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_sa():
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/28"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_sb():
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/29"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_ta():
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/25"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_kvb():
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/23"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_1w():
    """
    Získá rozvrh třídy 1W z Bakalářů
    """
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/1W"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_sxa():
    """
    Získá rozvrh třídy SXA z Bakalářů
    """
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/SXA"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_1a():
    """Získá rozvrh třídy 1.A z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/2A"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_kvia():
    """Získá rozvrh třídy KVIA z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/1Z"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_kvib():
    """Získá rozvrh třídy KVIB z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/20"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_2a():
    """Získá rozvrh třídy 2.A z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/27"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_sxb():
    """Získá rozvrh třídy SXB z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/1X"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_3a():
    """Získá rozvrh třídy 3.A z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/24"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_spta():
    """Získá rozvrh třídy SPTA z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/1T"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_sptb():
    """Získá rozvrh třídy SPTB z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/1U"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_4a():
    """Získá rozvrh třídy 4.A z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/21"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_okta():
    """Získá rozvrh třídy OKTA z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/1Q"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_oktb():
    """Získá rozvrh třídy OKTB z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/1R"
    return _scrape_rozvrh_generic(url)


def _scrape_rozvrh_generic(url):
    try:
        response = requests.get(url, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.content, 'html.parser')

        dnes = datetime.now()
        den_v_tydnu = dnes.weekday()
        aktualny_cas = dnes.hour * 60 + dnes.minute

        # Názvy dnů
        dny_nazvy = ['Pondělí', 'Úterý', 'Středa', 'Čtvrtek', 'Pátek', 'Sobota', 'Neděle']
        den_zkratky = ['po', 'út', 'st', 'čt', 'pá', 'so', 'ne']
        
        # Najdeme všechny hodiny na stránce
        hodiny_items = soup.find_all('div', class_='day-item-hover')
        
        # Parsujeme všechny hodiny z celého týdne
        vsechny_dny = {}  # {datum_str: {'den': 'Pondělí', 'datum': datetime, 'hodiny': []}}
        
        for hodina_div in hodiny_items:
            try:
                detail_json = hodina_div.get('data-detail', '{}')
                detail_json = html.unescape(detail_json)
                detail_data = json.loads(detail_json)
                subjecttext = detail_data.get('subjecttext', '')

                if not subjecttext:
                    continue

                teacher = detail_data.get('teacher', '')
                room = detail_data.get('room', '')
                theme = detail_data.get('theme', '')
                group = detail_data.get('group', '')

                parts = subjecttext.split('|')
                predmet = parts[0].strip() if len(parts) > 0 else ''

                if len(parts) > 2:
                    time_part = parts[2].strip()
                    match = re.search(r'(\d+[AB]?)\s*\((\d+:\d+)\s*-\s*(\d+:\d+)\)', time_part)
                    if match:
                        cislo_hodiny = match.group(1)
                        cas_od = match.group(2)
                        cas_do = match.group(3)
                        cas = f"{cas_od}-{cas_do}"

                        # Extrahujeme datum z subjecttext (např. "po 24.2.")
                        datum_match = re.search(r'(po|út|st|čt|pá)\s+(\d+)\.(\d+)\.', subjecttext)
                        if datum_match:
                            den_zkratka = datum_match.group(1)
                            den_cislo = int(datum_match.group(2))
                            mesic_cislo = int(datum_match.group(3))
                            rok = dnes.year
                            
                            # Vytvoříme datum
                            try:
                                datum_hodiny = datetime(rok, mesic_cislo, den_cislo)
                                datum_str = datum_hodiny.strftime('%Y-%m-%d')
                                
                                # Přidáme hodinu do správného dne
                                if datum_str not in vsechny_dny:
                                    den_index = den_zkratky.index(den_zkratka)
                                    vsechny_dny[datum_str] = {
                                        'den': dny_nazvy[den_index],
                                        'datum': datum_hodiny,
                                        'hodiny': []
                                    }
                                
                                hodina_info = {
                                    'cislo': cislo_hodiny,
                                    'cas': cas,
                                    'predmet': predmet,
                                    'ucitel': teacher,
                                    'mistnost': room,
                                    'tema': theme,
                                    'skupina': group
                                }
                                vsechny_dny[datum_str]['hodiny'].append(hodina_info)
                            except ValueError:
                                continue

            except (json.JSONDecodeError, KeyError, AttributeError):
                continue

        # Najdeme správný den k zobrazení
        den_k_zobrazeni = None
        datum_zobrazit = None
        den_nazev = None
        hodiny_list = []
        
        # Pokud je víkend, hledáme pondělí
        if den_v_tydnu >= 5:
            # Najdeme nejbližší pondělí
            for datum_str in sorted(vsechny_dny.keys()):
                datum = vsechny_dny[datum_str]['datum']
                if datum > dnes and datum.weekday() == 0:  # Pondělí
                    den_k_zobrazeni = vsechny_dny[datum_str]
                    datum_zobrazit = datum
                    den_nazev = 'Pondělí (příští týden)'
                    hodiny_list = den_k_zobrazeni['hodiny']
                    break
        else:
            # Zkusíme dnešní den
            dnes_str = dnes.strftime('%Y-%m-%d')
            if dnes_str in vsechny_dny:
                den_k_zobrazeni = vsechny_dny[dnes_str]
                hodiny_list = den_k_zobrazeni['hodiny']
                datum_zobrazit = dnes
                den_nazev = dny_nazvy[den_v_tydnu]
                
                # Zjistíme, jestli už poslední hodina skončila
                if hodiny_list:
                    posledni_hodina = max(hodiny_list, key=lambda x: x['cas'])
                    cas_match = re.search(r'-(\d+):(\d+)$', posledni_hodina['cas'])
                    if cas_match:
                        konec_hodiny = int(cas_match.group(1)) * 60 + int(cas_match.group(2))
                        if aktualny_cas > konec_hodiny:
                            # Hledáme zítřejší den
                            zitra = dnes + timedelta(days=1)
                            if zitra.weekday() == 5:  # Sobota -> pondělí
                                zitra = dnes + timedelta(days=3)
                            
                            zitra_str = zitra.strftime('%Y-%m-%d')
                            if zitra_str in vsechny_dny:
                                den_k_zobrazeni = vsechny_dny[zitra_str]
                                hodiny_list = den_k_zobrazeni['hodiny']
                                datum_zobrazit = zitra
                                den_nazev = f"{dny_nazvy[zitra.weekday()]} (zítřejší rozvrh)"
                            else:
                                # Data pro zítřek ještě nejsou dostupná
                                return {
                                    'den': f"{dny_nazvy[zitra.weekday()]} (zítřejší rozvrh)",
                                    'datum': zitra.strftime('%d.%m.%Y'),
                                    'hodiny': [],
                                    'data_nedostupna': True,
                                    'je_zitra': True
                                }
            else:
                # Dnešní den nemá data, hledáme nejbližší budoucí den
                for datum_str in sorted(vsechny_dny.keys()):
                    datum = vsechny_dny[datum_str]['datum']
                    if datum >= dnes:
                        den_k_zobrazeni = vsechny_dny[datum_str]
                        hodiny_list = den_k_zobrazeni['hodiny']
                        datum_zobrazit = datum
                        den_nazev = dny_nazvy[datum.weekday()]
                        break

        # Pokud jsme stále nic nenašli
        if not hodiny_list or datum_zobrazit is None:
            return {
                'den': dny_nazvy[den_v_tydnu if den_v_tydnu < 5 else 0],
                'datum': dnes.strftime('%d.%m.%Y'),
                'hodiny': [],
                'data_nedostupna': True,
                'je_zitra': False
            }

        # Seřadíme hodiny
        hodiny_list.sort(key=lambda x: x['cislo'])

        return {
            'den': den_nazev,
            'datum': datum_zobrazit.strftime('%d.%m.%Y'),
            'hodiny': hodiny_list,
            'data_nedostupna': False
        }

    except Exception as e:
        print(f"Chyba při scrapování rozvrhu: {e}")
        dnes = datetime.now()
        den_v_tydnu = dnes.weekday()
        dny_nazvy = ['Pondělí', 'Úterý', 'Středa', 'Čtvrtek', 'Pátek', 'Sobota', 'Neděle']

        return {
            'den': dny_nazvy[den_v_tydnu if den_v_tydnu < 5 else 0],
            'datum': dnes.strftime('%d.%m.%Y'),
            'hodiny': [],
            'data_nedostupna': True,
            'je_zitra': False
        }
