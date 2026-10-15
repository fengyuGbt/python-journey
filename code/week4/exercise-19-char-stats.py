def char_stats(text):
    ...  # 统计每个字符出现次数（过滤空白），返回 dict
    stats = {}
    text = text.replace(" ", "")  # 过滤空格
    for char in text:
        stats[char] = stats.get(char, 0) + 1
    return stats
# 验收：char_stats("hello world") → {'h':1,'e':1,'l':3,'o':2,'w':1,'r':1,'d':1}（空格被过滤）
print(char_stats("hello world"))
