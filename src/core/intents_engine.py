class Intent:
    def can_handle(self, command: str) -> bool:
        raise NotImplementedError

    def handle(self, command: str) -> str:
        raise NotImplementedError
