from core.intent_engine import Intent
from integrations.vehicle_simulator import VehicleSimulator

class SpeedIntent(Intent):
    def __init__(self):
        self.vehicle = VehicleSimulator()

    def can_handle(self, command: str) -> bool:
        keywords = ["velocidade", "rápido", "devagar"]
        return any(word in command.lower() for word in keywords)

    def handle(self, command: str) -> str:
        speed = self.vehicle.get_speed()
        return f"A velocidade atual é {speed} km/h."
