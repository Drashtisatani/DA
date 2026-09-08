# Section D — AI-Augmented Learning: Submission Notes

## 1. Exact prompt given to the AI tool

> "Write a Python program that generates a synthetic food delivery dataset with at least 5
> numeric columns and one categorical column (cuisine_type) using NumPy, loaded into a Pandas
> DataFrame. Then produce a Seaborn pairplot of all numeric columns, coloured by the categorical
> column, and save it as a PNG file. Also compute the Pearson correlation matrix and display it
> as a Seaborn heatmap with annotated cell values and a diverging colour palette, exported as a
> separate PNG file at DPI 200 with a descriptive filename."

## 2. Code (clearly marked, provided as separate files)

- **AI's original code:** `section_d_ai_original.py`
- **My corrected version:** `section_d_corrected.py`

## 3. What changed and why (bug/limitation found during testing without AI)

The AI's script generates `cuisine_type` with a ~10% chance of `None` (simulating real-world
missing data) and passes it straight into `sns.pairplot(df, hue='cuisine_type')`. Running it
didn't crash or print any error — but it silently **dropped every row with a null `cuisine_type`
from all pairplot panels**. Verified directly: with 150 generated rows, 14 ended up with a null
`cuisine_type`, and only 136 of 150 points were actually rendered (checked by counting the
scatter collection offsets). No warning was printed, so this would be easy to miss and would
quietly bias any conclusions drawn from the plot. The fix checks `cuisine_type` for nulls before
plotting, prints how many rows are affected, and fills them with an explicit `'Unknown'` category
so every row still appears in the pairplot instead of vanishing unannounced. The rest of the
AI's script was correct as generated — the heatmap already used `dpi=200` and a diverging
palette per the brief — so I renamed its output to a more descriptive filename
(`food_delivery_correlation_heatmap_200dpi.png`) while leaving that part of the logic untouched.
