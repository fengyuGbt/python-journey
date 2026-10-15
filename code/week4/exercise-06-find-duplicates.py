from collections import Counter
def find_duplicates(items,limit=None):
    ...  # 返回出现超过一次的元素，保持首次出现顺序
    count = Counter(items)
    duplicates = [item for item, c in count.items() if c > 1]
    return duplicates[:limit] if limit is not None else duplicates
# 验收：find_duplicates([3, 1, 2, 3, 4, 1, 5, 3]) → [3, 1]
print(find_duplicates([3, 1, 2, 3, 4, 1, 5, 3]))
print(find_duplicates([3, 3, 1, 1]))
print(find_duplicates([3, 1, 2, 3, 4, 1, 5, 3], limit=2))
