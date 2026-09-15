# Number guessing game v1 - L1 Day 3
# Fixed version; see lessons/003 for the "no win message" bug.
import random

secret = random.randint(1, 100)

for attempt in range(1, 8):
    try:
        guess = int(input("Enter a number between 1 and 100: "))
    except ValueError:
        print("Please enter an integer.")
        continue
    if guess == secret:
        print(f"Congratulations! You guessed it in {attempt} tries. Answer: {secret}")
        break
    elif guess > secret:
        print("Too high")
    else:
        print("Too low")
else:
    print(f"Sorry, 7 tries used up. The answer was {secret}.")
