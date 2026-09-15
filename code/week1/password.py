# Password strength checker - L1 Day 4
# Fixed version (counting conditions); see lessons/004 for the boolean-logic bug.
password = input("Enter your password: ")

length = len(password) > 7
has_letter = any(c.isalpha() for c in password)
has_digit = any(c.isdigit() for c in password)
score = sum([length, has_letter, has_digit])

if score == 3:
    print("Password safety: strong")
elif score == 2:
    print("Password safety: medium")
else:
    print("Password safety: weak")
