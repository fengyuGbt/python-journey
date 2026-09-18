# QA · `sorted(字典.items())` 为什么返回列表？遍历时为什么不用 `.items()`？/ Why does `sorted(dict.items())` return a list?

## 中文

**问题**：练习③里 `sorted(students.items(), ...)` 排完是什么类型？为什么 `for name, score in ranked` 遍历时不需要像 `students.items()` 那样加 `.items()`？

**回答**：

1. **`sorted()` 永远返回一个新列表**——不管输入是字典、集合、元组还是字符串，`sorted()` 一律吐出一个**新列表**。所以 `sorted(students.items())` 的结果是 `[('Alice', 85), ('Bob', 58), ...]`——一个**元组列表**。
2. **`.items()` 是"字典 → 键值对序列"的开关**：调用它产生一个 `dict_items` 视图，可迭代、逐个产出 `(key, value)` 元组，但它**不是列表**。
3. **遍历 `ranked` 不需要 `.items()`，因为已经不在遍历字典了**——`ranked` 是普通列表，`for name, score in ranked` 直接对每个元组解包。只有当你直接遍历**字典本体** `for x in students` 时，Python 只产出键（字符串），拿不到值，那时才需要 `.items()`。

**口诀**：看到"字典本体"才需要 `.items()`；`sorted()` / `zip()` 之后的产物都是普通容器，直接遍历即可。

**类型验证**：

```python
students = dict(zip(["Alice", "Bob", "Carol"], [85, 58, 73]))
print(type(students))              # <class 'dict'>
print(type(students.items()))      # <class 'dict_items'>
print(type(sorted(students.items())))  # <class 'list'>
print(sorted(students.items())[0])     # ('Alice', 85)
```

`dict_items` 是一个**视图**——像列表一样能迭代，但不是列表。`sorted()` 把任何可迭代对象"拍扁"成一个新的普通列表，之后的一切都是列表操作。

---

## English

**Question**: in exercise ③, what type does `sorted(students.items(), ...)` return? Why does `for name, score in ranked` not need `.items()`?

**Answer**:

1. **`sorted()` always returns a new list** — no matter the input (dict, set, tuple, string), it produces a fresh list. So `sorted(students.items())` is `[('Alice', 85), ('Bob', 58), ...]` — a **list of tuples**.
2. **`.items()` is the "dict → key-value pairs" switch**: it yields a `dict_items` view — iterable, producing `(key, value)` tuples one by one — but it is **not a list**.
3. **`ranked` needs no `.items()` because you are no longer iterating a dict** — `ranked` is a plain list; `for name, score in ranked` unpacks each tuple directly. Only when iterating the **dict itself** (`for x in students`) does Python yield just the keys (strings); that is when `.items()` is needed.

**Mnemonic**: need `.items()` only when you see the dict itself; after `sorted()` / `zip()`, the result is a normal container — iterate directly.

`dict_items` is a **view** — iterable like a list, but not a list. `sorted()` flattens any iterable into a new plain list; everything after that is plain list operations.

---

## 原对话摘录 / Original conversation excerpt

> 摘自学习者与 AI 助教的真实对话（2026-09-18）。

**学习者提问**：

> "sorted 那个把字典排序完以后，它就变成了一个列，列表吗？还是为什么它在那个遍历的时候不需要加 items？"

**助教回答要点**：

> "对，`sorted()` 排完永远返回一个'新列表'——不管输入是字典、集合还是字符串……遍历时不需要 `.items()`，是因为你已经不在遍历字典了——你遍历的是 `ranked`（列表），直接对每个元组解包。`.items()` 是字典的专属开关：只有当你直接遍历字典本体时，Python 只产出键，拿不到值，这时才需要 `.items()`。"
