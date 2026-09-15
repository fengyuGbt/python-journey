# Class score statistics - L1 Day 5
# sum() + generator counts how many booleans are True (True == 1).
scores = [45, 77, 65, 89, 98]
max_score = max(scores)
min_score = min(scores)
avg_score = sum(scores) / len(scores)
passed = sum(score >= 60 for score in scores)

print(f"Maximum score: {max_score}")
print(f"Minimum score: {min_score}")
print(f"Average score: {avg_score:.1f}")
print(f"Number of scores >= 60: {passed}")
