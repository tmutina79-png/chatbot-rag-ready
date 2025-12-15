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

from app.rozvrh.scraper import (
    scrape_rozvrh_kva, scrape_rozvrh_pa, scrape_rozvrh_tb,
    scrape_rozvrh_pb, scrape_rozvrh_sa, scrape_rozvrh_sb, scrape_rozvrh_ta, scrape_rozvrh_kvb,
    scrape_rozvrh_1w, scrape_rozvrh_sxa,
    scrape_rozvrh_1a, scrape_rozvrh_kvia, scrape_rozvrh_kvib, scrape_rozvrh_2a,
    scrape_rozvrh_sxb, scrape_rozvrh_3a, scrape_rozvrh_spta, scrape_rozvrh_sptb,
    scrape_rozvrh_4a, scrape_rozvrh_okta, scrape_rozvrh_oktb
)

import os

# Inicializace FastAPI aplikace a middleware
app = FastAPI(
    title="MATIČÁK",
    description="Matiční AI Pomocník - inteligentní školní asistent",
    version="0.1.1"  # Aktualizováno: Oprava scraperu rozvrhu TA
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

@app.get("/rozvrh/pb")
def get_rozvrh_pb():
    """
    Získá rozvrh třídy PB - používá lokální databázi
    """
    try:
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_pb()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("PB")
        return {"success": True, "data": rozvrh_data, "source": source}
    except Exception as e:
        return {"success": False, "error": str(e), "data": None}

@app.get("/rozvrh/sa")
def get_rozvrh_sa():
    """
    Získá rozvrh třídy SA - používá lokální databázi
    """
    try:
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_sa()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("SA")
        return {"success": True, "data": rozvrh_data, "source": source}
    except Exception as e:
        return {"success": False, "error": str(e), "data": None}

@app.get("/rozvrh/sb")
def get_rozvrh_sb():
    """
    Získá rozvrh třídy SB - používá lokální databázi
    """
    try:
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_sb()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("SB")
        return {"success": True, "data": rozvrh_data, "source": source}
    except Exception as e:
        return {"success": False, "error": str(e), "data": None}

@app.get("/rozvrh/ta")
def get_rozvrh_ta():
    """
    Získá rozvrh třídy TA - používá lokální databázi
    """
    try:
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_ta()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("TA")
        return {"success": True, "data": rozvrh_data, "source": source}
    except Exception as e:
        return {"success": False, "error": str(e), "data": None}

@app.get("/rozvrh/kvb")
def get_rozvrh_kvb():
    """
    Získá rozvrh třídy KVB - používá lokální databázi
    """
    try:
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_kvb()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("KVB")
        return {"success": True, "data": rozvrh_data, "source": source}
    except Exception as e:
        return {"success": False, "error": str(e), "data": None}

@app.get("/rozvrh/1w")
def get_rozvrh_1w():
    """
    Získá rozvrh třídy 1W - používá lokální databázi
    """
    try:
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_1w()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("1W")
        return {"success": True, "data": rozvrh_data, "source": source}
    except Exception as e:
        return {"success": False, "error": str(e), "data": None}

@app.get("/rozvrh/sxa")
def get_rozvrh_sxa():
    """Získá rozvrh třídy SXA - používá lokální databázi"""
    try:
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_sxa()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("SXA")
        return {"success": True, "data": rozvrh_data, "source": source}
    except Exception as e:
        return {"success": False, "error": str(e), "data": None}

@app.get("/rozvrh/1a")
def get_rozvrh_1a():
    """Získá rozvrh třídy 1.A"""
    try:
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_1a()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("1A")
        return {"success": True, "data": rozvrh_data, "source": source}
    except Exception as e:
        return {"success": False, "error": str(e), "data": None}

@app.get("/rozvrh/kvia")
def get_rozvrh_kvia():
    """Získá rozvrh třídy KVIA"""
    try:
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_kvia()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("KVIA")
        return {"success": True, "data": rozvrh_data, "source": source}
    except Exception as e:
        return {"success": False, "error": str(e), "data": None}

@app.get("/rozvrh/kvib")
def get_rozvrh_kvib():
    """Získá rozvrh třídy KVIB"""
    try:
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_kvib()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("KVIB")
        return {"success": True, "data": rozvrh_data, "source": source}
    except Exception as e:
        return {"success": False, "error": str(e), "data": None}

@app.get("/rozvrh/2a")
def get_rozvrh_2a():
    """Získá rozvrh třídy 2.A"""
    try:
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_2a()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("2A")
        return {"success": True, "data": rozvrh_data, "source": source}
    except Exception as e:
        return {"success": False, "error": str(e), "data": None}

@app.get("/rozvrh/sxb")
def get_rozvrh_sxb():
    """Získá rozvrh třídy SXB"""
    try:
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_sxb()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("SXB")
        return {"success": True, "data": rozvrh_data, "source": source}
    except Exception as e:
        return {"success": False, "error": str(e), "data": None}

@app.get("/rozvrh/3a")
def get_rozvrh_3a():
    """Získá rozvrh třídy 3.A"""
    try:
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_3a()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("3A")
        return {"success": True, "data": rozvrh_data, "source": source}
    except Exception as e:
        return {"success": False, "error": str(e), "data": None}

@app.get("/rozvrh/spta")
def get_rozvrh_spta():
    """Získá rozvrh třídy SPTA"""
    try:
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_spta()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("SPTA")
        return {"success": True, "data": rozvrh_data, "source": source}
    except Exception as e:
        return {"success": False, "error": str(e), "data": None}

@app.get("/rozvrh/sptb")
def get_rozvrh_sptb():
    """Získá rozvrh třídy SPTB"""
    try:
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_sptb()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("SPTB")
        return {"success": True, "data": rozvrh_data, "source": source}
    except Exception as e:
        return {"success": False, "error": str(e), "data": None}

@app.get("/rozvrh/4a")
def get_rozvrh_4a():
    """Získá rozvrh třídy 4.A"""
    try:
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_4a()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("4A")
        return {"success": True, "data": rozvrh_data, "source": source}
    except Exception as e:
        return {"success": False, "error": str(e), "data": None}

@app.get("/rozvrh/okta")
def get_rozvrh_okta():
    """Získá rozvrh třídy OKTA"""
    try:
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_okta()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("OKTA")
        return {"success": True, "data": rozvrh_data, "source": source}
    except Exception as e:
        return {"success": False, "error": str(e), "data": None}

@app.get("/rozvrh/oktb")
def get_rozvrh_oktb():
    """Získá rozvrh třídy OKTB"""
    try:
        rozvrh_data = None
        source = "database"
        try:
            rozvrh_data = scrape_rozvrh_oktb()
            if rozvrh_data:
                source = "scraping"
        except:
            pass
        if not rozvrh_data:
            rozvrh_data = data_manager.get_rozvrh("OKTB")
        return {"success": True, "data": rozvrh_data, "source": source}
    except Exception as e:
        return {"success": False, "error": str(e), "data": None}

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
            from app.kontakty.scraper import filter_ucitele_by_predmet
            ucitele_data = filter_ucitele_by_predmet(predmet_zkratka)
            if ucitele_data:
                source = "scraping"
        except Exception:
            pass
        # Fallback na lokální databázi
        if not ucitele_data:
            ucitele_data = data_manager.get_ucitele_by_predmet(predmet_zkratka)
        return {
            "success": True,
            "data": ucitele_data,
            "source": source
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "data": []
        }


@app.get("/kontakt/hledat-ucitele/{name}")
def hledat_ucitele(name: str):
    """
    Hledá učitele podle jména nebo příjmení
    
    Args:
        name: Jméno nebo příjmení učitele (case-insensitive)
    """
    try:
        # Nejdřív zkus scraping - načti všechny učitele
        ucitele_data = []
        source = "database"
        try:
            from app.kontakty.scraper import scrape_ucitele_pedagogicky_sbor
            ucitele_data = scrape_ucitele_pedagogicky_sbor()
            if ucitele_data:
                source = "scraping"
        except Exception:
            pass
        
        # Fallback na lokální databázi
        if not ucitele_data:
            ucitele_data = data_manager.get_ucitele()
        
        # Normalizace hledaného jména
        search_name = name.lower().strip()
        
        # Funkce pro odstranění diakritiky
        import unicodedata
        def remove_diacritics(text):
            return ''.join(
                c for c in unicodedata.normalize('NFD', text)
                if unicodedata.category(c) != 'Mn'
            )
        
        search_name_normalized = remove_diacritics(search_name)
        
        # Hledání učitele
        nalezeni_ucitele = []
        for ucitel in ucitele_data:
            ucitel_jmeno = ucitel.get('jmeno', '').lower()
            ucitel_jmeno_normalized = remove_diacritics(ucitel_jmeno)
            
            # Hledáme shodu v celém jméně nebo v jeho částech
            if (search_name in ucitel_jmeno or 
                search_name_normalized in ucitel_jmeno_normalized or
                any(search_name in part.lower() or search_name_normalized in remove_diacritics(part.lower()) 
                    for part in ucitel_jmeno.split())):
                nalezeni_ucitele.append(ucitel)
        
        return {
            "success": True,
            "data": nalezeni_ucitele,
            "count": len(nalezeni_ucitele),
            "source": source
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "data": [],
            "count": 0
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
