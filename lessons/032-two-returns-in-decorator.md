# 032 — 装饰器里两个 `return` 分别起什么作用

> Week 6 · Day 2 追加提问 · 2026-11-16

## 问题

```python
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f}s")
        return result        # ①
    return wrapper           # ②
```

这里有 2 个 `return`，分别起什么作用？

---

## 一、结论：两层函数，两个职责

| 编号 | 位置 | 管什么 | 什么时候执行 |
|---|---|---|---|
| ① `return result` | `wrapper` 内部 | **数据**：把原函数的返回值交回调用方 | 每次调用 `slow()` |
| ② `return wrapper` | `timer` 内部 | **函数**：把包装后的新函数交回给名字 `slow` | 定义时，只一次 |

外层负责“换人”：`slow` 这个名字改指向 `wrapper`。
里层负责“传话”：原 `slow` 算出的结果原样传回去。

---

## 二、时序

```python
@timer
def slow():
    time.sleep(0.5)
```

等价于：

```python
def slow():
    time.sleep(0.5)
slow = timer(slow)      # ← 此刻执行一次 timer()，得到 wrapper，赋给 slow
```

| 时刻 | 执行栈 | 走到的 return | 结果 |
|---|---|---|---|
| 定义时 | `timer(slow)` | ② `return wrapper` | `slow = wrapper` |
| 第 1 次 `slow()` | `wrapper()` | ① `return result` | 返回值交给调用方 |
| 第 2 次 `slow()` | `wrapper()` | ① `return result` | 同上 |

`timer` 本身只运行一次；`wrapper` 每次调用都运行。

---

## 三、实测：缺任何一个会怎样

### 缺里层 `return result`

```python
def timer_no_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("  (装饰器干了点活)")
        # 忘了 return result
    return wrapper


@timer_no_result
def add(a, b):
    return a + b


print(add(1, 2))
```

实测输出：

```text
  (装饰器干了点活)
add(1, 2) 返回： None
```

函数照常执行、副作用照做，但返回值变成 `None`。这是装饰器最常见的隐蔽 bug——调用方拿到 `None`，却不知道问题出在装饰器。

### 正确写法

```text
  (装饰器干了点活)
add2(1, 2) 返回： 3
```

### 缺外层 `return wrapper`

```python
def timer_no_wrapper(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    # 忘了 return wrapper


@timer_no_wrapper
def hello():
    return "hi"
```

实测输出：

```text
装饰后的 hello 是什么： None
TypeError: 'NoneType' object is not callable
```

`@timer_no_wrapper` 把 `hello` 赋成了 `None`，函数直接消失。报错发生在调用时刻，离出错位置很远，所以很难查。

---

## 四、顺带：`wraps` 复制的是名字，不是对象

实测：

```python
print(timer_ok)          # <function timer_ok 
print(timer_ok(add2))    # <function add2 
```

`timer_ok(add2)` 显示成 `add2`，但它实际是 `wrapper` 对象。`functools.wraps` 只复制 `__name__`、`__qualname__`、`__doc__`、`__module__`、`__dict__` 这些属性，并没有替换对象本身。

这也解释了为什么加 `wraps` 后日志里看到的是原函数名——名字被改了，函数还是新的那个。

---

## 五、记忆法

- 里层 `return`：管**数据**，别吞掉返回值。
- 外层 `return`：管**函数**，别弄丢函数本身。

---

## 六、英语词（本节相关）

| 词 | 含义 | 例句 |
|---|---|---|
| delegate | 委托 | `timer` **delegates** the actual call to `func`. |
| wrapper | 包装函数 | `wrapper` runs on every call. |
| propagate | 传递、原样返回 | `return result` **propagates** the original value. |
| drop the return value | 丢掉返回值 | Forgetting `return` **drops the return value**. |

---

## 原对话摘录 / Original conversation excerpt

> **2026-11-16**
> 学习者提问：
> **“有 2 个 return，分别起什么作用”**

> 助教：
> 里层 `return result` 把原函数的结果交回去（少了就变 None）；外层 `return wrapper` 把新函数交给 `slow`（少了就 TypeError: 'NoneType' object is not callable）。

---

*本篇所有 `text` 输出来自 `~/learning/.venv/bin/python` 实跑（脚本 `/tmp/two_return_check.py`）。*
