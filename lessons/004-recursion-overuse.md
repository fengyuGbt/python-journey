# 004 · 递归滥用 / Recursion overuse

## 中文

**场景**：猜数字 v2。非法输入（非数字）或"再来一局？"都用了**递归**处理。

**我的错误代码**：

```python
def play_round(secret, max_guesses):
    try:
        guess = int(input(...))
    except ValueError:
        print("输入无效")
        return play_round(secret, max_guesses)   # ← 递归
    ...

def main():
    ...
    if input("再来一局？") == "y":
        return main()                            # ← 递归
```

**风险**：Python 递归深度上限约 1000。用户连续输错 1000 次（或者一直玩）→ **RecursionError 崩溃**。

**分析**：递归的适用场景是"问题天然分层"（如树的遍历）。这里只是"重新问一次"，用循环更自然：**循环不会堆积调用栈。**

**根因**：知道递归这个工具，但**选错了工具**。判断标准：这个操作是"重复做同一件事"还是"分解成更小的同类问题"？前者用循环，后者用递归。

**教训**：
1. **输入校验、菜单重选、再来一局 = 循环，不是递归。**
2. 递归滥用是"看过很多资料但没写过代码"的典型症状——工具都认识，场景用不对。
3. 写完问自己："这段会无限增长吗？" 递归 + 用户输入 = 会。

**修复**（用 `while` + `continue`）：

```python
while remaining > 0:
    try:
        guess = int(input("请输入数字："))
    except ValueError:
        print("输入无效，请重新输入")   # 不扣次数、不递归
        continue
    ...
```

---

## English

**Situation**: in guessing game v2, both "invalid input" and "play again?" were handled with **recursion**.

**Risky code**: `return play_round(...)` on ValueError and `return main()` on "play again".

**Risk**: Python's recursion limit is ~1000. After 1000 bad inputs (or a long session) → **RecursionError crash**.

**Analysis**: recursion fits "naturally hierarchical" problems (e.g. tree traversal). Here we just need to "ask again" — a loop is the natural tool, and **loops don't grow the call stack**.

**Root cause**: I knew the tool (recursion) but **picked the wrong tool**. Test: is this "repeat the same thing" (→ loop) or "decompose into smaller identical problems" (→ recursion)?

**Lessons**:
1. **Input validation, menu reselection, "play again" = loop, not recursion.**
2. Recursion overuse is a classic symptom of "read a lot, wrote little" — you know all the tools, but misapply them.
3. Ask: "can this grow without limit?" Recursion + user input = yes.
