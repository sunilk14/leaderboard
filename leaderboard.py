import streamlit as st
import pandas as pd

# Initialize leaderboard data (persistent during session)
if "scores" not in st.session_state:
    st.session_state.scores = {}

st.title("📊 Python Hackathon Leaderboard")

# Team input
team = st.text_input("Enter your Team Name")

# Simulate problem solved
problems = ["Summary Stats", "Missing Values", "Groupby Aggregation", "Bonus Insight"]
problem_solved = st.selectbox("Select Problem Solved", problems)

if st.button("Submit"):
    st.session_state.scores.setdefault(team, set()).add(problem_solved)

# Show live leaderboard
st.subheader("🏆 Live Leaderboard")

scoreboard = {
    team: len(solved_problems) for team, solved_problems in st.session_state.scores.items()
}
df = pd.DataFrame(sorted(scoreboard.items(), key=lambda x: -x[1]), columns=["Team", "Score"])
st.table(df)

