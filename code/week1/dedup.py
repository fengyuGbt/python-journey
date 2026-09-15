# Deduplicate and sort descending - L1 Day 5
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
unique = sorted(set(numbers), reverse=True)
print(f"Original: {numbers}")
print(f"Unique (descending): {unique}")
