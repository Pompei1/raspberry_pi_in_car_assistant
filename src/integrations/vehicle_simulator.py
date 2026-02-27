import random

class VehicleSimulator:
    def get_speed(self) -> int:
        # Simula velocidade entre 0 e 120 km/h
        return random.randint(0, 120)
