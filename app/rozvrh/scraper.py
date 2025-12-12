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
    url = "https://bakalari.mgo.cz/rozvrh/pb"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_sa():
    url = "https://bakalari.mgo.cz/rozvrh/sa"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_sb():
    url = "https://bakalari.mgo.cz/rozvrh/sb"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_ta():
    url = "https://bakalari.mgo.cz/rozvrh/ta"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_kvb():
    url = "https://bakalari.mgo.cz/rozvrh/kvb"
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
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/1A"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_kvia():
    """Získá rozvrh třídy KVIA z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/KVIA"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_kvib():
    """Získá rozvrh třídy KVIB z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/KVIB"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_2a():
    """Získá rozvrh třídy 2.A z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/2A"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_sxb():
    """Získá rozvrh třídy SXB z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/SXB"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_3a():
    """Získá rozvrh třídy 3.A z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/3A"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_spta():
    """Získá rozvrh třídy SPTA z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/SPTA"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_sptb():
    """Získá rozvrh třídy SPTB z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/SPTB"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_4a():
    """Získá rozvrh třídy 4.A z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/4A"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_okta():
    """Získá rozvrh třídy OKTA z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/OKTA"
    return _scrape_rozvrh_generic(url)


def scrape_rozvrh_oktb():
    """Získá rozvrh třídy OKTB z Bakalářů"""
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/OKTB"
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
        den_nazev = dny_nazvy[den_v_tydnu]
        datum_zobrazit = dnes

        # Pokud je víkend, zobrazíme pondělí
        if den_v_tydnu >= 5:
            den_v_tydnu = 0
            den_nazev = 'Pondělí (příští týden)'
            dny_do_pondeli = (7 - dnes.weekday()) if dnes.weekday() == 6 else 1
            datum_zobrazit = dnes + timedelta(days=dny_do_pondeli)

        hodiny_list = []

        # Najdeme všechny hodiny na stránce
        hodiny_items = soup.find_all('div', class_='day-item-hover')

        den_zkratky = ['po', 'út', 'st', 'čt', 'pá', 'so', 'ne']
        hledany_den = den_zkratky[den_v_tydnu if den_v_tydnu < 7 else 0]
        datum_den = datum_zobrazit.strftime('%d.%m.')
        hledany_pattern = f"{hledany_den} {datum_den.lstrip('0')}"

        for hodina_div in hodiny_items:
            try:
                detail_json = hodina_div.get('data-detail', '{}')
                detail_json = html.unescape(detail_json)
                detail_data = json.loads(detail_json)
                subjecttext = detail_data.get('subjecttext', '')

                if hledany_pattern not in subjecttext:
                    continue

                teacher = detail_data.get('teacher', '')
                room = detail_data.get('room', '')
                theme = detail_data.get('theme', '')
                group = detail_data.get('group', '')

                if subjecttext:
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

                            hodina_info = {
                                'cislo': cislo_hodiny,
                                'cas': cas,
                                'predmet': predmet,
                                'ucitel': teacher,
                                'mistnost': room,
                                'tema': theme,
                                'skupina': group
                            }
                            hodiny_list.append(hodina_info)

            except (json.JSONDecodeError, KeyError, AttributeError):
                continue

        hodiny_list.sort(key=lambda x: x['cislo'])

        je_po_posledni_hodine = False
        if hodiny_list:
            posledni_hodina = hodiny_list[-1]
            cas_match = re.search(r'-(\d+):(\d+)$', posledni_hodina['cas'])
            if cas_match:
                konec_hodiny = int(cas_match.group(1)) * 60 + int(cas_match.group(2))
                if aktualny_cas > konec_hodiny and den_v_tydnu < 5:
                    je_po_posledni_hodine = True

        if je_po_posledni_hodine:
            den_v_tydnu_zitra = (den_v_tydnu + 1) % 7
            datum_zitra = dnes + timedelta(days=1)
            if den_v_tydnu_zitra == 5:
                den_v_tydnu_zitra = 0
                datum_zitra = dnes + timedelta(days=3)

            den_nazev = dny_nazvy[den_v_tydnu_zitra]
            hledany_den = den_zkratky[den_v_tydnu_zitra]
            datum_den = datum_zitra.strftime('%d.%m.').lstrip('0')
            hledany_pattern = f"{hledany_den} {datum_den}"

            hodiny_list = []
            for hodina_div in hodiny_items:
                try:
                    detail_json = hodina_div.get('data-detail', '{}')
                    detail_json = html.unescape(detail_json)
                    detail_data = json.loads(detail_json)
                    subjecttext = detail_data.get('subjecttext', '')

                    if hledany_pattern not in subjecttext:
                        continue

                    teacher = detail_data.get('teacher', '')
                    room = detail_data.get('room', '')
                    theme = detail_data.get('theme', '')
                    group = detail_data.get('group', '')

                    if subjecttext:
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

                                hodina_info = {
                                    'cislo': cislo_hodiny,
                                    'cas': cas,
                                    'predmet': predmet,
                                    'ucitel': teacher,
                                    'mistnost': room,
                                    'tema': theme,
                                    'skupina': group
                                }
                                hodiny_list.append(hodina_info)

                except (json.JSONDecodeError, KeyError, AttributeError):
                    continue

            hodiny_list.sort(key=lambda x: x['cislo'])
            datum_zobrazit = datum_zitra

        if not hodiny_list:
            hodiny_list = [
                {'cislo': '1', 'cas': '8:15-9:00', 'predmet': 'Žádné hodiny', 'ucitel': '', 'mistnost': '', 'tema': '', 'skupina': ''}
            ]

        return {
            'den': den_nazev,
            'datum': datum_zobrazit.strftime('%d.%m.%Y'),
            'hodiny': hodiny_list
        }

    except Exception as e:
        print(f"Chyba při scrapování rozvrhu: {e}")
        dnes = datetime.now()
        den_v_tydnu = dnes.weekday()
        dny_nazvy = ['Pondělí', 'Úterý', 'Středa', 'Čtvrtek', 'Pátek', 'Sobota', 'Neděle']

        return {
            'den': dny_nazvy[den_v_tydnu if den_v_tydnu < 5 else 0],
            'datum': dnes.strftime('%d.%m.%Y'),
            'hodiny': [
                {'cislo': '1', 'cas': '8:15-9:00', 'predmet': 'Chyba při načítání', 'ucitel': '', 'mistnost': '', 'tema': '', 'skupina': ''}
            ]
        }
