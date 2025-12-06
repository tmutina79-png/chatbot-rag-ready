from app.llm.client import LLMClient
from app.core.database import ConversationDB

class ConversationOrchestrator:
    def __init__(self):
        self.llm = LLMClient()
        self.db = ConversationDB()

    def generate_answer(self, user_message: str, user_id: str) -> str:
        # tady se později přidá RAG: retriever → context_chunks
        # Zatím používáme pravidlovou logiku
        response = self.llm.generate(prompt="", user_message=user_message)
        
        # Uložit konverzaci do databáze
        self.db.save_conversation(user_id, user_message, response)
        
        return response
