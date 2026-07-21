import streamlit as st
import json
from club import Club


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


players = load_players()
clubs = load_clubs()


st.set_page_config(
    page_title="Soccer GM",
    page_icon="⚽"
)


st.title("⚽ Soccer GM")

# Choose club
club_names = [club.name for club in clubs]

choice = st.selectbox(
    "Choose your club:",
    club_names
)

selected_club = next(
    club for club in clubs
    if club.name == choice
)


# Navigation
page = st.sidebar.selectbox(
    "Menu",
    [
        "Dashboard",
        "Squad",
        "Transfer Market"
    ]
)


# Dashboard
if page == "Dashboard":

    st.header(f"🏟️ {selected_club.name}")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "💰 Transfer Budget",
            f"${selected_club.budget:,}"
        )

    with col2:
        st.metric(
            "⭐ Reputation",
            selected_club.reputation
        )


# Squad
elif page == "Squad":

    st.header("👥 Squad")

    for squad_player in selected_club.players:

        player = next(
            (p for p in players if p["name"] == squad_player),
            None
        )

        if player:
            st.subheader(f"⚽ {player['name']}")
            st.write(
                f"{player['position']} | "
                f"Rating: {player['rating']} | "
                f"Value: ${player['value']:,}"
            )

            st.divider()


# Transfer Market
elif page == "Transfer Market":

    st.header("🔄 Transfer Market")

    st.write(
        f"Available Budget: ${selected_club.budget:,}"
    )

    for player in players:

        if player["name"] not in selected_club.players:

            st.subheader(player["name"])

            st.write(
                f"{player['position']} | "
                f"⭐ {player['rating']} | "
                f"💰 ${player['value']:,}"
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

                    st.success(
                        f"Signed {player['name']}!"
                    )

                else:
                    st.error(
                        "Not enough money!"
                    )

            st.divider()
