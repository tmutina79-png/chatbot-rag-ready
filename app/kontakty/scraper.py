"""
Web scraper pro získání informací o vedení školy z webu MGO
"""
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional


def scrape_vedeni_skoly() -> List[Dict[str, str]]:
    """
    Načte informace o vedení školy z webu MGO
    
    Returns:
        List[Dict]: Seznam slovníků s informacemi o vedení
    """
    url = "https://mgo.cz/jj/kontakty/vedeni-a-sprava-skoly.html"
    
    try:
        # Načtení stránky
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        response.encoding = 'utf-8'
        
        # Parsování HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        vedeni_list = []
        
        # Struktura stránky:
        # Mgr. Vasevič Ladislav - ředitel školy - Telefon: 596 11 88 77, linka 103
        # PaedDr. Mohelník Karel - zástupce ředitele - Telefon: 596 11 62 38, linka 104
        # Mgr. Čeledová Platošová Zdeňka - zástupce ředitele - Telefon: 596 11 62 38, linka 102
        
        # Najdeme všechny odkazy na osoby v sekci vedení
        osoby_links = soup.find_all('a', href=lambda x: x and 'vedeni-a-sprava-skoly' in x and x.count('/') > 4)
        
        for link in osoby_links:
            text = link.get_text(strip=True)
            
            # Získáme další text za odkazem (pozice a telefon)
            parent = link.parent
            if parent:
                full_text = parent.get_text(strip=True)
                
                # Extrahujeme jméno
                jmeno = text
                
                # Extrahujeme pozici (text mezi jménem a "Telefon:")
                pozice = ""
                telefon = ""
                
                if "ředitel" in full_text.lower():
                    if "zástupce ředitele" in full_text.lower():
                        pozice = "Zástupce ředitele"
                    else:
                        pozice = "Ředitel školy"
                elif "ekonomka" in full_text.lower():
                    pozice = "Ekonomka"
                elif "sekretářka" in full_text.lower():
                    pozice = "Sekretářka"
                elif "školní metodik prevence" in full_text.lower():
                    pozice = "Školní metodik prevence"
                elif "výchovný poradce" in full_text.lower():
                    pozice = "Výchovný poradce"
                
                # Extrahujeme telefon
                if "Telefon:" in full_text:
                    telefon_part = full_text.split("Telefon:")[1].strip()
                    # Vezměme první část (číslo s linkou)
                    telefon = telefon_part.split()[0].replace(',', '')
                    if "linka" in telefon_part:
                        linka = telefon_part.split("linka")[1].strip().split()[0]
                        telefon = f"+420 {telefon}, linka {linka}"
                
                # Přidáme jen vedení školy (ředitel a zástupci)
                if pozice and ("ředitel" in pozice.lower() or "Zástupce" in pozice):
                    osoba_data = {
                        "jmeno": jmeno,
                        "pozice": pozice,
                        "email": "",  # Email není přímo na stránce u konkrétních osob
                        "telefon": telefon if telefon else "N/A"
                    }
                    vedeni_list.append(osoba_data)
        
        # Pokud se nepodařilo načíst data, použijeme fallback
        if not vedeni_list:
            return get_fallback_vedeni_data()
        
        return vedeni_list
        
    except requests.RequestException as e:
        print(f"Chyba při načítání stránky: {e}")
        return get_fallback_vedeni_data()
    except Exception as e:
        print(f"Neočekávaná chyba: {e}")
        return get_fallback_vedeni_data()


def get_fallback_vedeni_data() -> List[Dict[str, str]]:
    """
    Vrátí záložní data v případě, že scraping selže
    Aktuální data z webu MGO (k 7.12.2025)
    """
    return [
        {
            "jmeno": "Mgr. Vasevič Ladislav",
            "pozice": "Ředitel školy",
            "email": "",
            "telefon": "+420 596 11 88 77, linka 103"
        },
        {
            "jmeno": "PaedDr. Mohelník Karel",
            "pozice": "Zástupce ředitele",
            "email": "",
            "telefon": "+420 596 11 62 38, linka 104"
        },
        {
            "jmeno": "Mgr. Čeledová Platošová Zdeňka",
            "pozice": "Zástupce ředitele",
            "email": "",
            "telefon": "+420 596 11 62 38, linka 102"
        }
    ]


def format_vedeni_info(vedeni_data: List[Dict[str, str]]) -> str:
    """
    Naformátuje informace o vedení do textu
    """
    text = "👔 Vedení školy - Matiční gymnázium Ostrava\n\n"
    
    for osoba in vedeni_data:
        text += f"▪️ {osoba.get('jmeno', 'N/A')}\n"
        text += f"   Pozice: {osoba.get('pozice', 'N/A')}\n"
        if osoba.get('email'):
            text += f"   📧 Email: {osoba.get('email')}\n"
        if osoba.get('telefon'):
            text += f"   📞 Telefon: {osoba.get('telefon')}\n"
        text += "\n"
    
    return text


def scrape_ucitele_pedagogicky_sbor() -> List[Dict[str, str]]:
    """
    Načte informace o všech učitelích z pedagogického sboru.
    Vrací seznam učitelů s jejich aprobací, kontakty atd.
    """
    url = "https://mgo.cz/jj/kontakty/pedagogickysbor.html"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        response.encoding = 'utf-8'
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        ucitele_data = []
        
        # Najdeme tabulku s učiteli
        table = soup.find('table')
        if not table:
            return get_fallback_ucitele_data()
        
        rows = table.find_all('tr')[1:]  # Přeskočíme hlavičku
        
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 5:
                jmeno = cols[0].get_text(strip=True)
                aprobace = cols[1].get_text(strip=True)
                mistnost = cols[2].get_text(strip=True)
                
                # Pokusíme se extrahovat email
                email_cell = cols[3]
                email = email_cell.get_text(strip=True)
                
                # Pokud je email skrytý JavaScriptem, zkusíme extrahovat z atributů nebo použít fallback
                if "chráněna před spamboty" in email or not email or "@" not in email:
                    # Zkusíme najít email link
                    email_link = email_cell.find('a', href=True)
                    if email_link and 'mailto:' in email_link.get('href', ''):
                        email = email_link.get('href').replace('mailto:', '')
                    else:
                        # Vytvoříme email podle vzoru prijmeni@mgo.cz
                        # Extrahujeme příjmení z celého jména (ignorujeme tituly)
                        parts = jmeno.split()
                        prijmeni = ""
                        
                        # Najdeme příjmení - je to obvykle slovo před křestním jménem
                        # Formát: "Titul Příjmení Jméno" nebo "Mgr. Příjmení Jméno"
                        for i, part in enumerate(parts):
                            # Přeskočíme tituly (obsahují tečku nebo jsou krátké zkratky)
                            if '.' not in part and len(part) > 2:
                                # Pokud následuje další slovo bez tečky, první je příjmení
                                if i + 1 < len(parts) and '.' not in parts[i + 1]:
                                    prijmeni = part
                                    break
                                # Jinak je to poslední "normální" slovo
                                prijmeni = part
                        
                        if prijmeni:
                            # Odstraníme speciální znaky a diakritiku z příjmení
                            prijmeni = prijmeni.lower().replace(',', '').replace('.', '')
                            # Odstranění diakritiky
                            prijmeni = (prijmeni
                                .replace('á', 'a').replace('č', 'c').replace('ď', 'd')
                                .replace('é', 'e').replace('ě', 'e').replace('í', 'i')
                                .replace('ň', 'n').replace('ó', 'o').replace('ř', 'r')
                                .replace('š', 's').replace('ť', 't').replace('ú', 'u')
                                .replace('ů', 'u').replace('ý', 'y').replace('ž', 'z'))
                            email = f"{prijmeni}@mgo.cz"
                        else:
                            email = "N/A"
                
                konzultace = cols[4].get_text(strip=True)
                
                if jmeno:  # Kontrola, že máme alespoň jméno
                    ucitele_data.append({
                        "jmeno": jmeno,
                        "aprobace": aprobace,
                        "klapka": mistnost,
                        "email": email,
                        "konzultace": konzultace
                    })
        
        if not ucitele_data:
            return get_fallback_ucitele_data()
        
        return ucitele_data
        
    except requests.RequestException as e:
        print(f"Chyba při načítání dat učitelů: {e}")
        return get_fallback_ucitele_data()
    except Exception as e:
        print(f"Neočekávaná chyba při načítání učitelů: {e}")
        return get_fallback_ucitele_data()


def filter_ucitele_by_predmet(predmet_zkratka: str) -> List[Dict[str, str]]:
    """
    Filtruje učitele podle zkratky předmětu.
    
    Args:
        predmet_zkratka: Zkratka předmětu (např. 'M', 'Čj', 'Aj')
    
    Returns:
        Seznam učitelů, kteří učí daný předmět
    """
    ucitele = scrape_ucitele_pedagogicky_sbor()
    
    # Normalizace zkratky předmětu pro porovnání
    predmet_zkratka_lower = predmet_zkratka.lower()
    
    filtered_ucitele = []
    for ucitel in ucitele:
        aprobace = ucitel.get('aprobace', '')
        # Rozdělíme aprobaci na jednotlivé předměty (oddělené čárkou)
        predmety = [p.strip() for p in aprobace.split(',')]
        
        # Kontrolujeme, zda učitel učí hledaný předmět
        for p in predmety:
            if p.lower() == predmet_zkratka_lower:
                filtered_ucitele.append(ucitel)
                break
    
    return filtered_ucitele


def get_predmet_zkratka(predmet_nazev: str) -> str:
    """
    Převede název předmětu na zkratku používanou v aprobaci.
    """
    mapping = {
        # Jazyky
        'cestina': 'Čj',
        'cj': 'Čj',
        'matematika': 'M',
        'm': 'M',
        'anglictina': 'Aj',
        'aj': 'Aj',
        'nemcina': 'Nj',
        'nj': 'Nj',
        'spanelstina': 'Šj',
        'sj': 'Šj',
        'francouzstina': 'Fj',
        'fj': 'Fj',
        'rustina': 'Rj',
        'rj': 'Rj',
        'latina': 'La',
        'la': 'La',
        # Přírodní vědy
        'fyzika': 'F',
        'f': 'F',
        'chemie': 'Ch',
        'ch': 'Ch',
        'biologie': 'Bi',
        'bi': 'Bi',
        # Společenské vědy
        'dejepis': 'D',
        'd': 'D',
        'zemepis': 'Z',
        'z': 'Z',
        'zsv': 'ZSV',
        'ov': 'Ov',
        'obcanska-vychova': 'Ov',
        'eks': 'EKS',
        # IT a umění
        'informatika': 'IVT',
        'ivt': 'IVT',
        'tv': 'Tv',
        'telesna-vychova': 'Tv',
        'hv': 'Hv',
        'hudebni-vychova': 'Hv',
        'vv': 'Vv',
        'vytvarnavychova': 'Vv'
    }
    return mapping.get(predmet_nazev.lower(), '')


def get_fallback_ucitele_data() -> List[Dict[str, str]]:
    """
    Vrátí záložní data učitelů v případě selhání scrapingu.
    """
    return [
        {
            "jmeno": "Data nejsou dostupná",
            "aprobace": "",
            "klapka": "",
            "email": "",
            "konzultace": ""
        }
    ]


def search_ucitele_by_name(search_query: str) -> List[Dict[str, str]]:
    """
    Vyhledá učitele podle jména nebo příjmení (bez diakritiky).
    
    Args:
        search_query: Hledané jméno/příjmení
    
    Returns:
        Seznam nalezených učitelů
    """
    def remove_diacritics(text: str) -> str:
        """Odstraní diakritiku z textu"""
        text = text.lower()
        replacements = {
            'á': 'a', 'č': 'c', 'ď': 'd', 'é': 'e', 'ě': 'e', 'í': 'i',
            'ň': 'n', 'ó': 'o', 'ř': 'r', 'š': 's', 'ť': 't', 'ú': 'u',
            'ů': 'u', 'ý': 'y', 'ž': 'z'
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text
    
    def clean_name_part(text: str) -> str:
        """Odstraní interpunkci a speciální znaky z jména"""
        # Odstraníme tečky, čárky a další interpunkci
        return text.replace('.', '').replace(',', '').strip()
    
    ucitele = scrape_ucitele_pedagogicky_sbor()
    
    # Normalizace hledaného dotazu
    search_normalized = remove_diacritics(search_query.strip())
    
    found_ucitele = []
    for ucitel in ucitele:
        jmeno = ucitel.get('jmeno', '')
        
        # Rozdělíme jméno na části, ale nejdřív odstraníme interpunkci
        jmeno_cleaned = jmeno.replace('.', ' ').replace(',', ' ')
        jmeno_parts = jmeno_cleaned.split()
        
        # Kontrolujeme každou část jména
        for part in jmeno_parts:
            if not part:  # Přeskočíme prázdné části
                continue
            part_normalized = remove_diacritics(part.strip())
            # Musí se shodovat celé slovo (kvůli požadavku uživatele)
            if part_normalized == search_normalized:
                found_ucitele.append(ucitel)
                break
    
    return found_ucitele


def format_ucitele_info(ucitele_data: List[Dict[str, str]], predmet_nazev: str = "") -> str:
    """
    Naformátuje informace o učitelích do textu.
    
    Args:
        ucitele_data: Seznam učitelů
        predmet_nazev: Název předmětu (pro nadpis)
    """
    if not ucitele_data:
        return f"📚 {predmet_nazev}\n\nNenalezeni žádní učitelé pro tento předmět."
    
    text = f"📚 {predmet_nazev} - Vyučující\n\n"
    
    for ucitel in ucitele_data:
        text += f"▪️ {ucitel.get('jmeno', 'N/A')}\n"
        if ucitel.get('aprobace'):
            text += f"   Aprobace: {ucitel.get('aprobace')}\n"
        if ucitel.get('klapka'):
            text += f"   ☎️ Klapka: {ucitel.get('klapka')}\n"
        if ucitel.get('email'):
            text += f"   📧 Email: {ucitel.get('email')}\n"
        if ucitel.get('konzultace'):
            text += f"   🕐 Konzultační hodiny: {ucitel.get('konzultace')}\n"
        text += "\n"
    
    return text
