class Head: # creamos la clase head 
    def __init__(self, size: str):
        self.size = size

    def get_size(self) -> str:
        return self.size

    def set_size(self, size: str):
        self.size = size
