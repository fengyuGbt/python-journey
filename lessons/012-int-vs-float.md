# 012 · int() 拒绝小数 / int() rejects decimals

## 中文

**场景**：L2 Day 3 练习②（金额格式化），输入 `1234567.891`，要求输出 `1,234,567.89`。

**错误代码**：

```python
number = int(number)          # ❌
print(f"You entered the number: {number:,.2f}")
```

**运行结果**：输入 `1234567.891` 直接抛 `ValueError` 走 except 分支；就算输入整数 `1234567`，输出也是 `1,234,567.00` 而不是 `1,234,567.89`。

**原因**：
- `int("1234567.891")` → **ValueError**。`int()` 只接受"整数形式的字符串"（`"123"`），带小数点就拒绝。
- 用 `int()` 后 `.2f` 对整数格式化只会补零（`.00`）。

**教训**：`int()` vs `float()` 的选择规则——
- `int()`：计数、索引、整数操作。
- `float()`：**金额、测量值、除法结果——凡是可能有小数的一律用 `float()`**。

**修复**（改一个词）：

```python
number = float(number)        # ✅
print(f"{number:,.2f}")       # 1234567.891 → 1,234,567.89
```

---

## English

**Situation**: L2 Day 3 exercise ② (amount formatting), input `1234567.891`, expected output `1,234,567.89`.

**Wrong code**:

```python
number = int(number)
print(f"You entered the number: {number:,.2f}")
```

**What happened**: `1234567.891` raised `ValueError` and fell into the except branch; even with an integer input, the output was `1,234,567.00`, not `1,234,567.89`.

**Why**: `int("1234567.891")` → **ValueError**. `int()` only accepts integer-form strings (`"123"`); a decimal point is rejected. And `.2f` on an int just pads zeros.

**Lesson**: choose the converter by the value's nature:
- `int()`: counts, indexes, integer operations.
- `float()`: **amounts, measurements, division results — anything that may have a decimal part**.

**Fix** (one word):

```python
number = float(number)
print(f"{number:,.2f}")   # 1234567.891 → 1,234,567.89
```

---

## 原对话摘录 / Original conversation excerpt

> 摘自学习者与 AI 助教的真实对话（2026-09-19）。

**学习者贴出的第一版（用 int() 转换）**：

```python
number = input("Enter a number: ")
try:
    number = int(number)
    print(f"You entered the number: {number:,.2f}")
except ValueError:
    print("That's not a valid number.")
```

**助教关键点评**：

> "❌ 有 bug——而且正好踩在题目的陷阱上：题目给 `1234567.891` 带小数，就是考你 `int()` 和 `float()` 的区别。`int('1234567.891')` 会直接 ValueError，题目要求的输入根本进不了格式化那一步。`int()` 只认整数，`float()` 认小数和整数——凡是可能有小数的一律用 `float()`。"

**学习者修正版**：

```python
number = input("Enter a number: ")
try:
    number = float(number)
    print(f"You entered the number: {number:,.2f}")
except ValueError:
    print("That's not a valid number.")
```
