# 出错时：返回 None / 异常冒泡 / raise？+ raise 后面的代码还执行吗 / Return None, raise, or let it bubble? What runs after raise?

## 中文

学习 `safe_divide()` 时产生的两个问题：

### 问题 1：`raise` 之后的代码还执行吗？

```python
def check_age(age):
    if age < 0:
        raise ValueError("年龄不能为负")
        print("这行永远不执行")     # ❌ 到不了
        return "这也到不了"          # ❌ 到不了
    return age                       # age < 0 时也到不了
```

**不执行。`raise` 一出，函数立刻终止**——之后的任何代码都是死代码。异常沿调用链往上抛，直到被 `except` 接住，或没人接就程序崩溃。

`raise` 和 `return` 是"兄弟"，都会结束函数，区别是：`return` 正常结束（带着值），`raise` 异常结束（带着错误往上抛）。

### 问题 2：出错时可以不返回 None 吗？

可以，三种方案，按场景选：

| 方案 | 写法 | 调用方怎么判断 | 适合 |
|---|---|---|---|
| ① 返回 None（哨兵值） | 出错分支 `return None` | `if result is None:` | 简单工具函数 |
| ② 异常冒泡（不接） | 不写 except，直接让异常往上抛 | 调用方自己 `try/except` | 调用方想自己决定怎么处理 |
| ③ raise 自定义异常 | `raise ZeroDivisionError("...")` | `except ZeroDivisionError as e:` | 错误需要带详细信息 |

**注意**：函数不写 `return` 默认就返回 `None`——出错分支打印完提示自然结束，返回值就是 None，不需要额外写。

### 附：`"abc" / 2` 报什么异常？

`TypeError`（类型不匹配），不是 `ValueError`。如果想接受字符串数字 `"10"`，先 `float()` 转换，转换失败才报 `ValueError`：

```python
try:
    a = float(a); b = float(b)
    result = a / b
except ValueError:        # 非数字
    ...
except ZeroDivisionError: # 除零
    ...
```

---

## English

Two questions from `safe_divide()`:

### Q1: Does code after `raise` run?

No. `raise` terminates the function immediately — everything after it is dead code. The exception bubbles up the call chain until an `except` catches it, or the program crashes.

`raise` and `return` are siblings: both end the function, but `return` ends normally (with a value), `raise` ends abnormally (throwing the error upward).

### Q2: Can I skip returning None on error?

Yes, three patterns:

| Pattern | Caller checks | When |
|---|---|---|
| Return None (sentinel) | `if result is None:` | simple utility |
| Let it bubble (no except) | caller wraps in `try/except` | caller owns the handling |
| raise a custom error | `except XError as e:` | error needs detail |

Note: a function with no `return` implicitly returns `None` — an error branch that just prints and ends already returns None.

### Bonus: what does `"abc" / 2` raise?

`TypeError` (type mismatch), not `ValueError`. To also accept numeric strings like `"10"`, convert with `float()` first — a failed conversion raises `ValueError`.

---

## 原对话摘录 / Original conversation excerpt

> 摘自学习者与 AI 助教的真实对话（2026-10-06）。

**学习者**：

> "这个还会返回 age？"（check_age 中 raise 后的 return）

**助教**：

> "不会。raise 一出，函数立刻终止——return age 根本执行不到。raise 和 return 是兄弟：return 正常结束，raise 异常结束往上抛。"

**学习者**：

> "返回 None？不返回 none 行不"

**助教**：

> "可以。不写 return 的函数默认就返回 None。三种方案：① return None 哨兵值 ② 异常冒泡 ③ raise 自定义异常。None 是给调用方判断成败的信号。"
