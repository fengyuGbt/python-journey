# Passed students via comprehension - L2 Day 2
students = {"Alice": 85, "Bob": 58, "Carol": 73, "Dave": 61, "Eve": 44}
passed = [name for name, score in students.items() if score >= 60]
print(passed)
