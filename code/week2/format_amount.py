# Amount formatting with thousands separator - L2 Day 3
number = input("Enter a number: ")
try:
    number = float(number)
    print(f"You entered the number: {number:,.2f}")
except ValueError:
    print("That's not a valid number.")
