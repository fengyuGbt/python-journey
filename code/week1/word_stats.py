# Word statistics - L1 Day 4
# Fixed version; see lessons/006 for the over-validation issue.
sentence = input("Enter a sentence: ")
while not sentence.strip():
    print("Empty input. Try again.")
    sentence = input("Enter a sentence: ")

words = sentence.split()
word_count = len(words)
char_count = sum(len(w) for w in words)      # letters only, no spaces
capitalized = [w.capitalize() for w in words]

print(f"Words: {word_count}")
print(f"Characters (no spaces): {char_count}")
print(f"Capitalized: {' '.join(capitalized)}")
