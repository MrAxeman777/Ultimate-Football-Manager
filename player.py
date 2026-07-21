class Player:
    def __init__(self, name, position, age, rating, potential, value, wage):
        self.name = name
        self.position = position
        self.age = age
        self.rating = rating
        self.potential = potential
        self.value = value
        self.wage = wage

    def info(self):
        return f"{self.name} | {self.position} | Rating: {self.rating}"
