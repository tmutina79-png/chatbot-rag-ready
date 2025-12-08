"""
Modul pro scraping informací o jídelně z webu obědů
"""
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
from datetime import datetime, date, timedelta
import re


def get_working_days_until_friday() -> List[date]:
    """
    Vrátí seznam pracovních dnů od dneška do nejbližšího pátku (včetně)
    
    Returns:
        List datumů od dneška do pátku
    """
    today = date.today()
    days = []
    current_day = today
    
    # Pokud je sobota nebo neděle, začneme od pondělí
    if current_day.weekday() == 5:  # Sobota
        current_day = today + timedelta(days=2)
    elif current_day.weekday() == 6:  # Neděle
        current_day = today + timedelta(days=1)
    
    # Přidáváme dny až do pátku (včetně)
    while current_day.weekday() <= 4:  # 0=pondělí, 4=pátek
        days.append(current_day)
        if current_day.weekday() == 4:  # Pátek
            break
        current_day += timedelta(days=1)
    
    return days


def scrape_dnesni_menu() -> Dict:
    """
    Stáhne a parsuje dnešní jídelníček ze stránky obedy.zs-mat5.cz
    
    Returns:
        Dict s informacemi o dnešním menu
    """
    try:
        url = "http://obedy.zs-mat5.cz/login"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        dnesni_datum = date.today()
        dnesni_menu = []
        
        # Hledáme dnešní datum ve formátu "DD.MM.YYYY"
        den_nazvy = ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek", "Sobota", "Neděle"]
        dnesni_den_nazev = den_nazvy[dnesni_datum.weekday()]
        dnesni_datum_str = f"{dnesni_datum.day}.{dnesni_datum.month}.{dnesni_datum.year}"
        
        print(f"🔍 Hledám menu pro: {dnesni_den_nazev} {dnesni_datum_str}")
        print(f"📅 Hledané varianty: {dnesni_datum.day:02d}.{dnesni_datum.month:02d}.{dnesni_datum.year}")
        
        # Najdeme div s dnešním datem (třída je 'jidelnicekTop')
        date_divs = soup.find_all('div', class_='jidelnicekTop')
        target_date_div = None
        
        print(f"📋 Nalezeno {len(date_divs)} divů s třídou 'jidelnicekTop'")
        
        for div in date_divs:
            div_text = div.get_text()
            # Pokud obsahuje datum
            if f"{dnesni_datum.day:02d}.{dnesni_datum.month:02d}.{dnesni_datum.year}" in div_text:
                target_date_div = div
                print(f"✅ Nalezen div s dnešním datem!")
                break
        
        if not target_date_div:
            print(f"⚠️ Dnešní datum nenalezeno na stránce")
            dnesni_menu = [
                {"typ": "Oběd 1", "nazev": "Menu pro dnešní den není k dispozici."},
                {"typ": "Oběd 2", "nazev": "Menu pro dnešní den není k dispozici."},
                {"typ": "BL (bezlepková varianta)", "nazev": "Menu pro dnešní den není k dispozici."}
            ]
        else:
            # Najdeme následující article element po tomto divu (všechny obědy jsou v jednom article)
            article = None
            
            for sibling in target_date_div.find_all_next():
                if sibling.name == 'div' and 'jidelnicekTop' in sibling.get('class', []):
                    break
                if sibling.name == 'article':
                    article = sibling
                    break
            
            if not article:
                print(f"⚠️ Nebyl nalezen article element pro dnešní den")
                dnesni_menu = [
                    {"typ": "Oběd 1", "nazev": "Menu pro dnešní den není k dispozici."},
                    {"typ": "Oběd 2", "nazev": "Menu pro dnešní den není k dispozici."},
                    {"typ": "BL (bezlepková varianta)", "nazev": "Menu pro dnešní den není k dispozici."}
                ]
            else:
                print(f"📦 Nalezen article element, zpracovávám všechny containery...")
                
                # V článku najdeme všechny containery (každý container = jeden typ obědu)
                containers = article.find_all('div', class_='container')
                print(f"📦 Nalezeno {len(containers)} containerů")
                
                processed_types = set()
                
                for container in containers:
                    container_text = container.get_text()
                    
                    # Najdeme typ obědu
                    typ_obedu = None
                    typ_raw = None
                    if 'Oběd 1d' in container_text:
                        continue  # Přeskočíme duplicitu
                    elif 'Oběd 1' in container_text and 'Oběd 1' not in processed_types:
                        typ_obedu = "Oběd 1"
                        typ_raw = "Oběd 1"
                    elif 'Oběd 2d' in container_text:
                        continue  # Přeskočíme duplicitu
                    elif 'Oběd 2' in container_text and 'Oběd 2' not in processed_types:
                        typ_obedu = "Oběd 2"
                        typ_raw = "Oběd 2"
                    elif 'Oběd BLd' in container_text:
                        continue  # Přeskočíme duplicitu
                    elif 'Oběd BL' in container_text and 'BL' not in processed_types:
                        typ_obedu = "BL (bezlepková varianta)"
                        typ_raw = "BL"
                    
                    # Zkontrolujeme, zda je označeno jako "Matiční"
                    je_maticni = 'Matiční' in container_text
                    
                    if typ_obedu and je_maticni and typ_obedu not in processed_types:
                        # Extrahujeme jídla z column divů
                        column_divs = container.find_all('div', class_='column')
                        
                        jidla = []
                        for col_div in column_divs:
                            text = col_div.get_text()
                            text_clean = re.sub(r'\s+', ' ', text).strip()
                            items = [item.strip() for item in text_clean.split(',')]
                            
                            for item in items:
                                item_clean = re.sub(r'\s*\([0-9,]*\)?\s*$', '', item).strip()
                                
                                if (item_clean and 
                                    len(item_clean) > 3 and
                                    item_clean.lower() not in [j.lower() for j in jidla] and
                                    item_clean not in ['Matiční', 'Maticni', 'Oběd 1', 'Oběd 2', 'Oběd BL']):
                                    jidla.append(item_clean)
                                    if len(jidla) >= 7:
                                        break
                            
                            if len(jidla) >= 7:
                                break
                        
                        menu_text = ', '.join(jidla[:7]) if jidla else "Informace o jídle není dostupná"
                        
                        dnesni_menu.append({
                            "typ": typ_obedu,
                            "nazev": menu_text
                        })
                        
                        processed_types.add(typ_obedu)
                        print(f"✅ {typ_obedu}: {menu_text[:60]}...")
        
        # Seřadíme podle typu
        poradi = {"Oběd 1": 1, "Oběd 2": 2, "BL (bezlepková varianta)": 3}
        dnesni_menu.sort(key=lambda x: poradi.get(x["typ"], 99))
        
        # Pokud máme méně než 3 položky, doplníme chybějící
        existing_types = {item["typ"] for item in dnesni_menu}
        all_types = ["Oběd 1", "Oběd 2", "BL (bezlepková varianta)"]
        
        for typ in all_types:
            if typ not in existing_types:
                dnesni_menu.append({
                    "typ": typ,
                    "nazev": "Není k dispozici"
                })
        
        # Znovu seřadíme
        dnesni_menu.sort(key=lambda x: poradi.get(x["typ"], 99))
        
        return {
            "datum": dnesni_datum.strftime("%d.%m.%Y"),
            "den": dnesni_den_nazev,
            "menu": dnesni_menu
        }
        
    except Exception as e:
        print(f"❌ Chyba při scrapování dnešního menu: {e}")
        import traceback
        traceback.print_exc()
        return {
            "error": str(e),
            "datum": date.today().strftime("%d.%m.%Y"),
            "menu": [{
                "typ": "Chyba",
                "nazev": f"Nepodařilo se načíst menu: {str(e)}"
            }]
        }


def scrape_tydenni_menu() -> Dict:
    """
    Stáhne a parsuje týdenní jídelníček ze stránky obedy.zs-mat5.cz
    Zobrazuje pouze dny od dneška do pátku (včetně)
    
    Returns:
        Dict s informacemi o týdenním menu
    """
    try:
        url = "http://obedy.zs-mat5.cz/login"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Získáme seznam dnů od dneška do pátku
        working_days = get_working_days_until_friday()
        
        tydenni_menu = []
        den_nazvy = ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek", "Sobota", "Neděle"]
        
        # Najdeme všechny sekce s datem
        all_date_divs = soup.find_all('div', class_='jidelnicekTop')
        
        print(f"📅 Načítám týdenní menu...")
        
        # Pro každý pracovní den hledáme odpovídající sekci
        for den_datum in working_days:
            den_nazev = den_nazvy[den_datum.weekday()]
            date_pattern = f"{den_datum.day:02d}.{den_datum.month:02d}.{den_datum.year}"
            
            menu_pro_den = []
            target_date_div = None
            
            # Najdeme div s tímto datem
            for date_div in all_date_divs:
                if date_pattern in date_div.get_text():
                    target_date_div = date_div
                    break
            
            if target_date_div:
                # Najdeme následující article (všechny obědy jsou v jednom article)
                article = None
                for sibling in target_date_div.find_all_next():
                    if sibling.name == 'div' and 'jidelnicekTop' in sibling.get('class', []):
                        break
                    if sibling.name == 'article':
                        article = sibling
                        break
                
                if article:
                    # V článku najdeme všechny containery
                    containers = article.find_all('div', class_='container')
                    
                    processed_types = set()
                    for container in containers:
                        container_text = container.get_text()
                        
                        typ_obedu = None
                        if 'Oběd 1d' in container_text:
                            continue
                        elif 'Oběd 1' in container_text and 'Oběd 1' not in processed_types:
                            typ_obedu = "Oběd 1"
                        elif 'Oběd 2d' in container_text:
                            continue
                        elif 'Oběd 2' in container_text and 'Oběd 2' not in processed_types:
                            typ_obedu = "Oběd 2"
                        elif 'Oběd BLd' in container_text:
                            continue
                        elif 'Oběd BL' in container_text and 'BL' not in processed_types:
                            typ_obedu = "BL"
                        
                        je_maticni = 'Matiční' in container_text
                        
                        if typ_obedu and je_maticni and typ_obedu not in processed_types:
                            column_divs = container.find_all('div', class_='column')
                            
                            jidla = []
                            for col_div in column_divs:
                                text = col_div.get_text()
                                text_clean = re.sub(r'\s+', ' ', text).strip()
                                items = [item.strip() for item in text_clean.split(',')]
                                
                                for item in items:
                                    item_clean = re.sub(r'\s*\([0-9,]*\)?\s*$', '', item).strip()
                                    
                                    if (item_clean and 
                                        len(item_clean) > 3 and
                                        item_clean.lower() not in [j.lower() for j in jidla] and
                                        item_clean not in ['Matiční', 'Maticni', 'Oběd 1', 'Oběd 2', 'Oběd BL']):
                                        jidla.append(item_clean)
                                        if len(jidla) >= 7:
                                            break
                                
                                if len(jidla) >= 7:
                                    break
                            
                            menu_text = ', '.join(jidla[:7]) if jidla else "Informace není dostupná"
                            
                            menu_pro_den.append({
                                "typ": typ_obedu,
                                "nazev": menu_text
                            })
                            
                            processed_types.add(typ_obedu)
            
            # Přidáme den do výsledku
            den_formatted = den_datum.strftime("%d.%m.%Y")
            if menu_pro_den:
                tydenni_menu.append({
                    "den": f"{den_nazev} {den_formatted}",
                    "datum": den_formatted,
                    "menu": menu_pro_den
                })
            else:
                tydenni_menu.append({
                    "den": f"{den_nazev} {den_formatted}",
                    "datum": den_formatted,
                    "menu": [{"typ": "Info", "nazev": "Menu není k dispozici"}]
                })
        
        # Pokud nemáme žádné dny
        if not tydenni_menu:
            tydenni_menu.append({
                "den": "Informace",
                "datum": date.today().strftime("%d.%m.%Y"),
                "menu": [{"typ": "Info", "nazev": "Momentálně není k dispozici jídelníček pro nadcházející dny."}]
            })
        
        print(f"✅ Načteno menu pro {len(tydenni_menu)} dnů")
        
        return {
            "tyden": f"Jídelníček od {working_days[0].strftime('%d.%m.')} do pátku" if working_days else "Aktuální týden",
            "dny": tydenni_menu
        }
        
    except Exception as e:
        print(f"❌ Chyba při scrapování týdenního menu: {e}")
        import traceback
        traceback.print_exc()
        return {
            "error": str(e),
            "dny": []
        }


def get_jidelna_info() -> Dict:
    """
    Vrací základní informace o jídelně
    
    Returns:
        Dict se základními informacemi
    """
    return {
        "nazev": "Školní jídelna MGO",
        "adresa": "Matiční gymnázium Ostrava",
        "kontakt": "info@mgo.cz",
        "telefon": "+420 596 136 632",
        "provozni_doba": {
            "pondeli_patek": "11:00 - 14:00",
            "vikend": "Zavřeno"
        }
    }


def format_jidelnicek_info(jidelnicek: Dict) -> str:
    """
    Formátuje informace o jídelníčku do čitelného textu
    
    Args:
        jidelnicek: Dictionary s informacemi o jídelníčku
        
    Returns:
        Formátovaný string s informacemi
    """
    if "error" in jidelnicek:
        return f"❌ Nepodařilo se načíst jídelníček: {jidelnicek['error']}"
    
    output = "🍽️ Školní jídelna MGO\n\n"
    
    if jidelnicek.get("dnesni_menu"):
        output += "📅 Dnešní menu:\n"
        for item in jidelnicek["dnesni_menu"]:
            output += f"  • {item}\n"
    else:
        output += "📅 Dnešní menu zatím není k dispozici.\n"
    
    output += "\n💡 Pro více informací navštivte web školy."
    
    return output
