class Mammal:
    def __init__(self, type: str):
        self.type = type

    def get_type(self) -> str:
        return self.type

    def set_type(self, type: str):
        self.type = type
