from fastapi import FastAPI
from app.core.orchestrator import ConversationOrchestrator
from app.core.models import UserMessage

app = FastAPI()
orchestrator = ConversationOrchestrator()

@app.post("/chat")
def chat(message: UserMessage):
    reply = orchestrator.generate_answer(message.text, user_id=message.user_id)
    return {"reply": reply}
