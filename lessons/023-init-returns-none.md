# 023 — 类初始化（`__init__`）为什么返回 `None`，对象到底由谁返回？

> Week 5 · OOP · 2026-11-15
> 类型：概念澄清（不是 bug 复盘）

---

## 原始疑问

> 「类初始化返回类型为啥是 None，不是应该是对象吗？」

出处：给 library_cli 的全部方法补 typing 注解时，看到 `def __init__(self, ...) -> None:` 产生疑问。

---

## 结论（先给答案）

`__init__` 的职责是**初始化一个已经存在的对象**（把属性装进去）。它本身不创建对象，也不返回对象——Python 强制它返回 `None`，返回别的东西会直接 TypeError。

你拿到的对象，是 **`Book(...)` 这个"类调用"动作**返回的；真正"造对象"的动作发生在 `__new__` 里。

---

## 三层执行链

```python
b = Book("Python", "Guido")
```

这一行内部实际是三步：

```
1. Book.__new__(Book)                    → 造出一个空壳对象（真正的"创建"在这）
2. Book.__init__(b, "Python", "Guido")   → 往空壳里装属性（"装修"）
3. 返回 b                                → 返回的是第 1 步造的对象，不是第 2 步的结果
```

`__init__` 是装修工：进去的时候对象已经存在了（`self` 就是那个对象），它不需要也不允许返回任何东西。

---

## 证据：`__init__` 返回非 None 直接报错

```python
class A:
    def __init__(self):
        return "x"

A()
# TypeError: __init__() should return None, not 'str'
```

说明 `-> None` 是**如实描述返回值**，不是简化写法。

---

## `__new__` vs `__init__`

| 方法 | 职责 | 返回值 | 谁负责造对象 |
|---|---|---|---|
| `__new__` | 创建实例 | 实例 | ✅ |
| `__init__` | 初始化实例（装属性） | `None`（强制） | ❌ |

`__new__` 的返回值才是 `B()` 的结果；`__init__` 的返回值被 Python 直接丢弃。

---

## 类比

| 角色 | 干的事 | 返回什么 |
|---|---|---|
| `__new__` | 造房子 | 房子（实例） |
| `__init__` | 装修房子 | 无（`None`） |
| `Book(...)`（类调用） | 叫工人造 + 装修 | 装好的房子 |

---

## 自测（30 秒）

```python
class A:
    def __init__(self):
        return "x"

A()   # 观察 TypeError
```

看到 `__init__() should return None, not 'str'`，机制就记住了。

---

## 项目里的落地

library_cli 中 `Book("x", "y")` 返回的 `b` 是对象；`__init__` 只是把 `title` / `author` / `is_borrowed` 装进 `b`。给 `__init__` 加 `-> None` 注解不改变任何运行时行为，只是把"它返回 `None`"这个事实写进类型契约。

---

## 英语 3 词

| 词 | 例句 |
|---|---|
| instantiate | `Book("Python", "Guido")` **instantiates** the `Book` class. |
| initialize | `__init__` **initializes** the object's attributes. |
| constructor | In Python, `__init__` is called the **constructor**, but `__new__` does the real creation. |

---

## 原对话摘录

**问**：类初始化返回类型为啥是 None，不是应该是对象吗？

**答**：对象确实是返回的，但不是 `__init__` 返回的——它返回的是 `None`，对象是"类调用"这个动作返回的。执行顺序是 `__new__` 造空壳 → `__init__` 装属性 → 返回 `b`（第 1 步造的对象）。Python 强制 `__init__` 返回 `None`，返回别的直接 TypeError。

---

## Original conversation excerpt (English)

**Q**: Why does `__init__` return `None` instead of the object?

**A**: Because `__init__` does not create the object — `__new__` does. `__init__` only initializes an existing instance and must return `None`; otherwise Python raises `TypeError`. The object returned by `Book(...)` is the instance created in `__new__`, not the return value of `__init__`.
