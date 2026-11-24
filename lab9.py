"""
TFB3133/TEB3133 Data Visualization
Lab 9: Design Principles and Chartjunk
Streamlit Application Demonstrating Visual De-cluttering and Chart Standards
"""

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import os

# Configure Streamlit page layout
st.set_page_config(
    page_title="Lab 9 | Design Principles & Chartjunk",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Sidebar Navigation & Context
# ---------------------------------------------------------
st.sidebar.title("Lab 9: Chart Design Controls")
st.sidebar.markdown(
    """
    **Course Reference:**  
    Lecture 2: *Design Principles for Visualization*  
    - Ten Design Standards  
    - Data Integrity & Baseline Distortions  
    - Eliminating Chartjunk  
    """
)

chart_view = st.sidebar.radio(
    "Select Chart Version to Display:",
    [
        "Assignment Submission (6 Branches - Polished)",
        "Lesson 1 Baseline: Improved Chart",
        "Lesson 1 Baseline: Cluttered Chart"
    ]
)

# ---------------------------------------------------------
# App Header
# ---------------------------------------------------------
st.title("Lab 9: Eliminating Chartjunk & Applying Design Principles")
st.markdown(
    "Explore how scale truncation, color overuse, and non-data ink distort visual perception, "
    "and how applying core visualization standards restores data integrity."
)

# ---------------------------------------------------------
# 1. Assignment Final: 6 Branches Extended & Polished
# ---------------------------------------------------------
if chart_view == "Assignment Submission (6 Branches - Polished)":
    st.subheader("Final Assignment Graphic: Six Regional Branches")
    
    # Updated dataset with 2 additional categories (Central & Northwest) and updated figures
    data_final = pd.DataFrame({
        "Branch": ["North", "South", "East", "West", "Central", "Northwest"],
        "Sales": [96, 99, 98, 104, 101, 92]
    })
    
    # Key Metrics Callout
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Top Performing Branch", "West", "104 units (+4 vs South)")
    with col2:
        st.metric("Lowest Performing Branch", "Northwest", "92 units (-12 vs West)")
    with col3:
        st.metric("Average Branch Sales", f"{data_final['Sales'].mean():.1f} units")
        
    st.markdown("---")

    fig, ax = plt.subplots(figsize=(9, 4.8), dpi=150)
    
    # Pre-attentive highlight: West branch in distinctive coral-red (#D9381E), others in calm slate (#5C768D)
    colors = ["#D9381E" if b == "West" else "#78909C" for b in data_final["Branch"]]
    
    bars = ax.bar(
        data_final["Branch"],
        data_final["Sales"],
        color=colors,
        width=0.55,
        edgecolor=None
    )
    
    # Design Standards: Zero baseline to preserve proportion integrity
    ax.set_ylim(0, 120)
    ax.set_yticks(range(0, 121, 20))
    ax.set_ylabel("Sales Volume (units)", fontsize=11, labelpad=8, color="#37474F")
    
    # Direct data labels on bars (avoids eye travel to axis)
    for bar in bars:
        h = bar.get_height()
        is_max = (h == data_final["Sales"].max())
        ax.annotate(
            f"{int(h)}",
            xy=(bar.get_x() + bar.get_width() / 2, h),
            xytext=(0, 4),
            textcoords="offset points",
            ha="center", va="bottom",
            fontsize=10.5,
            fontweight="bold" if is_max else "normal",
            color="#B71C1C" if is_max else "#263238"
        )
        
    # Informative & action-oriented title
    ax.set_title(
        "West Branch Recorded the Highest Sales at 104 Units",
        fontsize=13.5,
        fontweight="bold",
        pad=16,
        loc="left",
        color="#212121"
    )
    
    # Remove chartjunk: top and right spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#CFD8DC")
    ax.spines["bottom"].set_color("#CFD8DC")
    
    # Subtle horizontal-only gridlines to aid height estimation
    ax.grid(axis="y", color="#ECEFF1", linestyle="-", linewidth=0.8)
    ax.set_axisbelow(True)
    
    # Tick parameters
    ax.tick_params(axis="x", labelsize=11, length=0, colors="#263238")
    ax.tick_params(axis="y", labelsize=10, colors="#546E7A")
    
    # Attribution and source note (Lesson 3 standard requirement)
    attribution_text = "Data: fictional practice values (2026) | Chart: Data Visualization Student"
    fig.text(0.12, -0.02, attribution_text, fontsize=9, color="#78909C", style="italic")
    
    fig.tight_layout()
    st.pyplot(fig, clear_figure=False)
    
    # Automatically save final screenshot
    chart_path = os.path.join(os.path.dirname(__file__), "final_chart.png")
    fig.savefig(chart_path, dpi=300, bbox_inches="tight")
    
    st.caption("Fictional practice data. Baseline begins at zero to preserve physical bar length proportionality.")

    # Design Review Section
    with st.expander("Lesson 3 Design Critique & Standards Evaluation", expanded=True):
        st.markdown(
            """
            #### How Design Standards Support Understanding:
            1. **Scale & Baseline Integrity:** The vertical axis starts at 0 and increments naturally by 20. The 13% variation between highest (104) and lowest (92) is accurately conveyed without artificial exaggeration.
            2. **Selective Color Use (Pre-attentive Salience):** The top-performing branch (West) is highlighted in coral-red (`#D9381E`), while other branches remain neutral slate (`#78909C`). This immediately draws attention without rainbow clutter.
            3. **Elimination of Chartjunk:** Heavy grey backgrounds, thick white gridlines, and ornamental borders were eliminated, maximizing the data-ink ratio.
            4. **Data Density & Readability (6 Categories):** Adding two branches (Central and Northwest) maintained optimal spacing and legibility without requiring angled text or sub-plots.
            5. **Explicit Attribution:** Clear attribution provided directly on the visual for source authenticity and credit.
            """
        )

# ---------------------------------------------------------
# 2. Baseline Lesson 1: Improved Chart (4 Branches)
# ---------------------------------------------------------
elif chart_view == "Lesson 1 Baseline: Improved Chart":
    st.subheader("Lesson 1 Baseline: Improved Bar Chart (4 Branches)")
    
    data = pd.DataFrame({
        "Branch": ["North", "South", "East", "West"],
        "Sales": [96, 99, 98, 100],
    })
    
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=150)
    bars = ax.bar(data["Branch"], data["Sales"], color="#4C78A8")
    for branch, bar in zip(data["Branch"], bars):
        if branch == "West":
            bar.set_color("#E07A3F")
            
    ax.set_ylim(0, 105)
    ax.set_yticks(range(0, 101, 20))
    ax.bar_label(bars, fmt="%.0f", padding=3)
    ax.set_title("West branch recorded the highest sales", fontsize=12, pad=10)
    ax.grid(axis="y", color="#DDDDDD", linewidth=0.7)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_ylabel("Sales (units)")
    
    fig.tight_layout()
    st.pyplot(fig, clear_figure=False)
    
    # Save baseline improved chart
    chart_path = os.path.join(os.path.dirname(__file__), "improved_chart.png")
    fig.savefig(chart_path, dpi=300, bbox_inches="tight")
    
    st.caption("Fictional practice data. The improved bar chart starts at zero.")

# ---------------------------------------------------------
# 3. Baseline Lesson 1: Cluttered Chart (4 Branches)
# ---------------------------------------------------------
else:
    st.subheader("Lesson 1 Baseline: Cluttered Bar Chart (Distorted & Over-decorated)")
    
    data = pd.DataFrame({
        "Branch": ["North", "South", "East", "West"],
        "Sales": [96, 99, 98, 100],
    })
    
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=150)
    bars = ax.bar(
        data["Branch"],
        data["Sales"],
        color=["#8FB9A8", "#D8B365", "#B2ABD2", "#5E3C99"]
    )
    # Distorting truncation: scale starts at 95 instead of 0
    ax.set_ylim(95, 101)
    ax.set_facecolor("#E8E8E8")
    ax.grid(True, which="both", color="white", linewidth=2)
    ax.set_title("SALES PERFORMANCE!!!", fontsize=13, fontweight="bold")
    ax.set_ylabel("Sales (units)")
    
    fig.tight_layout()
    st.pyplot(fig, clear_figure=False)
    
    # Save baseline cluttered chart
    chart_path = os.path.join(os.path.dirname(__file__), "cluttered_chart.png")
    fig.savefig(chart_path, dpi=300, bbox_inches="tight")
    
    st.warning(
        "**Perceptual Flaws in Cluttered Version:**\n"
        "- Truncated Y-Axis [95, 101]: Exaggerates a minor 4% difference (96 vs 100) to appear as if West is 500% larger than North.\n"
        "- Rainbow colors: Every bar has an arbitrary hue with no communicative meaning.\n"
        "- Heavy gray background & thick white grids create high-frequency visual noise (chartjunk)."
    )
