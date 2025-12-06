from app.core.rule_based import RuleBasedResponder

class LLMClient:
    def __init__(self):
        self.rule_responder = RuleBasedResponder()
    
    def generate(self, prompt: str, user_message: str = None) -> str:
        # Použijeme pravidlovou logiku místo LLM API
        if user_message:
            return self.rule_responder.get_response(user_message)
        # Fallback pro starý způsob volání
        return f"(TEST) Odpovídám na: {prompt}"
