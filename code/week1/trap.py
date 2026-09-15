# Type trap - L1 Day 2
# "5" is a string; the + operator cannot concatenate str with int.
# int("5") converts it to a number so arithmetic works: 5 + 3 = 8
print(int("5") + 3)
