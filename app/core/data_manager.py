"""
Data Manager - Načítání dat z JSON databáze
Fallback, když scraping nefunguje nebo je server offline
"""

import json
import os
from typing import Dict, List, Optional
from datetime import datetime

class DataManager:
    """Spravuje lokální databázi školních dat"""
    
    def __init__(self, data_file: str = "data/skolni_data.json"):
        self.data_file = data_file
        self.data = self._load_data()
    
    def _load_data(self) -> Dict:
        """Načte data z JSON souboru"""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"⚠️  Varování: Soubor {self.data_file} nenalezen!")
            return self._get_default_data()
        except json.JSONDecodeError as e:
            print(f"⚠️  Chyba při čtení JSON: {e}")
            return self._get_default_data()
    
    def _get_default_data(self) -> Dict:
        """Vrátí výchozí data, pokud soubor neexistuje"""
        return {
            "vedeni": [],
            "ucitele": [],
            "jidelna": {"dnesni_menu": {}, "tydenni_menu": {}},
            "rozvrhy": {},
            "info": {}
        }
    
    # === VEDENÍ ŠKOLY ===
    
    def get_vedeni(self) -> List[Dict]:
        """Vrátí seznam vedení školy"""
        return self.data.get("vedeni", [])
    
    def format_vedeni_info(self) -> str:
        """Vrátí formátovaný text s informacemi o vedení"""
        vedeni = self.get_vedeni()
        if not vedeni:
            return "Informace o vedení školy nejsou k dispozici."
        
        text = "👔 Vedení školy - Matiční gymnázium Ostrava\n\n"
        for osoba in vedeni:
            text += f"▪️ {osoba['jmeno']}\n"
            text += f"   Pozice: {osoba['pozice']}\n"
            if osoba.get('email'):
                text += f"   📧 Email: {osoba['email']}\n"
            if osoba.get('telefon'):
                text += f"   📞 Telefon: {osoba['telefon']}\n"
            text += "\n"
        
        return text
    
    # === UČITELÉ ===
    
    def get_ucitele(self) -> List[Dict]:
        """Vrátí seznam všech učitelů"""
        return self.data.get("ucitele", [])
    
    def get_ucitele_by_predmet(self, predmet: str) -> List[Dict]:
        """Vrátí učitele pro daný předmět"""
        predmet_lower = predmet.lower().strip()
        ucitele = []
        
        for ucitel in self.get_ucitele():
            predmety = ucitel.get("predmety", [])
            if any(predmet_lower in p.lower() for p in predmety):
                ucitele.append(ucitel)
        
        return ucitele
    
    def search_ucitele_by_name(self, jmeno: str) -> List[Dict]:
        """Vyhledá učitele podle jména"""
        jmeno_lower = jmeno.lower().strip()
        vysledky = []
        
        for ucitel in self.get_ucitele():
            if jmeno_lower in ucitel['jmeno'].lower():
                vysledky.append(ucitel)
        
        return vysledky
    
    # === JÍDELNA ===
    
    def get_dnesni_menu(self) -> Dict:
        """Vrátí dnešní menu"""
        return self.data.get("jidelna", {}).get("dnesni_menu", {})
    
    def get_tydenni_menu(self) -> Dict:
        """Vrátí týdenní menu"""
        return self.data.get("jidelna", {}).get("tydenni_menu", {})
    
    # === ROZVRHY ===
    
    def get_rozvrh(self, trida: str) -> Optional[Dict]:
        """Vrátí rozvrh pro danou třídu"""
        return self.data.get("rozvrhy", {}).get(trida.upper())
    
    def get_dostupne_tridy(self) -> List[str]:
        """Vrátí seznam tříd, pro které máme rozvrh"""
        return list(self.data.get("rozvrhy", {}).keys())
    
    # === INFO O ŠKOLE ===
    
    def get_info(self) -> Dict:
        """Vrátí základní informace o škole"""
        return self.data.get("info", {})
    
    def format_info(self) -> str:
        """Vrátí formátovaný text s informacemi o škole"""
        info = self.get_info()
        if not info:
            return "Informace o škole nejsou k dispozici."
        
        text = f"🏫 {info.get('nazev', 'Matiční gymnázium Ostrava')}\n\n"
        text += f"📍 Adresa: {info.get('adresa', 'N/A')}\n"
        text += f"📞 Telefon: {info.get('telefon', 'N/A')}\n"
        text += f"📧 Email: {info.get('email', 'N/A')}\n"
        text += f"🌐 Web: {info.get('web', 'N/A')}\n"
        
        return text


# Globální instance
data_manager = DataManager()
