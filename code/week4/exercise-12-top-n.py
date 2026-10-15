def top_n(d, n):
    ...  # 按值降序，返回前 n 个 (key, value)
    for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)[:n]:
        yield (k, v)

# 验收：top_n({"a": 3, "b": 8, "c": 5}, 2) → [("b", 8), ("c", 5)]
print(list(top_n({"a": 3, "b": 8, "c": 5}, 2)))

def top_n_alt(d, n):
    return sorted(d.items(), key=lambda item: item[1], reverse=True)[:n]
