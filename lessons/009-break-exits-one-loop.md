# 009 · break 只跳一层，退出信号要用 return / break exits one loop only — signal the caller with return

## 中文

**场景**：简易计算器 CLI。用户在 `get_number()` 里输入 `exit` 想退出整个程序。

**我的错误代码**：

```python
def get_number():
    while True:
        try:
            user_input = input("Enter a number (or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting the program.")
                break            # ← 我以为这会退出整个程序
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    while True:
        user_input1 = get_number()   # 输入 exit → 拿到 None，但程序继续跑！
        user_input2 = get_number()   # 又弹提示要第二个数……
        ...
```

**现象**：输入 `exit` 后程序没有退出，继续要第二个数；再输入一次 `exit` 后还是要运算符，最终 `calculate(None, None, op)` **TypeError 崩溃**。

**分析**：`break` 只能跳出**包含它的最近一层循环**——这里是 `get_number()` 的 `while True`，不是 `main()` 的 `while True`。它**穿不过函数边界**。`break` 跳出循环后函数没有 `return`，隐式返回 `None`，`main()` 收到 `None` 却不知道"这是退出信号"，继续往下跑。

**根因**：函数和调用方之间**唯一的通信通道是返回值**。想让 `main()` 知道"用户要退出"，信号必须通过 `return` 层层传递——`break` 只是循环内部的指令，传不出去。

**教训**：
1. **`break` 跳一层循环，`return` 回到调用方**——功能不同，不能互换。
2. **函数间通信只能靠参数和返回值**。被调函数有"事件"要通知调用方（这里：用户想退出），用 `return` 传信号，调用方检查信号再决定是否退出。
3. 检查信号要立刻做：`if x is None: break`。

**修复**：

```python
def get_number():
    while True:
        try:
            user_input = input("Enter a number (or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting the program.")
                return None            # 信号：return，不是 break
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    user_input1 = get_number()
    if user_input1 is None:
        return                          # main 收到信号 → 真正退出
    ...
```

完整最终版见 [`code/week1/calculator.py`](../code/week1/calculator.py)。

---

## English

**Situation**: a CLI calculator. The user types `exit` in `get_number()` expecting the whole program to quit.

**My buggy code**: `break` inside `get_number()` when `exit` is read.

**Symptom**: typing `exit` did not quit — the program asked for a second number, then an operator, and finally crashed with `TypeError` from `calculate(None, None, op)`.

**Analysis**: `break` only exits the **nearest enclosing loop** — here `get_number()`'s `while True`, not `main()`'s. It **cannot cross the function boundary**. After `break`, the function ends without `return`, so it implicitly returns `None`; `main()` receives `None` but doesn't know it means "quit" and keeps running.

**Root cause**: the **only communication channel between a function and its caller is the return value**. For `main()` to know "the user wants to quit", the signal must travel through `return` — `break` is a loop-internal instruction that cannot leave the function.

**Lessons**:
1. **`break` exits one loop level; `return` goes back to the caller** — they are not interchangeable.
2. **Functions communicate only via parameters and return values.** When a callee has an event to report (here: user wants to quit), return a signal; the caller checks it and decides whether to exit.
3. Check the signal immediately: `if x is None: break`.

**Fix**: see the Chinese section above; the full final version is in [`code/week1/calculator.py`](../code/week1/calculator.py).

---

## 原对话摘录 / Original conversation excerpt

> 摘自学习者与 AI 助教的真实对话（2026-09-16）。这是第一篇带原对话摘录的复盘（格式约定见 `lessons/README.md`）。

**学习者贴出的第一版代码（节选，问题所在）**：

```python
def get_number():
    while True:
        try:
            user_input = input("Enter a number (or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting the program.")
                break          # ← 学习者原以为这会退出整个程序
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
```

**助教关键点评**：

> "这个 break 跳出的是 `get_number()` 自己的 `while True`，不是 `main()` 的 `while True`——它只跳一层，穿不过函数边界。break 之后没有 return，函数隐式返回 None，main 收到 None 却不知道这是'退出信号'，继续跑，最终 `calculate(None, None, op)` 直接 TypeError 崩溃。"

**学习者修复版的关键改动**：

```python
if user_input.lower() == 'exit':
    return None    # 用 return 传信号，而不是 break

# main() 里：
if user_input1 is None:
    return         # main 收到信号 → 真正退出整个程序
```

**助教总结**：

> "break 是'跳出循环'，return 是'回到调用方'。想让 main 知道'用户要退出'，信号只能通过 return 层层传递——被调函数 return → 调用方检查 → 再决定是否退出。"
