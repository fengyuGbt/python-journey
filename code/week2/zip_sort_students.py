# zip + sorted by value - L2 Day 2
names = ["Alice", "Bob", "Carol", "Dave", "Eve"]
scores = [85, 58, 73, 61, 44]
students = dict(zip(names, scores))
ranked = sorted(students.items(), key=lambda x: x[1], reverse=True)
for name, score in ranked:
    print(f"{name}: {score}")
