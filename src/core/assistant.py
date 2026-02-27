class Assistant:
    def __init__(self):
        self.name = "Car Assistant"

    def respond(self, command: str):
        if "hora" in command:
            return "Ainda vou aprender a falar as horas."
        return "Comando não reconhecido."

from intents.time_intent import TimeIntent
from intents.fallback_intent import FallbackIntent

class Assistant:
    def __init__(self):
        self.intents = [
            TimeIntent(),
            FallbackIntent()
        ]

    def process(self, command: str) -> str:
        for intent in self.intents:
            if intent.can_handle(command):
                return intent.handle(command)
