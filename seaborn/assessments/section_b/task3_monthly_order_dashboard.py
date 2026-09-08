import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)s

months = np.arange(1, 13)
total_orders = np.random.randint(1000, 5001, 12)
avg_order_value = np.random.uniform(200, 400, 12)
monthly_revenue = total_orders * avg_order_value
delivery_time_mean = 28
delivery_time_std = 4
simulated_delivery_times = np.random.normal(delivery_time_mean, delivery_time_std, 500)

fig, axes = plt.subplots(1, 3, figsize=(19, 5.5))
fig.suptitle('Food Delivery Platform - Monthly Performance Dashboard', fontsize=15, fontweight='bold')

# Subplot 1: Line chart of total orders per month, annotated points
ax0 = axes[0]
ax0.plot(months, total_orders, marker='o', color='#1f77b4')
for m, v in zip(months, total_orders):
    ax0.annotate(str(v), xy=(m, v), xytext=(0, 8), textcoords='offset points',
                 ha='center', fontsize=8)
ax0.set_title('Total Orders per Month')
ax0.set_xlabel('Month')
ax0.set_ylabel('Total Orders')
ax0.set_xticks(months)

# Subplot 2: Bar chart of monthly revenue, colour-coded vs Rs 8,00,000 threshold
ax1 = axes[1]
threshold = 800000
bar_colors = ['green' if rev > threshold else 'red' for rev in monthly_revenue]
ax1.bar(months, monthly_revenue, color=bar_colors)
ax1.axhline(threshold, color='black', linestyle='--', linewidth=1.2,
            label='Rs 8,00,000 threshold')
ax1.set_title('Monthly Revenue')
ax1.set_xlabel('Month')
ax1.set_ylabel('Revenue (Rs)')
ax1.set_xticks(months)
ax1.legend()

# Subplot 3: Histogram of simulated delivery times with mean line
ax2 = axes[2]
ax2.hist(simulated_delivery_times, bins=15, color='#4c9aff', edgecolor='black')
sample_mean = simulated_delivery_times.mean()
ax2.axvline(sample_mean, color='red', linestyle='--', linewidth=1.5, label=f'Mean = {sample_mean:.1f} min')
ax2.set_title('Delivery Time Distribution (500 simulated deliveries)')
ax2.set_xlabel('Delivery Time (min)')
ax2.set_ylabel('Frequency')
ax2.legend()

plt.tight_layout()
plt.savefig('food_delivery_dashboard.png', dpi=150)
plt.close()

print('Total orders per month:', total_orders.tolist())
print('Monthly revenue (Rs):', np.round(monthly_revenue, 2).tolist())
print(f'Simulated delivery time mean: {sample_mean:.2f} min (std used to generate: {delivery_time_std})')
print('Saved chart: food_delivery_dashboard.png (DPI 150)')
