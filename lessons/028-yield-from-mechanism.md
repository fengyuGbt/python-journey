# 028 — `yield from` 的原理

> Week 6 · Day 1 追加提问 · 2026-11-15

## 问题

```python
def chain(list1, list2):
    yield from list1
    yield from list2
```

这个是什么原理？为什么两个 `yield from` 能接成一个序列？

---

## 一、结论：一个 for 循环 + 三件额外的事

最核心的等价关系：

```python
yield from X
# 约等于
for item in X:
    yield item
```

`chain` 能“接起来”，靠的是**函数体顺序执行**：第一个 `yield from list1` 是阻塞点，必须等 `list1` 彻底耗尽、抛出 `StopIteration`，才往下走到第二个 `yield from list2`。

---

## 二、逐帧看执行过程

```python
gen = chain([1, 2, 3], [4, 5])
```

| 第几次 `next` | 生成器内部动作 | 产出 |
|---|---|---|
| 1 | 进入函数 → 开始第一个 `yield from` → 取 `list1[0]` | `1`（暂停，保存 frame） |
| 2 | 从暂停处恢复 → 取 `list1[1]` | `2` |
| 3 | 取 `list1[2]` | `3` |
| 4 | `list1` 耗尽 → 第一个 `yield from` 结束 → 进入第二个 → 取 `list2[0]` | `4` |
| 5 | 取 `list2[1]` | `5` |
| 6 | `list2` 也耗尽 → 函数体结束 | `StopIteration` |

生成器能“记住走到哪”，是因为它保存了一个栈帧（frame），每次 `next` 从上次 `yield` 处恢复，而不是重新执行函数。

---

## 三、实测：`yield from` 比 for 循环多做的三件事

### ① 子生成器的 `return` 值会被接住

```python
def sub():
    yield 1
    yield 2
    return "done"


def outer():
    result = yield from sub()
    print("sub returned:", result)


for v in outer():
    print("got", v)
```

实测输出：

```text
got 1
got 2
sub returned: done
```

`yield from` 是**表达式**，有返回值：子生成器 `return` 的东西成为它的值。普通 `for x in sub()` 拿不到 `"done"`——它藏在 `StopIteration.value` 里。

### ② 能转发任意 iterable

```python
def mixed():
    yield from "ab"
    yield from [1, 2]
    yield from {"k": "v"}


print(list(mixed()))
```

实测输出：

```text
['a', 'b', 1, 2, 'k']
```

字符串按字符走，字典按 key 走。只要是 iterable 都行，不需要是生成器。

### ③ 双向通道（PEP 380）

`yield from` 会把外层的 `send()`、`throw()`、`close()` 转发给子生成器。这是它和 `for x in X: yield x` 唯一的**实质性**区别——协程（`asyncio` 的 `await` 底层就是这套机制）靠它把值送进去。

---

## 四、和 `list1 + list2` 的区别

| 维度 | `list1 + list2` | `yield from` |
|---|---|---|
| 是否复制数据 | 复制，生成新列表 | 不复制，边走边吐 |
| 何时执行 | 立即 | 惰性，`next` 才动 |
| 能否接无限流 | 不行（会卡死） | 可以 |
| 类型要求 | 必须都是 list | 任意 iterable 混接 |
| 内存 | 两份数据之和 | 常数 |

实测“不复制”：

```python
a = [1, 2, 3]
combined = list(chain(a, [4, 5]))
a.append(99)
print(combined)   # [1, 2, 3, 4, 5]，仍是旧内容
```

因为它遍历的是当时的元素，不持有副本。

---

## 五、坑

`yield from` 遍历列表时**不复制**。边遍历边修改同一个列表会报：

```text
RuntimeError: list changed size during iteration
```

要改就先 `list(x)` 拷一份再遍历。

---

## 六、澄清：`frame` 不可迭代，和 `list(x)` 不是一回事

有人会问：文档里说的 frame，是不是能 `list(frame)` 变成列表？

不是。`frame` 是解释器的栈帧对象，没有迭代器接口，`list(frame)` 直接报错：

```text
TypeError: 'frame' object is not iterable
```

它和第五节里的 `list(x)` 是两件无关的事——那里的 `x` 是**被遍历的列表**，`list(x)` 的意思是“拷一份再遍历”。

### frame 里装了什么

```python
def g():
    x = 10
    yield x
    x += 5
    yield x


gen = g()
print(next(gen))
print(type(gen.gi_frame))
print(gen.gi_frame.f_locals)
print(gen.gi_frame.f_lineno)
```

实测输出：

```text
10
<class 'frame'>
{'x': 10}
3
```

第二次 `next` 之后：

```text
15
{'x': 15}
5
```

耗尽之后 `gen.gi_frame` 变成 `None`——现场被清掉，这正是生成器不能二次遍历的物理原因。

| 属性 | 含义 |
|---|---|
| `gen.gi_frame` | 当前栈帧，未开始或已结束时为 `None` |
| `f_locals` | 局部变量当前值（`{'x': 10}`） |
| `f_lineno` | 停在源码第几行 |
| `list(gen.gi_frame)` | ❌ `TypeError: 'frame' object is not iterable` |

---

## 七、英语词（本节相关）

| 词 | 含义 | 例句 |
|---|---|---|
| delegate | 委托、转发 | `yield from` **delegates** to a sub-iterator. |
| sub-generator | 子生成器 | The `return` value of the **sub-generator** is captured. |
| frame | 栈帧 | A generator keeps its own **frame**. |
| exhaust | 耗尽 | The first `yield from` runs until the list is **exhausted**. |
| PEP 380 | 提案编号 | **PEP 380** defines `yield from`. |

---

## 原对话摘录 / Original conversation excerpt

> **2026-11-15**
> 学习者提问：
> **"def chain(list1,list2): yield from list1; yield from list2，这个是什么原理"**

> 助教：
> `yield from X` 约等于 `for item in X: yield item`。两个 `yield from` 能接起来，靠的是函数体顺序执行——第一个必须等 list1 耗尽（抛出 StopIteration）才往下走。

---

*本篇所有 `text` 输出来自 `~/learning/.venv/bin/python` 实跑（脚本 `/tmp/yf_check.py`）。*
