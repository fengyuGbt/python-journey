# Number guessing game v2 - L1 Weekend Project
# Fixed version; see lessons/004 (recursion), 005 (exit), 007 (format), 008 (leaked answer).
import random


def choose_difficulty():
    """Ask until a valid choice is given. Returns (secret, upper, max_guesses)."""
    while True:
        level = input("Choose difficulty (1 easy / 2 medium / 3 hard): ")
        if level == "1":
            return random.randint(1, 50), 50, 10
        elif level == "2":
            return random.randint(1, 100), 100, 7
        elif level == "3":
            return random.randint(1, 200), 200, 5
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


def play_round(secret, upper, max_guesses):
    """Play one round. Invalid input does not cost a guess."""
    remaining = max_guesses
    while remaining > 0:
        try:
            guess = int(input(f"Enter a number (1-{upper}): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if guess < 1 or guess > upper:
            print(f"Out of range. Enter a number between 1 and {upper}.")
            continue
        if guess < secret:
            print("Too low!")
            remaining -= 1
        elif guess > secret:
            print("Too high!")
            remaining -= 1
        else:
            score = remaining * 10
            used = max_guesses - remaining + 1
            print(f"Congratulations! You got it in {used} tries. Score: {score}")
            return
    print(f"Out of guesses. The answer was {secret}. Score: 0")


def main():
    while True:
        secret, upper, guesses = choose_difficulty()
        play_round(secret, upper, guesses)
        if input("Play again? (y/n): ").lower() != "y":
            break


if __name__ == "__main__":
    main()
