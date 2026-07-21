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
            c["reputation"]
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

st.subheader("Choose your club")

club_names = [club.name for club in clubs]

choice = st.selectbox(
    "Select your club:",
    club_names
)

selected_club = None

for club in clubs:
    if club.name == choice:
        selected_club = club


st.divider()

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


st.success(
    f"You are now managing {selected_club.name}!"
)
