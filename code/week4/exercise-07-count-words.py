from collections import Counter
import re

def count_words(text):
    ...  # 小写、按空白拆、去标点，返回 {word: count}
    return Counter(re.findall(r'\b\w+\b', text.lower()))

# 验收：count_words("Hello world hello python hello") → {'hello': 3, 'world': 1, 'python': 1}
print(count_words("Hello, world! Hello."))     # {'hello': 2, 'world': 1}
print(count_words("Hello world hello python hello"))  # 原用例也要保持通过