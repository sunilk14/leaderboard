import streamlit as st
import pandas as pd

# Initialize leaderboard data (persistent during session)
if "scores" not in st.session_state:
    st.session_state.scores = {}

st.title("📊 Python Hackathon Leaderboard")

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRVfLHiUTMKKYoEUra1bZeTsUA9DcPc4u7aL_fCY2IvKkUDzuN7dTBNvxoEK1whWmmKoxtaaJDTzLWH/pub?gid=1258247712&single=true&output=csv"

df = pd.read_csv(url)

leaderboard = df.groupby("Team")["Task"].nunique().reset_index()
leaderboard.columns = ["Team", "Score"]
leaderboard = leaderboard.sort_values("Score", ascending=False)

st.table(leaderboard)
