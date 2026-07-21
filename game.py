import json
from player import Player
from club import Club


def load_players():
    with open("database/players.json", "r") as file:
        data = json.load(file)

    players = []

    for p in data:
        player = Player(
            p["name"],
            p["position"],
            p["age"],
            p["rating"],
            p["potential"],
            p["value"],
            p["wage"]
        )
        players.append(player)

    return players


def load_clubs():
    with open("database/clubs.json", "r") as file:
        data = json.load(file)

    clubs = []

    for c in data:
        club = Club(
            c["name"],
            c["budget"],
            c["reputation"]
        )
        clubs.append(club)

    return clubs


# Load game data
players = load_players()
clubs = load_clubs()


# Start game
print("⚽ Welcome to Soccer GM!")

print("\nChoose your club:")

for index, club in enumerate(clubs):
    print(f"{index + 1}. {club.name}")

choice = int(input("\nEnter club number: "))

your_club = clubs[choice - 1]

print(f"\n🏟️ You are now managing {your_club.name}!")
print(your_club.info())
