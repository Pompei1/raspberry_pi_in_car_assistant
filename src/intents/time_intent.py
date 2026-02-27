from datetime import datetime
from core.intent_engine import Intent

class TimeIntent(Intent):
    def can_handle(self, command: str) -> bool:
        return "hora" in command.lower()

    def handle(self, command: str) -> str:
        now = datetime.now()
        return f"Agora são {now.hour} horas e {now.minute} minutos."
