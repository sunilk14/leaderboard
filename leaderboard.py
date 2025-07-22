import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Hackathon Leaderboard", layout="centered")
st.title("🏆 Python Hackathon Leaderboard")




CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRVfLHiUTMKKYoEUra1bZeTsUA9DcPc4u7aL_fCY2IvKkUDzuN7dTBNvxoEK1whWmmKoxtaaJDTzLWH/pub?gid=1258247712&single=true&output=csv"

# ---- PARAMETERS ----
GROUPS = [f"Group{str(i).zfill(2)}" for i in range(1, 10)]       # Group01 to Group09
TASKS = [f"Task{str(i).zfill(2)}" for i in range(1, 11)]          # Task01 to Task10

# ---- SCORING FUNCTION ----
def assign_score(rank):
    if rank == 0:
        return 5
    elif rank in [1, 2]:
        return 4
    elif rank in [3, 4, 5]:
        return 3
    elif rank in [6, 7]:
        return 2
    else:
        return 1

# ---- READ FORM RESPONSES ----
df = pd.read_csv(CSV_URL)
df.columns = [col.strip() for col in df.columns]
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df = df.sort_values(by=["TaskName", "Timestamp"])

# ---- CALCULATE SCORES ----
score_dict = {}

for task in TASKS:
    task_df = df[df["TaskName"] == task].reset_index(drop=True)
    for rank, row in task_df.iterrows():
        group = row["GroupName"]
        score = assign_score(rank)
        score_dict[(group, task)] = score

# ---- INITIALIZE FULL TABLE ----
data = []
for group in GROUPS:
    row = {"GroupName": group}
    for task in TASKS:
        row[task] = score_dict.get((group, task), 0)
    data.append(row)

pivot = pd.DataFrame(data)
pivot["Total"] = pivot[TASKS].sum(axis=1)
pivot = pivot.sort_values(by="Total", ascending=False)
pivot = pivot.set_index("GroupName")

# ---- DISPLAY ----
st.caption(f"Last updated: {datetime.now().strftime('%H:%M:%S')}")
st.dataframe(
    pivot.style.format(na_rep="–"),
    use_container_width=True,
    height=380,  # adjust height as needed
    width=520
)

# Optional: Refresh button
if st.button("🔄 Refresh Now"):
    st.experimental_rerun()
