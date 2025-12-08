from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.core.orchestrator import ConversationOrchestrator
from app.core.models import UserMessage
from app.core.database import ConversationDB
from app.kontakty.scraper import (
    scrape_vedeni_skoly, 
    format_vedeni_info,
    filter_ucitele_by_predmet,
    get_predmet_zkratka,
    format_ucitele_info
)
from app.jidelna.scraper import (
    get_jidelna_info, 
    format_jidelnicek_info,
    scrape_dnesni_menu,
    scrape_tydenni_menu
)
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
    """Získá informace o vedení školy ze stránky MGO"""
    try:
        vedeni_data = scrape_vedeni_skoly()
        return {
            "success": True,
            "data": vedeni_data,
            "formatted_text": format_vedeni_info(vedeni_data)
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
    Získá učitele pro daný předmět ze stránky pedagogického sboru.
    
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
        
        # Načteme učitele pro daný předmět
        ucitele_data = filter_ucitele_by_predmet(predmet_zkratka)
        
        # Získáme čitelný název předmětu
        predmet_nazvy = {
            'cestina': 'Český jazyk',
            'matematika': 'Matematika',
            'anglictina': 'Angličtina',
            'nemcina': 'Němčina',
            'fyzika': 'Fyzika',
            'chemie': 'Chemie',
            'biologie': 'Biologie',
            'dejepis': 'Dějepis',
            'zemepis': 'Zeměpis',
            'informatika': 'Informatika',
            'tv': 'Tělesná výchova',
            'hv': 'Hudební výchova'
        }
        predmet_nazev = predmet_nazvy.get(predmet_id.lower(), predmet_id)
        
        return {
            "success": True,
            "data": ucitele_data,
            "predmet": predmet_nazev,
            "formatted_text": format_ucitele_info(ucitele_data, predmet_nazev)
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "data": []
        }


@app.get("/jidelna")
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
    Získá dnešní menu z webu obedy.zs-mat5.cz
    """
    try:
        menu_data = scrape_dnesni_menu()
        return {
            "success": True,
            "data": menu_data
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
    Získá týdenní menu z webu obedy.zs-mat5.cz
    """
    try:
        menu_data = scrape_tydenni_menu()
        return {
            "success": True,
            "data": menu_data
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "data": None
        }
