from collections import Counter

text = "The quick, brown fox. Jumps over the lazy dog!"
chars = text.lower()

counts = Counter(ch for ch in chars if ch.isalpha())          # ← 一行完成全部计数
print(counts.most_common(3))     # ← 直接取前 3，不用 sorted + lambda

