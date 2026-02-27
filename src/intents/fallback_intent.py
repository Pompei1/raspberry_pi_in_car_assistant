from core.intent_engine import Intent

class FallbackIntent(Intent):
    def can_handle(self, command: str) -> bool:
        return True

    def handle(self, command: str) -> str:
        return "Desculpe, não entendi o comando."
