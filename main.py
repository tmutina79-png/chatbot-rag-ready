from fastapi import FastAPI
from app.core.orchestrator import ConversationOrchestrator
from app.core.models import UserMessage
from app.core.database import ConversationDB

app = FastAPI(
    title="MATIČÁK",
    description="Matiční AI Pomocník - inteligentní školní asistent",
    version="0.1.0"
)
orchestrator = ConversationOrchestrator()
db = ConversationDB()

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
