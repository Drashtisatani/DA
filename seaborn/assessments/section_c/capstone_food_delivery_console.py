import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # never display charts interactively
import matplotlib.pyplot as plt
import seaborn as sns

NUMERIC_COLS = ['order_value', 'delivery_time_mins', 'rating']


def generate_dataset(n_rows=220, seed=11):
    """Generate the underlying food delivery dataset with NumPy (>= 200 rows)."""
    np.random.seed(seed)

    restaurant_names = ['Spice Villa', 'Curry House', 'Noodle Bar', 'Pizza Point', 'Sweet Tooth']
    cities = ['Mumbai', 'Delhi', 'Bengaluru']
    cuisine_types = ['North Indian', 'Chinese', 'Fast Food']

    df = pd.DataFrame({
        'restaurant_name': np.random.choice(restaurant_names, n_rows),
        'city': np.random.choice(cities, n_rows),
        'order_value': np.random.uniform(150, 900, n_rows),
        'delivery_time_mins': np.random.normal(30, 8, n_rows),
        'rating': np.random.normal(4.0, 0.7, n_rows).clip(1.0, 5.0),
        'cuisine_type': np.random.choice(cuisine_types, n_rows),
    })

    # Introduce some missing values to make the null-check step meaningful
    for col in NUMERIC_COLS:
        null_idx = np.random.choice(df.index, size=int(n_rows * 0.04), replace=False)
        df.loc[null_idx, col] = np.nan

    return df


def clean_dataset(df):
    """Check for and fill nulls in numeric columns before any analysis runs."""
    null_counts = df[NUMERIC_COLS].isna().sum()
    total_nulls = null_counts.sum()
    if total_nulls > 0:
        print(f"[startup] Found {total_nulls} null value(s) in numeric columns "
              f"({dict(null_counts[null_counts > 0])}) - filling with column medians.")
        for col in NUMERIC_COLS:
            df[col] = df[col].fillna(df[col].median())
    else:
        print("[startup] No null values found in numeric columns.")
    return df


def option_summary_statistics(df):
    """(1) Summary Statistics - primary technique: NumPy statistical functions."""
    print("\n--- Summary Statistics (NumPy) ---")
    for col in NUMERIC_COLS:
        values = df[col].to_numpy()
        print(f"{col}: min={np.min(values):.2f}  max={np.max(values):.2f}  "
              f"mean={np.mean(values):.2f}  median={np.median(values):.2f}  "
              f"std={np.std(values):.2f}")


def option_distribution_analysis(df):
    """(2) Distribution Analysis - primary technique: Matplotlib subplots."""
    print("\n--- Distribution Analysis (Matplotlib) ---")
    fig, axes = plt.subplots(1, len(NUMERIC_COLS), figsize=(15, 4.5))
    for ax, col in zip(axes, NUMERIC_COLS):
        ax.hist(df[col], bins=15, color='#4c9aff', edgecolor='black')
        ax.set_title(col)
        ax.set_xlabel(col)
        ax.set_ylabel('Frequency')
    fig.suptitle('Distribution Analysis - Numeric Columns')
    plt.tight_layout()
    plt.savefig('distribution_analysis.png', dpi=150)
    plt.close(fig)
    print("Saved chart: distribution_analysis.png (DPI 150)")


def option_correlation_heatmap(df):
    """(3) Correlation Heatmap - primary technique: Seaborn heatmap."""
    print("\n--- Correlation Heatmap (Seaborn) ---")
    corr = df[NUMERIC_COLS].corr()
    plt.figure(figsize=(6, 5))
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Heatmap - Numeric Columns')
    plt.tight_layout()
    plt.savefig('capstone_correlation_heatmap.png', dpi=150)
    plt.close()
    print("Saved chart: capstone_correlation_heatmap.png (DPI 150)")


def option_restaurant_performance(df):
    """(4) Restaurant Performance Report - primary technique: Pandas groupby."""
    print("\n--- Restaurant Performance Report (Pandas groupby) ---")
    report = (
        df.groupby('restaurant_name')
          .agg(
              mean_order_value=('order_value', 'mean'),
              mean_delivery_time=('delivery_time_mins', 'mean'),
              mean_rating=('rating', 'mean'),
              orders=('restaurant_name', 'count'),
          )
          .sort_values('mean_rating', ascending=False)
    )
    print(report.round(2).to_string())


def print_final_summary(df):
    """After exit: top 3 restaurants by mean rating, strongest correlated pair,
    and overall delivery time mean/std."""
    print("\n=================== FINAL SUMMARY REPORT ===================")

    top3 = (
        df.groupby('restaurant_name')['rating'].mean()
          .sort_values(ascending=False)
          .head(3)
    )
    print("Top 3 restaurants by mean rating:")
    for name, rating in top3.items():
        print(f"  {name}: {rating:.2f}")

    corr = df[NUMERIC_COLS].corr().abs()
    corr_vals = corr.to_numpy().copy()
    np.fill_diagonal(corr_vals, 0)
    corr = pd.DataFrame(corr_vals, index=corr.index, columns=corr.columns)
    max_pair = corr.stack().idxmax()
    max_val = corr.stack().max()
    print(f"\nNumeric column pair with highest absolute Pearson correlation: "
          f"{max_pair[0]} <-> {max_pair[1]} (|r| = {max_val:.3f})")

    delivery_time = df['delivery_time_mins'].to_numpy()
    print(f"\nOverall delivery time: mean = {np.mean(delivery_time):.2f} min, "
          f"std = {np.std(delivery_time):.2f} min")
    print("==============================================================")


def run_menu(df, auto_inputs=None):
    """Main menu loop. If auto_inputs is given, it's used instead of input()
    for automated testing."""
    input_iter = iter(auto_inputs) if auto_inputs is not None else None

    def get_input(prompt):
        if input_iter is not None:
            value = next(input_iter)
            print(prompt + value)
            return value
        return input(prompt)

    menu_text = (
        "\nFood Delivery Analytics Console\n"
        "  1. Summary Statistics\n"
        "  2. Distribution Analysis\n"
        "  3. Correlation Heatmap\n"
        "  4. Restaurant Performance Report\n"
        "  5. Exit\n"
        "Choose an option (1-5): "
    )

    while True:
        choice = get_input(menu_text).strip()
        if choice == '1':
            option_summary_statistics(df)
        elif choice == '2':
            option_distribution_analysis(df)
        elif choice == '3':
            option_correlation_heatmap(df)
        elif choice == '4':
            option_restaurant_performance(df)
        elif choice == '5':
            print("\nExiting menu...")
            break
        else:
            print("Invalid option - please choose 1-5.")

    print_final_summary(df)


if __name__ == "__main__":
    dataset = generate_dataset()
    dataset = clean_dataset(dataset)
    run_menu(dataset)
