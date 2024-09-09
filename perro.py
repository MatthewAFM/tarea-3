class Dog(Mammal):
    def __init__(self, name: str, type: str, head: Head):
        super().__init__(type)
        self.name = name
        self.head = head

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def go_for_walk(self):
        print(f"{self.name} caminando")

    def get_head(self) -> Head:
        return self.head

    def set_head(self, head: Head):
        self.head = head
