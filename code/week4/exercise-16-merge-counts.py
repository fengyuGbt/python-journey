def merge_counts(d1, d2):
    ...  # 相同单词计数相加，返回新 dict，不改入参
    result = d1.copy()
    for k, v in d2.items():
        result[k] = result.get(k, 0) + v
    return result
# 验收：merge_counts({"a": 2, "b": 1}, {"b": 3, "c": 4}) → {"a": 2, "b": 4, "c": 4}
print(merge_counts({"a": 2, "b": 1}, {"b": 3, "c": 4}))
