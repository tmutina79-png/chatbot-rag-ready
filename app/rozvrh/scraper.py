"""
Scraper pro získávání rozvrhu z Bakalářů
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json
import html

def scrape_rozvrh_kva():
    """
    Načte rozvrh třídy KVA z Bakalářů a vrátí rozvrh pro dnešní den
    
    Returns:
        dict: Obsahuje den, datum a seznam hodin
    """
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/22"
    return _scrape_rozvrh_generic(url)

def scrape_rozvrh_pa():
    """
    Načte rozvrh třídy PA z Bakalářů a vrátí rozvrh pro dnešní den
    
    Returns:
        dict: Obsahuje den, datum a seznam hodin
    """
    url = "https://mgo.bakalari.cz/bakaweb/Timetable/Public/Actual/Class/2B"
    return _scrape_rozvrh_generic(url)

def _scrape_rozvrh_generic(url):
    
    try:
        response = requests.get(url, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Zjistíme dnešní den v týdnu (0=pondělí, 6=neděle)
        dnes = datetime.now()
        den_v_tydnu = dnes.weekday()
        
        # Názvy dnů
        dny_nazvy = ['Pondělí', 'Úterý', 'Středa', 'Čtvrtek', 'Pátek', 'Sobota', 'Neděle']
        den_nazev = dny_nazvy[den_v_tydnu]
        
        # Pokud je víkend, zobrazíme pondělí (index 0)
        if den_v_tydnu >= 5:
            den_v_tydnu = 0
            den_nazev = 'Pondělí (příští týden)'
        
        hodiny_list = []
        
        # Najdeme všechny hodiny na stránce
        hodiny_items = soup.find_all('div', class_='day-item-hover')
        
        # Dnes je např. pondělí 8.12., takže hledáme hodiny s "po 8.12." v subjecttext
        den_zkratky = ['po', 'út', 'st', 'čt', 'pá', 'so', 'ne']
        hledany_den = den_zkratky[den_v_tydnu if den_v_tydnu < 7 else 0]
        datum_den = dnes.strftime('%d.%m.')  # Formát: "8.12."
        hledany_pattern = f"{hledany_den} {datum_den.lstrip('0')}"  # Např. "po 8.12."
        
        for hodina_div in hodiny_items:
            try:
                # Získáme JSON data z data-detail atributu
                detail_json = hodina_div.get('data-detail', '{}')
                
                # Dekódujeme HTML entity a parsujeme JSON
                detail_json = html.unescape(detail_json)
                detail_data = json.loads(detail_json)
                
                # Extrahujeme informace
                subjecttext = detail_data.get('subjecttext', '')
                
                # Kontrola, zda patří k dnešnímu dni
                if hledany_pattern not in subjecttext:
                    continue
                
                teacher = detail_data.get('teacher', '')
                room = detail_data.get('room', '')
                theme = detail_data.get('theme', '')
                group = detail_data.get('group', '')
                
                # Parsujeme subjecttext pro získání předmětu a času
                # Formát: "Český jazyk a literatura | po 8.12. | 1 (8:15 - 9:00)"
                if subjecttext:
                    parts = subjecttext.split('|')
                    predmet = parts[0].strip() if len(parts) > 0 else ''
                    
                    # Extrahujeme číslo hodiny a čas
                    if len(parts) > 2:
                        time_part = parts[2].strip()
                        # Hledáme číslo hodiny a čas
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
            
            except (json.JSONDecodeError, KeyError, AttributeError) as e:
                continue
        
        # Seřadíme hodiny podle čísla
        hodiny_list.sort(key=lambda x: x['cislo'])
        
        # Pokud nemáme žádné hodiny, použijeme fallback
        if not hodiny_list:
            hodiny_list = [
                {'cislo': '1', 'cas': '8:15-9:00', 'predmet': 'Žádné hodiny', 'ucitel': '', 'mistnost': '', 'tema': '', 'skupina': ''}
            ]
        
        return {
            'den': den_nazev,
            'datum': dnes.strftime('%d.%m.%Y'),
            'hodiny': hodiny_list
        }
        
    except Exception as e:
        print(f"Chyba při scrapování rozvrhu: {e}")
        # V případě chyby vrátíme ukázkový rozvrh
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
