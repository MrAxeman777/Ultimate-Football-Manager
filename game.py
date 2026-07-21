import json

def load_players():
    with open("database/players.json", "r") as file:
        return json.load(file)


def load_clubs():
    with open("database/clubs.json", "r") as file:
        return json.load(file)


players = load_players()
clubs = load_clubs()

print(players)
print(clubs)
