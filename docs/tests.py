# Teste de Verificação de hora por comando por comando em um unico arquivo sem import
# testado com o time zone de São paulo

from datetime import datetime, timezone
import pytz

class Intent:
    def can_handle(self, command: str) -> bool:
        raise NotImplementedError

    def handle(self, command: str) -> str:
        raise NotImplementedError

class TimeIntent(Intent):
    def can_handle(self, command: str) -> bool:
        return "hora" in command.lower()

    def handle(self, command: str) -> str:
        # Get current UTC time
        utc_now = datetime.now(timezone.utc)
        # Define the timezone for São Paulo
        sa_paulo_timezone = pytz.timezone('America/Sao_Paulo')
        # Convert UTC time to São Paulo timezone
        sa_paulo_now = utc_now.astimezone(sa_paulo_timezone)
        return f"Agora são {sa_paulo_now.hour} horas e {sa_paulo_now.minute} minutos no fuso horário de São Paulo."

class FallbackIntent(Intent):
    def can_handle(self, command: str) -> bool:
        return True

    def handle(self, command: str) -> str:
        return "Desculpe, não entendi o comando."

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
def main():
  assistant = Assistant()

  while True:
      command = input("Digite um comando: ")
      response = assistant.process(command)
      print(response)

if __name__ == "__main__":
    main()
