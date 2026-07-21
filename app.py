import streamlit as st
import json
from club import Club


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

if selected_club.players:
    for player in selected_club.players:
        st.write(f"⚽ {player}")
else:
    st.write("No players yet.")
