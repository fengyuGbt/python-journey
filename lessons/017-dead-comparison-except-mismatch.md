# 017 · 比较表达式当语句用是死代码；except 类型必须匹配 raise / Dead comparison; except type must match raise

## 中文

**背景**：第 3 周 Day 4（模块与包）练习 1——把计算器封装成 `calc.py` 模块，`use_calc.py` 导入使用。学习中踩了两个典型坑。

---

**坑 1：把比较表达式当成"执行"写**

初版 `evaluate` 的 else 分支：

```python
else:
    operation == '/'   # ← 死代码
    return divide(a, b)
```

`operation == '/'` 是一个**比较表达式**——它算出 `True` 或 `False`，但没有被 if 判断、没有被赋值，结果被直接丢弃，**这一行什么都不做**。于是 else 变成"管你输入什么一律除"。

**修复**：比较必须进条件：

```python
elif operation == '/':
    return divide(a, b)
else:
    raise ValueError("Invalid operation...")
```

**坑 2：except 类型与 raise 类型不匹配**

`calc.divide` 里 `raise ValueError("Denominator cannot be zero")`，`use_calc.py` 却写 `except ZeroDivisionError`——**接不住**。除零异常一路落到更靠前的 `except ValueError`，提示变成误导的"Invalid input. Please enter numeric values."

**修复（两条规则）**：
- **except 匹配的是 raise 的那个类型**：`raise ZeroDivisionError` 就用 `except ZeroDivisionError`。
- **用语义正确的原生类型**：除零在 Python 里原生就是 `ZeroDivisionError`（`1/0` 抛的就是它），所以 `divide` 应该 `raise ZeroDivisionError`，而不是借 `ValueError`。

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    return a / b
```

---

**正向成果：import 机制实证**

`calc.py` 顶层放 `print("module loaded")` 后：

```
>>> import calc
module loaded          # 第一次：找到文件并执行一遍
>>> import calc        # 第二次：什么都不打印
```

- `import` 会**从头执行一遍**目标文件 → 所以主逻辑要放 `main()` 里并用 `if __name__ == "__main__"` 保护。
- 第二次 `import` 不执行：模块已缓存进 `sys.modules`，直接返回缓存对象。

---

## English

**Context**: Week 3 Day 4 (modules & packages), Exercise 1 — packaging the calculator as `calc.py` and importing it from `use_calc.py`. Two classic traps.

---

**Trap 1: writing a comparison as a statement**

```python
else:
    operation == '/'   # dead code
    return divide(a, b)
```

`operation == '/'` evaluates to `True`/`False` but the result is never used — not in an `if`, not assigned. The line does nothing; the `else` branch unconditionally divides.

**Fix**: comparisons belong in conditions:

```python
elif operation == '/':
    return divide(a, b)
else:
    raise ValueError("Invalid operation...")
```

**Trap 2: except type must match the raised type**

`calc.divide` raised `ValueError`, while `use_calc.py` caught `except ZeroDivisionError` — it never matched. The exception fell through to the earlier `except ValueError`, printing the misleading "Invalid input. Please enter numeric values."

**Fix (two rules)**:
- **except matches whatever type you raise**: `raise ZeroDivisionError` → `except ZeroDivisionError`.
- **Use the semantically correct native type**: division by zero is natively `ZeroDivisionError` in Python (`1/0` raises it), so `divide` should raise that, not borrow `ValueError`.

---

**Positive result: import mechanism proven**

With `print("module loaded")` at the top of `calc.py`:

```
>>> import calc
module loaded          # first: find the file and execute it once
>>> import calc        # second: nothing printed
```

- `import` **executes the whole file once** — hence main logic goes into `main()` protected by `if __name__ == "__main__"`.
- The second `import` is a no-op: the module is cached in `sys.modules`, so Python returns the cached object.

---

## 原对话摘录 / Original conversation excerpt

> 摘自学习者与 AI 助教的真实对话（2026-10-07）。

**学习者**（初版 evaluate）：

> "def evaluate(a, b): ... else: operation == '/' return divide(a, b)"

**助教**：

> "`operation == '/'` 是一个比较表达式——它算出一个 True 或 False，但你没把结果用起来，所以这一行什么都不做。后果是 else 分支变成'管你输入什么，一律执行除法'。"

**学习者**（修好 evaluate 后，use_calc 加了 `except ZeroDivisionError`）：

> "except ZeroDivisionError as e: print(e)"

**助教**：

> "看你的 calc.py：divide 里 raise 的是 ValueError，但你抓的是 except ZeroDivisionError——类型对不上，接不住。核心规则：except 匹配的是 raise 的那个类型。"

**学习者修复 divide 后运行**：

> "10 / 0 → Denominator cannot be zero" — ✅ 除零被专门接住，提示准确

**学习者验证 import 机制**：

> ">>> import calc → module loaded；>>> import calc → （无输出）"

**助教**：

> "第二次 import 时，Python 发现 calc 已经在 sys.modules 缓存里，直接返回缓存对象，不再执行文件。"
