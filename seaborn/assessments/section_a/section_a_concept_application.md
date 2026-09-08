# Section A — Concept Application
---

## S1 — NumPy Vectorisation vs For-Loop (Delivery Fee Calculator)

**Why vectorisation is technically superior:** a Python `for`-loop over 50,000 elements pays the interpreter's per-iteration overhead every single time — type-checking each element, dispatching a Python-level arithmetic operation, boxing/unboxing values, and appending to a list one at a time. NumPy vectorisation instead pushes the entire computation down into pre-compiled, contiguous-memory C loops (often further optimised with SIMD instructions), so the interpreter is only invoked once for the whole array rather than 50,000 times. For an array this size, that difference is typically one to two orders of magnitude in speed, with lower memory churn since no intermediate Python list is being grown.

**What broadcasting allows:** broadcasting lets a single scalar (`Rs 5`) be treated as if it were an array of the same shape as `distances`, without NumPy actually allocating and copying that value 50,000 times in memory. Internally, NumPy just reuses the scalar across every element during the vectorised operation, so `fee = 20 + 5 * distances` computes all 50,000 fees in one expression with no explicit replication or looping needed.

**Where a Python loop is still necessary:** when each iteration depends on external, non-vectorisable work — for example, calling an external pricing API per order, applying business logic with complex branching that differs per row in a way that can't be expressed as array-wide boolean masks, or when the computation is inherently sequential (each result depends on the *previous* result, like a running total with path-dependent logic that plain cumulative NumPy functions can't express). In those cases a loop (or `apply()`, which is really just a disguised loop) is unavoidable.

---

## S2 — groupby() + agg() vs Manual Per-Restaurant Looping

**Why groupby()/agg() is correct:** filtering the DataFrame once per restaurant inside a loop re-scans the *entire* DataFrame on every iteration — for *k* restaurants that's roughly O(n × k) work. `groupby()` instead does a single pass to bucket rows by `restaurant_name`, then `agg()` computes all requested statistics per bucket using Pandas' optimised (Cython-backed) aggregation routines — one O(n) pass total. It's also far less error-prone: no manually maintained accumulator variables or reset-per-loop bugs.

**Method chain:**
```python
summary = df.groupby('restaurant_name').agg(
    avg_order_value=('order_value', 'mean'),
    avg_delivery_time=('delivery_time_mins', 'mean'),
    avg_rating=('rating', 'mean')
)
```

**What the resulting index represents:** after this groupby, the DataFrame's index is no longer the default `RangeIndex` — it becomes `restaurant_name` itself, with one row per unique restaurant. Each row is now *labelled* by the restaurant it summarises rather than by row position (unless `.reset_index()` is called afterward to push `restaurant_name` back into a regular column).

---

## S3 — Choosing Chart Types for a 3-Part Monthly Report

| Metric | Chart type | Why |
|---|---|---|
| (a) Total orders per month over a year | **Line chart** | It's a time series over 12 sequential, ordered periods — a line makes the month-to-month trend and any seasonality visible. |
| (b) Proportion of orders by cuisine type | **Pie chart** (bar chart is a reasonable alternative) | This is a parts-of-a-whole comparison across a small number of categories (4) — pie charts are built for exactly that framing, though a bar chart would make precise value comparisons easier if the audience needs to compare cuisines closely rather than just see relative share. |
| (c) Distribution of delivery times | **Histogram** | Delivery time is a continuous numeric variable — a histogram is the standard way to show how values are spread across ranges/bins. |

**Configuring `plt.subplots()`:** `fig, axes = plt.subplots(1, 3, figsize=(18, 5))` — one row, three columns, giving each chart its own `Axes` (`axes[0]`, `axes[1]`, `axes[2]`) side by side in a single figure.

**Should the x-axis be shared?** **No.** `sharex=True` forces all three subplots onto a common x-axis domain, but here the three x-axes mean completely different things — months (ordinal time), cuisine categories (nominal labels), and delivery-time bins (continuous numeric ranges). Sharing an axis only makes sense when subplots represent the same underlying variable; forcing these three together would produce a meaningless combined axis.

---

## S4 — Using plt.annotate() to Mark the Spike Day

**Approach:** find the index of the peak with `peak_idx = np.argmax(order_volumes)`, then pull `peak_day = days[peak_idx]` and `peak_value = order_volumes[peak_idx]`. Then:
```python
plt.annotate(
    f'Day {peak_day}: {peak_value}',
    xy=(peak_day, peak_value),
    xytext=(peak_day, peak_value + 200),
    arrowprops=dict(facecolor='black', arrowstyle='->')
)
```

**Two parameters and what they control:**
- **`xy`** — the actual data coordinate being pointed *at* (the peak point itself). This is what the arrow's tip touches.
- **`xytext`** — where the annotation *text* is drawn, usually offset from `xy` so the label doesn't sit directly on top of (and obscure) the data point.
- *(bonus)* **`arrowprops`** — a dict controlling whether an arrow is drawn at all, and its style (color, arrow head shape via `arrowstyle`, line width) connecting `xytext` to `xy`.

---

## S5 — Boxplot vs Violinplot for Ratings by Restaurant Category

**Recommendation: `sns.boxplot()`.**

Two reasons specific to this dataset:
1. **The rating scale is discrete (1–5), not continuous.** A violin plot's shape comes from a kernel density estimate, which smooths discrete integer values into a continuous curve — implying gradations between, say, 3 and 4 that don't actually exist in the data. That smoothing can visually mislead more than it clarifies for a 5-point discrete scale.
2. **The manager specifically wants to know about outliers.** A boxplot has an explicit, standard convention for this — points beyond 1.5×IQR from the quartiles are drawn individually as outlier markers. A violin plot has no equivalent built-in outlier flag; you'd have to eyeball where the density trails off, which is far less precise for a direct "does this category have more extreme outliers" question.

**When violinplot would be preferable instead:** if the manager cared about the *overall shape* of ratings within each category — e.g., whether a category is bimodal (many 1-star and many 5-star ratings, few in between) rather than a single central cluster — a violin plot's density curve reveals that multi-peaked structure directly, which a boxplot's five-number summary would completely hide (two very different distributions can produce nearly identical boxplots).

---

## S6 — Seaborn Correlation Heatmap for Multicollinearity Screening

**Approach:** compute `corr_matrix = df.corr()` (Pearson by default) across the 8 numeric columns, then `sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)`.

**What the colour scale represents:** it encodes both the strength and direction of each pairwise correlation using a **diverging** palette — a neutral/light colour at 0 (no relationship), trending toward one colour extreme (e.g., dark red) as correlation approaches +1, and the opposite extreme (e.g., dark blue) as it approaches −1. This lets you scan the whole grid visually and spot concerning cells without reading every number.

**Reading a specific cell:** for example, a cell at the intersection of `distance_km` and `delivery_time_mins` showing `0.82` means those two features move together strongly and positively — orders with a longer distance tend to also have a longer delivery time, and vice versa.

**Threshold for flagging multicollinearity:** conventionally **|r| > 0.8** (sometimes 0.7, depending on how conservative the team wants to be). That threshold is chosen because once two features are correlated that strongly, they carry largely redundant information — including both in a regression model doesn't add real predictive signal, but it does inflate the variance of the coefficient estimates (the model struggles to attribute effect to one variable vs. the other), making coefficients unstable and harder to interpret. 0.8 is a widely-used rule of thumb that balances catching genuinely problematic overlap without flagging every mild, expected relationship.
