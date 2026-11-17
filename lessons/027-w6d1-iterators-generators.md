# 027 — 第 6 周 Day 1：迭代器与生成器

> Week 6 · Day 1 · 2026-11-15
> 三道练习全部通过。其中两题首版有坑（`even_numbers` 不出数、`read_lines` 统计只数一半、`groupby` 嵌套遍历），修正后实测通过。

---

## 一、概念地图

| 概念 | 定义 | 关键特征 |
|---|---|---|
| 可迭代对象 iterable | 能用 `for` 遍历的东西 | 有 `__iter__`；列表、字典、文件、字符串都是 |
| 迭代器 iterator | 能一个个吐值、吐完就到底的东西 | 有 `__iter__` + `__next__`，**有状态**，只能走一次 |
| 生成器 generator | 用 `yield` 写出来的迭代器 | 调用函数**不执行**，`next()` 才执行到下一个 `yield` |
| 生成器表达式 | `(x for x in seq)` | 惰性求值、不占内存、同样只能走一次 |

`for` 的底层三步：

```text
it = iter(obj)        # 拿到迭代器
while True:
    try:
        x = next(it)  # 一个个取
    except StopIteration:
        break         # 取完了就退出
```

---

## 二、练习 1：无限偶数生成器

**首版（错）**

```python
def even_numbers(x=0):
    while True:
        yield x + 2
```

输出：`2 2 2 2`。

**病根**：`x` 从来没变过。`yield x + 2` 每次都用同一个初始值算，算完就丢，`x` 本身没被修改。生成器保存的是“执行到哪一行”，不保存“变量应该变成几”。

**修正版**

```python
def even_numbers(x=0):
    while True:
        yield x        # 先吐当前值
        x += 2         # 推进
```

**实测输出**

```text
0 2 4 6 8 10 12 14 16 18
```

要点：`yield` 放在 `x += 2` 前面，第一次吐 0；放后面，第一次吐 2。

---

## 三、练习 2：逐行读大文件

**首版（统计错）**

```python
def read_lines(path):
    with open(path, "r") as f:
        for line in f:
            yield line

count = 0
gen1 = read_lines("big.txt")
for line in gen1:
    next(gen1)      # ← 每次多消耗一行
    count += 1
print(count)        # 100000 行的文件会打成 50000
```

**病根**：`for` 每次迭代自己就调一次 `next()`，循环体里再调一次，等于每轮吃掉两行、只记一次数。

**修正版**

```python
def read_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        yield from f

print(repr(next(read_lines("/home/acer/learning/big.txt")))
print(sum(1 for _ in read_lines("/home/acer/learning/big.txt")))
```

**实测输出**

```text
first line: '1\n'
line count: 100000
```

`wc -l big.txt` 也是 100000，对上了。

两个知识点：

- `yield from f` 等价于 `for line in f: yield line`，少一层缩进。
- 用 `len(f.readlines())` 结果一样，但 10 万行会一次性全塞进内存。生成器逐行吐，内存占用与文件大小无关。

---

## 四、练习 3：`chain` 与 `groupby`

### A. `chain`（自己实现，没用 itertools）

```python
def chain(list1, list2):
    yield from list1
    yield from list2

print(list(chain([1, 2, 3], [3, 4, 5, 6])))   # [1, 2, 3, 3, 4, 5, 6]
```

自己写比直接调 `itertools.chain` 更值：两个 `yield from` 接起来，就是“先吐完第一个、再吐第二个”。

### B. `groupby`：首版错在嵌套遍历

**首版（错）**

```python
def group_by(words: list):
    yield from sorted(words, key=lambda x: x[0])

gen = group_by(["hello", "world", "apple", "www"])
for i in gen:
    for j in gen:                                  # ← 内层把生成器吃到空
        if i[:1].isupper() == j[0:1].isupper():    # ← 比的是"是否大写"
            print(i, j)
```

三个错叠在一起：

1. `yield from sorted(...)` 只是把词排序后一个个吐出来，没有分组。
2. `for i in gen` 里再 `for j in gen`：内层耗尽生成器，外层拿到第 2 个元素时已经是空的，循环提前结束。
3. `isupper()` 比较的是“大小写状态”，不是“首字母相同”；词全是小写，条件恒真。

**正确版**

```python
from itertools import groupby

words = ["apple", "avocado", "banana", "blueberry", "cherry", "apricot"]

for k, v in groupby(words, key=lambda x: x[0]):
    print(k, list(v))

for k, v in groupby(sorted(words, key=lambda x: x[0]), key=lambda x: x[0]):
    print(k, list(v))
```

**实测输出**

```text
--- 不排序 ---
a ['apple', 'avocado']
b ['banana', 'blueberry']
c ['cherry']
a ['apricot']
--- 排序后 ---
a ['apple', 'avocado', 'apricot']
b ['banana', 'blueberry']
c ['cherry']
```

两个必须记住的点：

- **`groupby` 只切“连续相同”的段**。不排序时 `apricot` 被 b、c 隔开，就自成第二组 `a`。
- **`v` 是迭代器，必须当场 `list(v)`**。只写 `print(k)` 的话，下一轮循环时这一组已经被释放，回头再取是空的。

---

## 五、为什么 `groupby` 必须先排序

学习者的原话：

> 因为迭代器只有局部视角，只能比较最近的两个。

方向对。精确说法是：

`groupby` 是**流式**的，一次只往前走一格，拿「当前元素的 key」和「当前这一组的 key」比——相等就留在组里，不等就立刻关掉当前组、开新组。它不建字典、不回头、不缓存历史。所以同一个 key 的元素一旦被别的 key 隔断，就只能另起一组。

这也是它省内存的原因：数据多大都不需要全装进来，只要有序，同类自然挨在一起。**省内存的代价就是要先排序。**

---

## 六、今天踩到的 4 个坑

| # | 坑 | 表现 | 修法 |
|---|---|---|---|
| 1 | 生成器变量不自增 | `yield x + 2` 输出 `2 2 2 2` | `yield x` 后再 `x += 2` |
| 2 | `for` 里再调 `next` | 10 万行文件数出 5 万 | 循环体里不要再 `next` |
| 3 | 同一个生成器嵌套遍历 | 外层只跑一轮就结束 | 要遍历两遍就重新调用函数 |
| 4 | `groupby` 前没排序 | 同一个 key 分成好几组 | 先 `sorted`，并当场 `list()` 消费每组 |

第 1、3、4 条其实是同一件事的三张脸：**迭代器是“一次性、有状态、只能往前”的**。

---

## 七、一个细节：`key=lambda x: x[0]` 与 `sorted(words)` 不等价

之前说“两者结果一样”，实际跑出来不一样，这里更正：

```python
words = ["apple", "avocado", "banana", "blueberry", "cherry", "apricot"]

sorted(words)                          # ['apple', 'apricot', 'avocado', ...]
sorted(words, key=lambda x: x[0])      # ['apple', 'avocado', 'apricot', ...]
```

- `sorted(words)` 比**整串**：`apple` vs `apricot` 第三字母 `p < r`，所以 apricot 在前。
- `sorted(words, key=lambda x: x[0])` 只比**首字母**：三个 a 开头视为相等，而 Python 排序是**稳定**的，相等元素保持原始相对顺序 → `apple, avocado, apricot` 不变。

对 `groupby` 来说两种都能正确分组（只关心首字母连续）；但要知道它们排出来的顺序不同。

---

## 八、英语词（Day 1 相关）

| 词 | 含义 | 例句 |
|---|---|---|
| iterable | 可迭代对象 | A list is **iterable**. |
| iterator | 迭代器 | An **iterator** keeps its own position. |
| generator | 生成器 | A function with `yield` returns a **generator**. |
| lazy evaluation | 惰性求值 | Generators use **lazy evaluation**. |
| exhaust | 耗尽 | A generator is **exhausted** after one loop. |
| yield from | 从子迭代器逐个产出 | `yield from` delegates to another iterable. |
| groupby | 分组 | `groupby` only groups **consecutive** keys. |

---

## 原对话摘录 / Original conversation excerpt

> **2026-11-15**
> 学习者首版：
> ```python
> def even_numbers(x=0):
>     while True:
>         yield x + 2
> ```
> 助教：`输出会是 2 2 2 2 —— x 从来没有变过，生成器只记住"执行到哪一行"，不会替你维护变量。`

> 学习者第二版：
> ```python
> for line in gen1:
>     next(gen1)
>     count += 1
> ```
> 助教：`for 每次迭代自己就调一次 next，你在循环体里再调一次，等于每轮吃掉两行、只记一次数。10 万行会打成 50000。`

> 学习者第三版 `groupby`：
> ```python
> for i in gen:
>     for j in gen:
>         if i[:1].isupper() == j[0:1].isupper():
> ```
> 助教：`同一生成器嵌套遍历，内层会把它吃到空；isupper() 比的是大小写状态，不是首字母。`

> 学习者对"为什么必须排序"的回答：
> **"因为迭代器只有局部视角，只能比较最近的两个。"**

---

*本篇所有 `text` 输出来自 `~/learning/.venv/bin/python` 实跑（脚本 `/tmp/w6d1_check.py`），对应文件 `~/learning/w6d1_iter_gen.py`。*
