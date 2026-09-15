# QA · `while True` 是什么？为什么用它？/ What is `while True` and why use it?

## 中文

**问题**：`while True` 是什么？`choose_difficulty()` 里为什么要用它？

**回答**：

`while True` 是**无限循环**——条件永远是 `True`，循环体会一直执行，直到遇到 `break`（跳出循环）或 `return`（跳出函数）。

**典型用途**：**"问到合法为止"的输入校验**。比如选择难度，用户可能输 1/2/3，也可能输 `abc`、`99`。函数必须保证：**不拿到合法输入，绝不结束**。

```python
def choose_difficulty():
    while True:
        level = input("Choose difficulty (1/2/3): ")
        if level == "1":
            return random.randint(1, 50), 50, 10   # 合法 → return，函数结束
        if level == "2":
            return random.randint(1, 100), 100, 7
        if level == "3":
            return random.randint(1, 200), 200, 5
        print("Invalid choice.")                    # 非法 → 回到循环开头再问
```

流程：
- 用户输 `2` → 命中 `return` → 函数结束，循环随之消失
- 用户输 `abc` → 三个 `if` 都不中 → 打印提示 → **回到顶部再问**

**和递归对比**：有人用 `return choose_difficulty()` 处理非法输入（递归）。输错 1000 次就 RecursionError。`while True` 只是回到循环开头，**不调用自己，不累积栈**。

**唯一的坑**：`while True` 里必须有退出路径（`break`/`return`）。写之前问自己："什么情况下它会结束？"

---

## English

**Question**: what is `while True`, and why does `choose_difficulty()` use it?

**Answer**:

`while True` is an **infinite loop** — the condition is always `True`, so the body keeps running until `break` (leave the loop) or `return` (leave the function).

**Typical use**: **"ask until valid" input validation**. A user may type 1/2/3 — or `abc`, `99`. The function must guarantee: **it never ends until it gets valid input.**

Flow:
- User types `2` → hits `return` → function ends, loop disappears
- User types `abc` → no `if` matches → prints a hint → **loops back to the top and asks again**

**vs recursion**: some people write `return choose_difficulty()` on invalid input (recursion). 1000 bad inputs → RecursionError. `while True` just restarts the loop — **no self-calls, no growing stack.**

**The one trap**: `while True` must contain an exit path (`break`/`return`). Before writing it, ask: "what will end this loop?"
