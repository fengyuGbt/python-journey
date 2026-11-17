# 030 — 子迭代器的 `StopIteration` 为什么不会让外层 `break`

> Week 6 · Day 1 追加提问 · 2026-11-15

## 问题

```python
out = []
while True:
    try:
        out.append(next(gen))
    except StopIteration:
        break
```

`gen = chain([1, 2, 3], [4, 5])` 内部有两个子迭代器。第一个 `list1` 用完时会抛 `StopIteration`，为什么外层没有在那一刻 `break`？

---

## 一、结论：`StopIteration` 在生成器边界被“翻译”了

`yield from` 的内部语义等价于：

```python
try:
    for item in list1:
        yield item
except StopIteration:
    pass          # 吃掉，继续往下执行
```

`list1` 耗尽抛出的 `StopIteration` 是**内部事件**，被 `yield from` 当场接住，转换成“这一段委托结束”，然后继续执行 `yield from list2`。外层调用者看不到这次异常。

外层第一次收到 `StopIteration`，是整个 `chain` 函数体执行完（`return`）的那一刻。

---

## 二、实测：逐次 `next`

```python
def chain(a, b):
    yield from a
    yield from b


gen = chain([1, 2, 3], [4, 5])
for i in range(1, 8):
    try:
        print(f"next #{i}: {next(gen)}")
    except StopIteration:
        print(f"next #{i}: StopIteration ← 外层第一次见到")
        break
```

```text
next #1: 1
next #2: 2
next #3: 3
next #4: 4        ← list1 在这里耗尽，没有任何异常冒出来
next #5: 5
next #6: StopIteration ← 外层第一次见到
```

第 4 次正常返回 4，证明 `list1` 的结束信号被内部消化了。

---

## 三、反证：不捕获会怎样（PEP 479）

```python
def bad(a, b):
    it = iter(a)
    while True:
        yield next(it)


list(bad([1, 2, 3], [4, 5]))
```

实测：

```text
RuntimeError: generator raised StopIteration
```

Python 3.7+ 不允许 `StopIteration` 从生成器里逃出去。原因：如果它逃出来，调用方会误判为“这个生成器正常结束”，而实际只是内部某个子迭代器用完了。PEP 479 强制转成 `RuntimeError`，逼你在内部处理。

手动捕获就能接上：

```python
def fixed(a, b):
    it = iter(a)
    while True:
        try:
            yield next(it)
        except StopIteration:
            break          # 只跳出一层 while
    for x in b:
        yield x


print(list(fixed([1, 2, 3], [4, 5])))
```

实测输出：

```text
[1, 2, 3, 4, 5]
```

---

## 四、三层边界对照表

| 谁抛的 `StopIteration` | 谁来接 | 结果 |
|---|---|---|
| 子迭代器 `list1` 用完 | `yield from` / `for` 内部 | 吞掉，继续往下 |
| 生成器函数 `return` | 调用方的 `for` / `next()` | 对外结束信号 |
| 函数内部裸 `next()` 没接住 | 没人接 | PEP 479 → `RuntimeError` |

`for` 循环同理：`for x in it` 内部捕获 `StopIteration` 然后结束循环，使用者永远看不到这个异常。

---

## 五、和 028 的呼应

`yield from` 捕获子迭代器的 `StopIteration` 时，会读取它的 `value` 属性，作为 `yield from` 表达式的返回值。所以子生成器 `return "done"`，外层能拿到 `"done"`——见 028 第三节。

---

## 六、英语词（本节相关）

| 词 | 含义 | 例句 |
|---|---|---|
| translate | 转换、翻译 | `StopIteration` is **translated** at the generator boundary. |
| escape | 逃逸 | A leaked `StopIteration` **escapes** the generator. |
| boundary | 边界 | The generator **boundary** is where the exception is caught. |
| swallow | 吞掉（异常） | `yield from` **swallows** the inner `StopIteration`. |

---

## 原对话摘录 / Original conversation excerpt

> **2026-11-15**
> 学习者提问：
> **“out = [] … except StopIteration: break，gen 有两个 stopIteration，为啥不是第一个 list 出现 stopIteration 就 break？”**

> 助教：
> `list1` 的 `StopIteration` 在 `yield from` 内部就被吞了，外层看到的 “结束” 只有整个函数 body 走完那一次。裸 `next()` 不捕获的话，Python 会直接报 `RuntimeError: generator raised StopIteration`。

---

*本篇所有 `text` 输出来自 `~/learning/.venv/bin/python` 实跑（脚本 `/tmp/si_check.py`）。*
