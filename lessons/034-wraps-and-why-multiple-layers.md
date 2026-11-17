# 034 — `functools.wraps` 有什么用，为什么要包那么多层

> Week 6 · Day 2 追加提问 · 2026-11-17

## 两个问题

1. `functools` 里的 `wraps` 到底有什么用？
2. 装饰器为什么要包那么多层，少一层不行吗？

---

## A. `functools.wraps` 的作用

### 一句话

让包装后的函数在**展示层面**仍然像原函数：名字、文档、签名都不丢。

### 实测对比

同一个原函数，不加 wraps 与加 wraps：

| 检查项 | 不加 wraps | 加 wraps |
|---|---|---|
| `__name__` | `wrapper` | `add2` |
| `__doc__` | `None` | `add two numbers` |
| `inspect.signature` | `(*args, **kwargs)` | `(a, b)` |
| `__wrapped__` | 不存在 | 指向原函数 |

实测输出（不加 wraps）：

```text
name      : wrapper
doc       : None
signature : (*args, **kwargs)
module    : __main__
```

实测输出（加 wraps）：

```text
name      : add2
doc       : add two numbers
signature : (a, b)
__wrapped__: True
wrapped is add2 original: <function add2 
```

### 它具体复制了什么

`functools.wraps(func)` 把 `func` 的这些属性复制到 `wrapper` 上：

- `__module__`
- `__name__`
- `__qualname__`
- `__doc__`
- `__dict__`
- `__wrapped__`（指向原函数）

`inspect.signature()` 会顺着 `__wrapped__` 找到原函数，所以签名能正确显示成 `(a, b)`。

### 为什么必须在乎

| 场景 | 不加 wraps 的后果 |
|---|---|
| 日志 / traceback | 所有被装饰函数都显示 `wrapper`，无法定位 |
| IDE 提示 / `help()` | 签名变 `(*args, **kwargs)`，文档为空 |
| Flask 路由、click 命令、pytest 收集 | 按 `__name__` 建立索引，函数名冲突会互相覆盖 |

### `functools` 的其他常用工具

| 工具 | 作用 |
|---|---|
| `lru_cache` / `cache` | 缓存函数结果 |
| `partial` | 固定部分参数，生成新函数 |
| `reduce` | 累积运算 |
| `singledispatch` | 按第一个参数类型分发实现 |
| `total_ordering` | 补全比较方法 |

---

## B. 为什么要包多层

### 一句话

每一层对应一个**必须提前固定**的值，而这些值到达的**时机不同**。

```python
@retry(times=3)
def f(): ...
```

等价于：

```python
f = retry(times=3)(f)
```

### 三次执行

| 时机 | 谁执行 | 拿到什么 | 返回什么 |
|---|---|---|---|
| 定义时第 1 次 | `retry(3)` | `times=3` | `inner` |
| 定义时第 2 次 | `inner(f)` | `f` 这个函数 | `wrapper` |
| 每次调用 | `wrapper(...)` | 运行参数 | 原函数的返回值 |

`times` 在 `@retry(times=3)` 那一行就要确定，此刻函数还不存在；函数要到下一阶段才提供。两件事不可能压在同一层解决。

### 实测：压成一层会怎样

```python
def retry_flat(times=3, func=None):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@retry_flat(times=3)
def hello():
    return "hi"
```

实测输出：

```text
TypeError: 'NoneType' object is not callable
```

原因：`retry_flat(times=3)` 立刻返回 `wrapper`，此时 `func` 还是 `None`；随后 Python 又把这个返回值拿去调用 `hello`，`func` 仍为空。

### 层数与需求的对应

| 需求 | 层数 | 每层固定什么 |
|---|---|---|
| `@deco` | 2 | `func` |
| `@deco(arg)` | 3 | `arg` → `func` |
| 装饰器类 | 用 `__call__` 替代外层 | 实例属性 |

### 底层机制是闭包

内层函数能用外层的 `times` 和 `func`，是因为闭包：外层局部变量被内层函数保留，即使外层已经返回。没有这层结构，`wrapper` 运行时拿不到 `func`。

**结论：层数不是风格问题，而是参数到达顺序的必然结果。够用就好。**

---

## C. 英语词（本节相关）

| 词 | 含义 | 例句 |
|---|---|---|
| metadata | 元数据 | `wraps` copies the original **metadata**. |
| signature | 函数签名 | `inspect.signature` shows `(a, b)` after `wraps`. |
| closure | 闭包 | A **closure** keeps the outer variables alive. |
| timing | 时机 | The two values arrive at different **timing**. |

---

## 原对话摘录 / Original conversation excerpt

> **2026-11-17**
> 学习者提问：
> **“那个 functools 那那个工具有什么用呢？然后我包这么多层又有什么用呢？”**

> 助教：
> `wraps` 保住名字、文档、签名；多层是因为参数和函数在不同时刻到达，压成一层会报 `'NoneType' object is not callable`。

---

*本篇所有 `text` 输出来自 `~/learning/.venv/bin/python` 实跑（脚本 `/tmp/wraps_check.py`）。*
