def dedup_keep_order(items):
    ...  # 去掉重复，保持首次出现顺序
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
# 验收：dedup_keep_order([3, 1, 3, 2, 1, 4]) → [3, 1, 2, 4]
print(dedup_keep_order([3, 1, 3, 2, 1, 4]))
