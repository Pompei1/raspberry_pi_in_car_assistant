class Assistant:
    def __init__(self):
        self.name = "Car Assistant"

    def respond(self, command: str):
        if "hora" in command:
            return "Ainda vou aprender a falar as horas."
        return "Comando não reconhecido."
