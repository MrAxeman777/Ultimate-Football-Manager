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
st.write("Become the manager of a football club!")

st.divider()


club_names = [club.name for club in clubs]

choice = st.selectbox(
    "Choose your club:",
    club_names
)


selected_club = next(
    club for club in clubs
    if club.name == choice
)


st.header(f"🏟️ {selected_club.name}")


col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Transfer Budget",
        f"${selected_club.budget:,}"
    )

with col2:
    st.metric(
        "Reputation",
        selected_club.reputation
    )


st.divider()

st.subheader("👥 Squad")


for squad_player in selected_club.players:

    player = next(
        (p for p in players if p["name"] == squad_player),
        None
    )

    if player:
        with st.container():
            st.subheader(f"⚽ {player['name']}")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.write(f"Position: {player['position']}")
                st.write(f"Age: {player['age']}")

            with col2:
                st.write(f"⭐ Rating: {player['rating']}")
                st.write(f"🚀 Potential: {player['potential']}")

            with col3:
                st.write(f"💰 Value: ${player['value']:,}")
                st.write(f"💵 Wage: ${player['wage']:,}")

            st.divider()
