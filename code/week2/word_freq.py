# Word frequency counter - L2 Day 1
# Final version: get() one-liner + lower() normalization + Top 5 by count.
text = "the quick brown fox jumps over the lazy dog the dog"
words = text.split()

word_count = {}
for word in words:
    word = word.lower()
    word_count[word] = word_count.get(word, 0) + 1

sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_word_count[:5]:
    print(f"{word}: {count}")
