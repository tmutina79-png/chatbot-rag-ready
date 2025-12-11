from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.core.orchestrator import ConversationOrchestrator
from app.core.models import UserMessage
from app.core.database import ConversationDB
from app.core.data_manager import data_manager
from app.kontakty.scraper import (
    scrape_vedeni_skoly, 
    format_vedeni_info,
    filter_ucitele_by_predmet,
    get_predmet_zkratka,
    format_ucitele_info,
    search_ucitele_by_name
)
from app.jidelna.scraper import (
    get_jidelna_info, 
    format_jidelnicek_info,
    scrape_dnesni_menu,
    scrape_tydenni_menu
)
from app.rozvrh.scraper import scrape_rozvrh_kva, scrape_rozvrh_pa, scrape_rozvrh_tb
import os

app = FastAPI(
    title="MATIČÁK",
    description="Matiční AI Pomocník - inteligentní školní asistent",
    version="0.1.0"
)

# CORS middleware pro povolení requestů z browseru
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

orchestrator = ConversationOrchestrator()
db = ConversationDB()

# Servírovat statické soubory (obrázky, atd.)
app.mount("/static", StaticFiles(directory="app/ui"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    """Zobrazí webové rozhraní"""
    html_path = os.path.join("app", "ui", "chat.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/config.js")
async def get_config():
    """Servíruje config.js"""
    config_path = os.path.join("app", "ui", "config.js")
    with open(config_path, "r", encoding="utf-8") as f:
        content = f.read()
    return HTMLResponse(content=content, media_type="application/javascript")

@app.post("/chat")
def chat(message: UserMessage):
    reply = orchestrator.generate_answer(message.text, user_id=message.user_id)
    return {"reply": reply}

@app.get("/history/{user_id}")
def get_history(user_id: str, limit: int = 10):
    """Získá historii konverzací pro daného uživatele"""
    history = db.get_user_history(user_id, limit)
    return {"user_id": user_id, "history": history}

@app.get("/stats/{user_id}")
def get_stats(user_id: str):
    """Získá statistiky uživatele"""
    stats = db.get_user_stats(user_id)
    if stats:
        return {"user_id": user_id, "stats": stats}
    return {"error": "User not found"}

@app.get("/conversations")
def get_all_conversations(limit: int = 50):
    """Získá všechny nedávné konverzace"""
    conversations = db.get_all_conversations(limit)
    return {"conversations": conversations}

@app.get("/kontakt/vedeni")
def get_vedeni_skoly():
    """Získá informace o vedení školy - používá lokální databázi"""
    try:
        # Nejdřív zkus scraping
        try:
            vedeni_data = scrape_vedeni_skoly()
            if vedeni_data:
                return {
                    "success": True,
                    "data": vedeni_data,
                    "formatted_text": format_vedeni_info(vedeni_data),
                    "source": "scraping"
                }
        except:
            pass
        
        # Fallback na lokální databázi
        vedeni_data = data_manager.get_vedeni()
        return {
            "success": True,
            "data": vedeni_data,
            "formatted_text": data_manager.format_vedeni_info(),
            "source": "database"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "data": []
        }


@app.get("/kontakt/ucitele/{predmet_id}")
def get_ucitele_by_predmet(predmet_id: str):
    """
    Získá učitele pro daný předmět - používá lokální databázi
    
    Args:
        predmet_id: ID předmětu (např. 'matematika', 'cestina', 'anglictina')
    """
    try:
        # Převedeme ID na zkratku předmětu
        predmet_zkratka = get_predmet_zkratka(predmet_id)
        
        if not predmet_zkratka:
            return {
                "success": False,
                "error": f"Neznámý předmět: {predmet_id}",
                "data": []
            }
        
        # Nejdřív zkus scraping
        ucitele_data = []
        source = "database"
        try:
            ucitele_data = filter_ucitele_by_predmet(predmet_zkratka)
            if ucitele_data:
                source = "scraping"
        except:
            pass
        
        # Fallback na lokální databázi
        if not ucitele_data:
            ucitele_data = data_manager.get_ucitele_by_predmet(predmet_id.lower())
        
        # Získáme čitelný název předmětu
        predmet_nazvy = {
            # Jazyky
            'cestina': 'Český jazyk',
            'cj': 'Český jazyk',
            'čj': 'Český jazyk',
            'český jazyk': 'Český jazyk',
            'cesky jazyk': 'Český jazyk',
            'matematika': 'Matematika',
            'm': 'Matematika',
            'anglictina': 'Angličtina',
            'aj': 'Angličtina',
            'angličtina': 'Angličtina',
            'nemcina': 'Němčina',
            'nj': 'Němčina',
            'němčina': 'Němčina',
            'spanelstina': 'Španělština',
            'sj': 'Španělština',
            'šj': 'Španělština',
            'španělština': 'Španělština',
            'francouzstina': 'Francouzština',
            'fj': 'Francouzština',
            'francouzština': 'Francouzština',
            'rustina': 'Ruština',
            'rj': 'Ruština',
            'ruština': 'Ruština',
            'latina': 'Latina',
            'la': 'Latina',
            # Přírodní vědy
            'fyzika': 'Fyzika',
            'f': 'Fyzika',
            'chemie': 'Chemie',
            'ch': 'Chemie',
            'biologie': 'Biologie',
            'bi': 'Biologie',
            # Společenské vědy
            'dejepis': 'Dějepis',
            'd': 'Dějepis',
            'dějepis': 'Dějepis',
            'zemepis': 'Zeměpis',
            'z': 'Zeměpis',
            'zeměpis': 'Zeměpis',
            'zsv': 'Základy společenských věd',
            'základy společenských věd': 'Základy společenských věd',
            'zaklady spolecenskych ved': 'Základy společenských věd',
            'ov': 'Občanská výchova',
            'obcanska-vychova': 'Občanská výchova',
            'občanská výchova': 'Občanská výchova',
            'obcanska vychova': 'Občanská výchova',
            'eks': 'EKS',
            'ekonomie': 'EKS',
            # IT a umění
            'informatika': 'Informatika',
            'ivt': 'Informatika',
            'tv': 'Tělesná výchova',
            'telesna-vychova': 'Tělesná výchova',
            'tělesná výchova': 'Tělesná výchova',
            'telesna vychova': 'Tělesná výchova',
            'hv': 'Hudební výchova',
            'hudebni-vychova': 'Hudební výchova',
            'hudební výchova': 'Hudební výchova',
            'hudebni vychova': 'Hudební výchova',
            'vv': 'Výtvarná výchova',
            'vytvarnavychova': 'Výtvarná výchova',
            'výtvarná výchova': 'Výtvarná výchova'
        }
        predmet_nazev = predmet_nazvy.get(predmet_id.lower(), predmet_id)
        
        return {
            "success": True,
            "data": ucitele_data,
            "predmet": predmet_nazev,
            "formatted_text": format_ucitele_info(ucitele_data, predmet_nazev),
            "source": source
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "data": []
        }


@app.get("/kontakt/hledat-ucitele/{jmeno}")
def hledat_ucitele(jmeno: str):
    """
    Vyhledá učitele podle jména nebo příjmení - používá lokální databázi
    
    Args:
        jmeno: Jméno nebo příjmení učitele (bez diakritiky)
    """
    try:
        # Nejdřív zkus scraping
        ucitele_data = []
        source = "database"
        try:
            ucitele_data = search_ucitele_by_name(jmeno)
            if ucitele_data:
                source = "scraping"
        except:
            pass
        
        # Fallback na lokální databázi
        if not ucitele_data:
            ucitele_data = data_manager.search_ucitele_by_name(jmeno)
        
        if not ucitele_data:
            return {
                "success": True,
                "data": [],
                "message": f"Nebyl nalezen žádný učitel se jménem nebo příjmením '{jmeno}'.",
                "source": source
            }
        
        return {
            "success": True,
            "data": ucitele_data,
            "count": len(ucitele_data),
            "source": source
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "data": []
        }


@app.get("/jidelna/info")
def get_jidelna():
    """
    Získá informace o školní jídelně
    """
    try:
        jidelna_data = get_jidelna_info()
        return {
            "success": True,
            "data": jidelna_data
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "data": None
        }


@app.get("/jidelna/dnesni-menu")
def get_dnesni_menu():
    """
    Získá dnešní menu - používá lokální databázi
    """
    try:
        # Nejdřív zkus scraping
        menu_data = None
        source = "database"
        try:
            menu_data = scrape_dnesni_menu()
            if menu_data:
                source = "scraping"
        except:
            pass
        
        # Fallback na lokální databázi
        if not menu_data:
            menu_data = data_manager.get_dnesni_menu()
        
        return {
            "success": True,
            "data": menu_data,
            "source": source
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "data": None
        }


@app.get("/jidelna/tydenni-menu")
def get_tydenni_menu():
    """
    Získá týdenní menu - používá lokální databázi
    """
    try:
        # Nejdřív zkus scraping
        menu_data = None
        source = "database"
        try:
            menu_data = scrape_tydenni_menu()
            if menu_data:
                source = "scraping"
        except:
            pass
        
        # Fallback na lokální databázi
        if not menu_data:
            menu_data = data_manager.get_tydenni_menu()
        
        return {
            "success": True,
            "data": menu_data,
            "source": source
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "data": None
        }


@app.get("/rozvrh/kva")
def get_rozvrh_kva():
    """
    Získá rozvrh třídy KVA - používá lokální databázi
    """
    try:
        # Nejdřív zkus scraping
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_kva()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        
        # Fallback na lokální databázi
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("KVA")
        
        return {
            "success": True,
            "data": rozvrh_data,
            "source": source
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "data": None
        }

@app.get("/rozvrh/pa")
def get_rozvrh_pa():
    """
    Získá rozvrh třídy PA - používá lokální databázi
    """
    try:
        # Nejdřív zkus scraping
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_pa()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        
        # Fallback na lokální databázi
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("PA")
        
        return {
            "success": True,
            "data": rozvrh_data,
            "source": source
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "data": None
        }

@app.get("/rozvrh/tb")
def get_rozvrh_tb():
    """
    Získá rozvrh třídy TB - používá lokální databázi
    """
    try:
        # Nejdřív zkus scraping
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_tb()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        
        # Fallback na lokální databázi
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("TB")
        
        return {
            "success": True,
            "data": rozvrh_data,
            "source": source
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "data": None
        }
