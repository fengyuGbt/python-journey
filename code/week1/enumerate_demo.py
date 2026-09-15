# enumerate demo - L1 Day 5
# enumerate(names, start=1) gives (1, "Alice"), (2, "Bob"), ...
names = ["Alice", "Bob", "Carol"]
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")
