# Self-introduction with type conversion - L1 Day 2
# input() always returns a string; int() converts it so we can do arithmetic.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My name is {name}, I am {age} years old, next year I will be {age + 1}.")
