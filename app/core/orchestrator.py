from app.llm.client import LLMClient

class ConversationOrchestrator:
    def __init__(self):
        self.llm = LLMClient()

    def generate_answer(self, user_message: str, user_id: str) -> str:
        # tady se později přidá RAG: retriever → context_chunks
        prompt = f"User ({user_id}) said: {user_message}\nAnswer politely in Czech."
        return self.llm.generate(prompt)
