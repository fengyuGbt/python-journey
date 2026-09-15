# BMI calculator - L1 Day 2
# Fixed version; see lessons/002 for the unit-ambiguity bug in the prompt.
weight = float(input("Enter your weight in kg (e.g. 70): "))
height = float(input("Enter your height in meters (e.g. 1.77): "))
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.2f}")
