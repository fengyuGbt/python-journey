# Grade classifier - L1 Day 3
score = int(input("Enter your score (0-100): "))

if 85 <= score <= 100:
    print("Excellent")
elif 70 <= score < 85:
    print("Good")
elif 60 <= score < 70:
    print("Pass")
elif 0 <= score < 60:
    print("Fail")
else:
    print("Score out of range, please enter 0-100.")
