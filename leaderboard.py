import streamlit as st
import pandas as pd

# Initialize leaderboard data (persistent during session)
if "scores" not in st.session_state:
    st.session_state.scores = {}

st.title("📊 Python Hackathon Leaderboard")

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRhYwVRkT0NT57Ue8f89qwrlfrlPi6WeaAFZ-ZXTgxZIBzN44pYlkjzWBtzPmk6Jr35EG4ZWmWNbEW_/pub?gid=0&single=true&output=csv"

df = pd.read_csv(url)

leaderboard = df.groupby("Team")["Task"].nunique().reset_index()
leaderboard.columns = ["Team", "Score"]
leaderboard = leaderboard.sort_values("Score", ascending=False)

st.table(leaderboard)
