def apply_all(funcs, x):
    ...  # 依次把每个函数作用到结果上
    for f in funcs:
        x = f(x)
    return x

f1 = lambda n: n + 1
f2 = lambda n: n * 2
# 验收：f1 = lambda n: n + 1; f2 = lambda n: n * 2
# apply_all([f1, f2], 5) → 12（先 +1=6，再 *2=12）
print(apply_all([f1, f2], 5))
