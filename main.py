from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.core.orchestrator import ConversationOrchestrator
from app.core.models import UserMessage
from app.core.database import ConversationDB
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
