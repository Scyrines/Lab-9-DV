import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Lab 9 | Chart Design", layout="wide")

data = pd.DataFrame({
    "Branch": ["North", "South", "East", "West"],
    "Sales": [96, 99, 98, 100],
})

st.title("Designing a Clearer Bar Chart")
version = st.radio("Choose a chart", ["Cluttered", "Improved"])

fig, ax = plt.subplots(figsize=(8, 4.5))

if version == "Cluttered":
    bars = ax.bar(
        data["Branch"],
        data["Sales"],
        color=["#8FB9A8", "#D8B365", "#B2ABD2", "#5E3C99"]
    )
    ax.set_ylim(95, 101)
    ax.set_facecolor("#E8E8E8")
    ax.grid(True, which="both", color="white", linewidth=2)
    ax.set_title("SALES PERFORMANCE!!!")
else:
    bars = ax.bar(data["Branch"], data["Sales"], color="#4C78A8")
    for branch, bar in zip(data["Branch"], bars):
        if branch == "West":
            bar.set_color("#E07A3F")
    ax.set_ylim(0, 105)
    ax.set_yticks(range(0, 101, 20))
    ax.bar_label(bars, fmt="%.0f", padding=3)
    ax.set_title("West branch recorded the highest sales")
    ax.grid(axis="y", color="#DDDDDD", linewidth=0.7)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

ax.set_ylabel("Sales (units)")
fig.tight_layout()
st.pyplot(fig, clear_figure=True)
st.caption("Fictional practice data. The improved bar chart starts at zero.")
