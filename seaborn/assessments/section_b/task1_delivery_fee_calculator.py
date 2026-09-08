import numpy as np

# Generate 25 random delivery distances between 1.0 km and 15.0 km, seed=42
np.random.seed(42)
distances = np.random.uniform(1.0, 15.0, 25)

# Vectorised fee calculation: fee = Rs 20 + Rs 5 x distance
fees = 20 + 5 * distances

# Boolean indexing: orders where fee exceeds Rs 60
high_fee_mask = fees > 60
high_fee_distances = distances[high_fee_mask]
high_fee_fees = fees[high_fee_mask]

print("All distances (km):")
print(np.round(distances, 2))
print("\nAll fees (Rs):")
print(np.round(fees, 2))

print(f"\nOrders with delivery fee > Rs 60 ({high_fee_mask.sum()} orders):")
for d, f in zip(high_fee_distances, high_fee_fees):
    print(f"  distance = {d:.2f} km  ->  fee = Rs {f:.2f}")

print("\nFee array statistics:")
print(f"  Minimum : Rs {np.min(fees):.2f}")
print(f"  Maximum : Rs {np.max(fees):.2f}")
print(f"  Mean    : Rs {np.mean(fees):.2f}")
print(f"  Std Dev : Rs {np.std(fees):.2f}")
