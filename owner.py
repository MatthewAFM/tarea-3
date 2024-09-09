class Owner:
    def __init__(self, name: str):
        self.name = name
        self.dogs = []

    def get_name(self) -> str:
        return self.name

    def walk_dog(self):
        for dog in self.dogs:
            dog.go_for_walk()

    def add_dog(self, dog: Dog):
        self.dogs.append(dog)
