# 031 — `*args` 与 `**kwargs` 的区别

> Week 6 · Day 2 追加提问 · 2026-11-16

## 问题

装饰器里的 `def wrapper(*args, **kwargs):`，`args` 前的 `*` 和 `kwargs` 前的 `**` 有什么区别？

---

## 一、结论对照表

| | `*args` | `**kwargs` |
|---|---|---|
| 收什么 | 多余的**位置参数** | 多余的**关键字参数** |
| 收成什么 | `tuple` | `dict` |
| 定义时 | 收集 | 收集 |
| 调用时 | 拆开 list/tuple | 拆开 dict |

一句话：**同一个符号，定义时是“收集”，调用时是“拆开”**。名字 `args`/`kwargs` 只是社区约定，写成 `*a`、`**b` 效果完全一样。

---

## 二、定义时：收集

```python
def show(*args, **kwargs):
    print("args   =", args, "| type =", type(args).__name__)
    print("kwargs =", kwargs, "| type =", type(kwargs).__name__)
```

实测：

```text
--- show(1, 2, 3) ---
args   = (1, 2, 3) | type = tuple
kwargs = {} | type = dict

--- show(x=1, y=2) ---
args   = () | type = tuple
kwargs = {'x': 1, 'y': 2} | type = dict

--- show(1, 2, x=3, y=4) ---
args   = (1, 2) | type = tuple
kwargs = {'x': 3, 'y': 4} | type = dict
```

位置参数按顺序收进 `args`，关键字参数按名字收进 `kwargs`，两边互不影响。

---

## 三、调用时：拆开

```python
def add(a, b):
    return a + b


print(add(*[3, 4]))                  # 7
print(add(**{"a": 3, "b": 4}))       # 7
```

实测：

```text
add(*[3, 4])   = 7
add(**{"a": 3, "b": 4}) = 7
```

典型用途：参数放在容器里、要打散传出去，或者需要转发另一个函数的入参。

---

## 四、单独的 `*`：强制关键字传参

```python
def kwonly(a, *, b):
    return a, b
```

实测：

```text
kwonly(1, b=2) = (1, 2)
TypeError: kwonly() takes 1 positional argument but 2 were given
```

`*` 后面不跟名字时，它就是一个分隔符：后面的参数只能按名字传。

完整的 Python 3 签名分隔符：

```python
def f(a, /, b, *, c):
    ...
```

| 符号 | 含义 |
|---|---|
| `/` 之前 | 仅位置参数（不能用 `a=1` 传） |
| `/` 与 `*` 之间 | 普通参数，两种传法都行 |
| `*` 之后 | 仅关键字参数（不能按位置传） |

---

## 五、参数顺序不能乱

合法顺序：

```python
def f(a, b=2, *args, c=3, **kwargs):
    ...
```

普通参数 → 默认值参数 → `*args` → 关键字-only 参数 → `**kwargs`。

---

## 六、一个高频错误

```python
def full(a, b=2, *args, **kwargs):
    return a, b, args, kwargs


full(1, 2, 3, a=9)
```

实测：

```text
full(1) = (1, 2, (), {})
full(1, 3, 5, 6, x=7) = (1, 3, (5, 6), {'x': 7})
TypeError: full() got multiple values for argument 'a'
```

`a` 已经按位置收到 `1`，关键字又给 `a=9`，同一个参数收了两次值，直接报错。

---

## 七、为什么装饰器里永远写 `(*args, **kwargs)`

装饰器不知道被装饰函数的签名。写成 `wrapper(*args, **kwargs)` 才能做到**透明转发**：

```python
def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
```

不管原函数是 `f()`、`f(x)` 还是 `f(a, b=1, *rest)`，都能原样透过去。如果只写 `def wrapper():`，装饰任何带参数的函数都会在调用时报错。

---

## 八、英语词（本节相关）

| 词 | 含义 | 例句 |
|---|---|---|
| positional argument | 位置参数 | `*args` collects extra **positional arguments**. |
| keyword argument | 关键字参数 | `**kwargs` collects extra **keyword arguments**. |
| unpack | 拆包 | `*` **unpacks** a list at the call site. |
| keyword-only | 仅关键字 | A bare `*` makes the following parameters **keyword-only**. |

---

## 原对话摘录 / Original conversation excerpt

> **2026-11-16**
> 学习者提问：
> **“参数 args，* 和 ** 有啥区别”**

> 助教：
> 单个 `*` 收位置参数成 tuple，双 `**` 收关键字参数成 dict；调用时反过来是拆包。

---

*本篇所有 `text` 输出来自 `~/learning/.venv/bin/python` 实跑（脚本 `/tmp/args_check.py`）。*
