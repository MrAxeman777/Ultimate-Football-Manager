class Club:
    def __init__(self, name, budget, reputation, players=None):
        self.name = name
        self.budget = budget
        self.reputation = reputation
        self.players = players if players else []
        self.trophies = []

    def info(self):
        return f"{self.name} | Budget: ${self.budget:,} | Reputation: {self.reputation}"
