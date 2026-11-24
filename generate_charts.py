"""
Script to generate all chart figures for Lab 9:
1. cluttered_chart.png
2. improved_chart.png
3. final_chart.png
"""

import matplotlib.pyplot as plt
import pandas as pd
import os

out_dir = r"C:\Users\ASUS\Documents\Uni Docs\Data Viz\Lab 9"

# 1. Cluttered Chart
data_orig = pd.DataFrame({
    "Branch": ["North", "South", "East", "West"],
    "Sales": [96, 99, 98, 100],
})

fig1, ax1 = plt.subplots(figsize=(8, 4.5), dpi=300)
bars1 = ax1.bar(
    data_orig["Branch"],
    data_orig["Sales"],
    color=["#8FB9A8", "#D8B365", "#B2ABD2", "#5E3C99"]
)
ax1.set_ylim(95, 101)
ax1.set_facecolor("#E8E8E8")
ax1.grid(True, which="both", color="white", linewidth=2)
ax1.set_title("SALES PERFORMANCE!!!", fontsize=13, fontweight="bold")
ax1.set_ylabel("Sales (units)")
fig1.tight_layout()
fig1.savefig(os.path.join(out_dir, "cluttered_chart.png"), dpi=300, bbox_inches="tight")
plt.close(fig1)

# 2. Improved Chart (Lesson 1 Baseline)
fig2, ax2 = plt.subplots(figsize=(8, 4.5), dpi=300)
bars2 = ax2.bar(data_orig["Branch"], data_orig["Sales"], color="#4C78A8")
for branch, bar in zip(data_orig["Branch"], bars2):
    if branch == "West":
        bar.set_color("#E07A3F")
ax2.set_ylim(0, 105)
ax2.set_yticks(range(0, 101, 20))
ax2.bar_label(bars2, fmt="%.0f", padding=3)
ax2.set_title("West branch recorded the highest sales", fontsize=12, pad=10)
ax2.grid(axis="y", color="#DDDDDD", linewidth=0.7)
ax2.set_axisbelow(True)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.set_ylabel("Sales (units)")
fig2.tight_layout()
fig2.savefig(os.path.join(out_dir, "improved_chart.png"), dpi=300, bbox_inches="tight")
plt.close(fig2)

# 3. Final Assignment Chart (Lesson 3: 6 Branches Extended & Polished)
data_final = pd.DataFrame({
    "Branch": ["North", "South", "East", "West", "Central", "Northwest"],
    "Sales": [96, 99, 98, 104, 101, 92]
})

fig3, ax3 = plt.subplots(figsize=(9, 4.8), dpi=300)
colors = ["#D9381E" if b == "West" else "#78909C" for b in data_final["Branch"]]
bars3 = ax3.bar(
    data_final["Branch"],
    data_final["Sales"],
    color=colors,
    width=0.55
)
ax3.set_ylim(0, 120)
ax3.set_yticks(range(0, 121, 20))
ax3.set_ylabel("Sales Volume (units)", fontsize=11, labelpad=8, color="#37474F")

for bar in bars3:
    h = bar.get_height()
    is_max = (h == data_final["Sales"].max())
    ax3.annotate(
        f"{int(h)}",
        xy=(bar.get_x() + bar.get_width() / 2, h),
        xytext=(0, 4),
        textcoords="offset points",
        ha="center", va="bottom",
        fontsize=10.5,
        fontweight="bold" if is_max else "normal",
        color="#B71C1C" if is_max else "#263238"
    )

ax3.set_title(
    "West Branch Recorded the Highest Sales at 104 Units",
    fontsize=13.5,
    fontweight="bold",
    pad=16,
    loc="left",
    color="#212121"
)

ax3.spines["top"].set_visible(False)
ax3.spines["right"].set_visible(False)
ax3.spines["left"].set_color("#CFD8DC")
ax3.spines["bottom"].set_color("#CFD8DC")
ax3.grid(axis="y", color="#ECEFF1", linestyle="-", linewidth=0.8)
ax3.set_axisbelow(True)
ax3.tick_params(axis="x", labelsize=11, length=0, colors="#263238")
ax3.tick_params(axis="y", labelsize=10, colors="#546E7A")

attribution_text = "Data: fictional practice values (2026) | Chart: Data Visualization Student"
fig3.text(0.12, -0.02, attribution_text, fontsize=9, color="#78909C", style="italic")

fig3.tight_layout()
fig3.savefig(os.path.join(out_dir, "final_chart.png"), dpi=300, bbox_inches="tight")
plt.close(fig3)

print("All Lab 9 charts generated successfully!")
