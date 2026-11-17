# 029 — `chain` 的两个迭代器怎么“合并”成一个列表

> Week 6 · Day 1 追加提问 · 2026-11-15

## 问题

```python
def chain(list1, list2):
    yield from list1
    yield from list2

gen = chain([1, 2, 3], [4, 5])
print(list(gen))          # [1, 2, 3, 4, 5]
```

`chain` 里有两个迭代器，它们最后是怎么合并成一个列表的？

---

## 一、结论：`chain` 不合并，`list()` 才合并

`chain(...)` 返回的**不是列表**，是一个生成器对象。它内部并没有“两个迭代器并存”，而是**同一时刻只有一个在活动**：`list1` 用完再换 `list2`。

真正的“合并”发生在 `list(gen)` 这一步：`list()` 不停地向生成器要值，要到一个就往列表里塞一个，直到生成器报 `StopIteration`。

```text
chain: 负责按顺序产出（生产者，不存数据）
list(): 负责收集（消费者，把值堆起来）
```

打比方：`chain` 是水管，`list()` 是水桶。水管里不存水，水只在桶里才有形状。

---

## 二、三步拆开看

**第 1 步：调用函数，什么都不执行**

```python
gen = chain([1, 2, 3], [4, 5])
```

函数体里有 `yield`，所以这是个生成器函数。调用它只创建一个生成器对象，函数体**一行都没跑**。

**第 2 步：每次 `next` 产出一个值**

```text
next #1 → 取 list1[0] → 1
next #2 → 取 list1[1] → 2
next #3 → 取 list1[2] → 3
next #4 → list1 耗尽 → 切到 list2 → 4
next #5 → 取 list2[1] → 5
next #6 → 两个都空了 → StopIteration
```

**第 3 步：`list()` 收集**

`list(gen)` 的等价手写版就是：

```python
out = []
while True:
    try:
        out.append(next(gen))
    except StopIteration:
        break
print(out)
```

实测输出 `[1, 2, 3, 4, 5]`，和 `list(gen)` 一模一样。

---

## 三、实测证据

### ① 返回值类型

```text
type: <class 'generator'>
is list? False
```

### ② 同一时刻只有一个子迭代器在活动

`yield from list1` 在源码第 2 行，`yield from list2` 在第 3 行。看每取一个值时生成器停在哪一行：

```text
next #1: value=1, 停在源码第 2 行
next #2: value=2, 停在源码第 2 行
next #3: value=3, 停在源码第 2 行
next #4: value=4, 停在源码第 3 行     ← 这里才切换
next #5: value=5, 停在源码第 3 行
```

第 4 次才跳到第 3 行，说明 `list1` 是**彻底用完**之后才启动 `list2` 的。不存在“两个迭代器同时遍历、交错合并”。

---

## 四、一个后果：传进去的生成器会被吃掉

```python
inner = (x for x in [1, 2, 3])
print(list(chain(inner, [4, 5])))   # [1, 2, 3, 4, 5]
print(list(chain(inner, [4, 5])))   # [4, 5]
```

第二遍只剩 `[4, 5]`——`inner` 是个生成器，第一遍已经走到底了。而列表 `[1, 2, 3]` 可以反复遍历，因为列表每次 `iter()` 都会新建一个迭代器。

这就是“可迭代对象”和“迭代器”的分界线：

| | 列表（iterable） | 生成器（iterator） |
|---|---|---|
| `iter()` 每次 | 新建一个从头开始的迭代器 | 返回自己，位置不变 |
| 能遍历几遍 | 无限遍 | 一遍 |

---

## 五、英语词（本节相关）

| 词 | 含义 | 例句 |
|---|---|---|
| producer | 生产者 | The generator is a **producer**. |
| consumer | 消费者 | `list()` is a **consumer**. |
| collect | 收集 | `list()` **collects** values until `StopIteration`. |
| hand over | 交接 | Control is **handed over** to the second `yield from`. |

---

## 原对话摘录 / Original conversation excerpt

> **2026-11-15**
> 学习者提问：
> **“它不是有两个迭代器吗？那最后这两个迭代器是怎么合并成一个列表的？”**

> 助教：
> `chain` 返回的是一个生成器，不是列表。合并发生在 `list(gen)`——它不停地 `next` 并 `append`，直到 `StopIteration`。`chain` 只负责顺序，不负责合并。

---

*本篇所有 `text` 输出来自 `~/learning/.venv/bin/python` 实跑（脚本 `/tmp/merge_check.py`）。*
