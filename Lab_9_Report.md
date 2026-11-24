# TFB3133 / TEB3133 Data Visualization
# Lab 9: Design Principles and Chartjunk — Comprehensive Report

---

## 1. Executive Summary & Lab Objective

- **Course:** TFB3133 / TEB3133 Data Visualization
- **Topic:** Lab 9 — Design Principles and Chartjunk
- **Source Slide Reference:** Lecture 2, *"Design Principles for Visualization"*
- **Core Concepts:** The Ten Design Standards, Data Integrity (Lie Factor & Axis Truncation), Eliminating Chartjunk (Maximizing the Data-Ink Ratio), Pre-attentive Color Attributes, and Source Attribution.

---

## 2. Comparison of the Two Views (Lesson 3.1)

### 2.1 Three Key Differences and Their Perceptual Effect on the Reader

| Design Feature | Cluttered Version | Improved Version | Perceptual Effect on the Reader |
| :--- | :--- | :--- | :--- |
| **1. Value Scale & Baseline** | Truncated Y-axis spanning $[95, 101]$ | Zero-anchored Y-axis spanning $[0, 105]$ (or $[0, 120]$ for 6 branches) | Truncating the axis magnifies a 4-unit gap into a massive visual chasm. Starting at zero provides an accurate representation of bar length relative to total sales magnitude. |
| **2. Color Usage** | Arbitrary rainbow palette (`#8FB9A8`, `#D8B365`, `#B2ABD2`, `#5E3C99`) | Neutral slate palette (`#4C78A8`) with a single warm accent (`#E07A3F`) for the leader | Rainbow colors imply non-existent categorical groupings and overwhelm visual memory. Selective accenting leverages pre-attentive processing to guide focus directly to the key insight. |
| **3. Non-Data Ink (Chartjunk)** | Heavy grey background (`#E8E8E8`), thick white gridlines, screaming all-caps title (`SALES PERFORMANCE!!!`) | White background, removed top/right spines, subtle horizontal grid lines (`#DDDDDD`), informative title | Eliminating chartjunk maximizes the data-ink ratio. The reader's cognitive effort is directed toward interpreting the data rather than filtering out visual noise. |

### 2.2 Mathematical Analysis of Axis Truncation & Apparent Difference

The sales values for the initial four branches are:
$$\text{North} = 96, \quad \text{South} = 99, \quad \text{East} = 98, \quad \text{West} = 100$$

- **Actual Relative Difference:**
  The true percentage difference between North (96) and West (100) is:
  $$\frac{100 - 96}{96} \times 100\% = \frac{4}{96} \times 100\% \approx 4.17\%$$
- **Apparent Difference with Truncated Axis $[95, 101]$:**
  Because the bars originate at a baseline of 95:
  - $\text{Apparent Height}(\text{North}) = 96 - 95 = 1 \text{ unit}$
  - $\text{Apparent Height}(\text{West}) = 100 - 95 = 5 \text{ units}$
  $$\text{Apparent Ratio} = \frac{5}{1} = 5.0 \quad (\mathbf{500\% \text{ larger!}})$$

**Conclusion:** The shortened vertical axis produces an apparent difference that is over **100 times larger** than the true relative difference ($500\%$ visual ratio vs. $4.17\%$ actual difference). This constitutes an extreme violation of Edward Tufte's **Data Integrity Principle** ($\text{Lie Factor} \gg 1$), severely misleading the audience into believing West vastly outperformed North when performance across branches was virtually identical.

---

## 3. Critique of Five Design Standards (Lesson 2 & 3)

### Standard 1: Scales
- **Cluttered:** Starts at 95. In bar charts, the visual quantity encoded is the physical length and area of the rectangle. Any non-zero baseline corrupts this 1:1 proportional relationship.
- **Improved:** Sets the value axis to zero ($[0, 105]$) with natural, uniform 20-unit increments ($0, 20, 40, 60, 80, 100$). This ensures bar lengths directly reflect actual sales volumes.

### Standard 2: Color
- **Cluttered:** Every single bar uses an unrelated hue (teal, ochre, lavender, purple). This introduces false categories and cognitive friction, as viewers wonder what each color signifies.
- **Improved:** Employs a restrained palette. The baseline bars are rendered in neutral slate blue/gray, while the focal data point (West branch) is rendered in warm coral-red. This uses color as a functional pre-attentive cue rather than decorative garnish.

### Standard 3: Chartjunk
- **Cluttered:** Saturated with ornamental chartjunk—heavy grey plot background, stark white gridlines across both dimensions, and redundant border frames.
- **Improved:** Adheres to Tufte's rule of maximizing the data-ink ratio. The background is clean white, top and right spines are removed, and only faint horizontal guidelines remain to assist vertical alignment without competing with the data bars.

### Standard 4: Text and Labels
- **Cluttered:** Features an uninformative, emotional title (`SALES PERFORMANCE!!!`) without stating what the chart shows. Viewers must mentally trace bar tops across thick grids to read values.
- **Improved:** Uses an informative, declarative headline (`West branch recorded the highest sales`). Direct numeric value labels (`ax.bar_label`) are placed at the end of each bar, allowing immediate numerical identification without axis scanning.

### Standard 5: Attribution
- **Cluttered:** Completely lacks source documentation, temporal context, and author credit, undermining credibility.
- **Improved:** Explicitly includes an italicized attribution footnote: `Data: fictional practice values (2026) | Chart: Data Visualization Student`, establishing source clarity and transparency.

---

## 4. Further Improvements & Category Extension (Lesson 3.2 & 3.3)

### 4.1 Expanding to Six Categories
To test visual scalability and data density, two additional regional branches were introduced:
- `Central`: $101 \text{ units}$
- `Northwest`: $92 \text{ units}$
- `West` (Updated): $104 \text{ units}$ (top branch)
- `South`: $99 \text{ units}$, `East`: $98 \text{ units}$, `North`: $96 \text{ units}$

### 4.2 Readability & Density Assessment
- **Bar Spacing & Layout:** With 6 categories, the horizontal layout remains clean and readable. The bar width was tuned to $0.55$, leaving ample white space between categories.
- **Label Orientation:** Branch names (`North`, `South`, `East`, `West`, `Central`, `Northwest`) are fully legible horizontally without needing vertical stacking or 45-degree rotation, adhering to the Readability standard.
- **Visual Threshold:** If the dataset expanded beyond 10–12 branches, a vertical bar layout would become crowded. In that scenario, pivoting to a horizontal bar chart (`barh`) or facet small multiples would be recommended to prevent label collision.

---

## 5. Summary of Visual Deliverables

| File | Resolution | Description |
| :--- | :--- | :--- |
| `cluttered_chart.png` | 300 DPI | Lesson 1 baseline chart exhibiting truncated axis, chartjunk, and rainbow colors. |
| `improved_chart.png` | 300 DPI | Lesson 1 baseline improved chart with zero baseline and single accent color. |
| `final_chart.png` | 300 DPI | Lesson 3 assignment final chart with 6 categories, direct annotations, and attribution. |

---

## 6. Reflection on Accuracy, Misinterpretation, and Verification (150–200 Words)

> Restoring a zero baseline to the vertical scale was the single most impactful change for improving data accuracy. In the truncated version, the arbitrary range of 95 to 101 exaggerated a minor 4.17% sales difference into an apparent 500% visual disparity, severely distorting proportional perception. Anchoring the axis at zero ensured that physical bar lengths faithfully represented the underlying quantities, upholding fundamental data integrity.
>
> However, a reader could still be misled if they interpret identical bar widths as indicating equal territory size or customer volume, or if they overlook that these figures represent static snapshots without temporal trends or variance. Furthermore, highlighting the top-performing branch in vibrant accent color risks drawing attention solely to the leader while obscuring systemic regional patterns.
>
> To verify the chart against its source data, I systematically cross-checked the annotated numeric labels directly against the Pandas DataFrame values, confirmed that relative pixel heights matched mathematical ratios, and ensured that the y-axis tick intervals incremented consistently. This rigorous verification process guaranteed that visual encodings communicated the exact empirical measurements without perceptual distortion.

*(Reflection Word Count: 180 words)*
