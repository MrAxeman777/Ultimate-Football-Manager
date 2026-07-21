import streamlit as st
import json
import os
from club import Club


SAVE_FILE = "database/saves.json"


def load_players():
    with open("database/players.json", "r") as file:
        return json.load(file)


def load_clubs():
    with open("database/clubs.json", "r") as file:
        data = json.load(file)

    clubs = []

    for c in data:
        club = Club(
            c["name"],
            c["budget"],
            c["reputation"],
            c["players"]
        )
        clubs.append(club)

    return clubs


def save_game(club):
    save_data = {
        "club": club.name,
        "budget": club.budget,
        "reputation": club.reputation,
        "players": club.players
    }

    with open(SAVE_FILE, "w") as file:
        json.dump(save_data, file, indent=4)


def load_save():
    if os.path.exists(SAVE_FILE):

        with open(SAVE_FILE, "r") as file:
            data = json.load(file)

            if data:
                return data

    return None


players = load_players()
clubs = load_clubs()


st.set_page_config(
    page_title="Soccer GM",
    page_icon="⚽"
)


st.title("⚽ Soccer GM")


# Load previous save
saved_game = load_save()


if saved_game:

    selected_club = next(
        club for club in clubs
        if club.name == saved_game["club"]
    )

    selected_club.budget = saved_game["budget"]
    selected_club.reputation = saved_game["reputation"]
    selected_club.players = saved_game["players"]

else:

    club_names = [club.name for club in clubs]

    choice = st.selectbox(
        "Choose your club:",
        club_names
    )

    selected_club = next(
        club for club in clubs
        if club.name == choice
    )


st.sidebar.success(
    f"Managing {selected_club.name}"
)


page = st.sidebar.selectbox(
    "Menu",
    [
        "Dashboard",
        "Squad",
        "Transfer Market"
    ]
)


if page == "Dashboard":

    st.header("🏟️ Club Dashboard")

    st.metric(
        "💰 Budget",
        f"${selected_club.budget:,}"
    )

    st.metric(
        "⭐ Reputation",
        selected_club.reputation
    )


elif page == "Squad":

    st.header("👥 Squad")

    for name in selected_club.players:

        player = next(
            (p for p in players if p["name"] == name),
            None
        )

        if player:

            st.subheader(player["name"])

            st.write(
                f"{player['position']} | "
                f"⭐ {player['rating']}"
            )


elif page == "Transfer Market":

    st.header("🔄 Transfer Market")

    for player in players:

        if player["name"] not in selected_club.players:

            st.write(
                f"{player['name']} - ${player['value']:,}"
            )

            if st.button(
                f"Buy {player['name']}",
                key=player["name"]
            ):

                if selected_club.budget >= player["value"]:

                    selected_club.players.append(
                        player["name"]
                    )

                    selected_club.budget -= player["value"]

                    save_game(selected_club)

                    st.success(
                        f"Signed {player['name']}!"
                    )

                else:

                    st.error(
                        "Not enough money!"
                    )


if st.button("💾 Save Game"):

    save_game(selected_club)

    st.success(
        "Game saved!"
    )
