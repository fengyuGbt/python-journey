# 036 — 什么时候调用需要 `try` 接住

> Week 6 · Day 2 · 2026-11-17

## 问题

学习者提问：

> 为啥 `slow()` 接住了，另外两个没接住？

前提本身需要纠正：**`slow()` 不是被“接住”，它根本不抛异常**。`@timer` 里没有任何 `try`。

---

## 一、实测：`@timer` 不吞异常

```python
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.3f}s")
        return result
    return wrapper


@timer
def ok():
    time.sleep(0.1)
    return "done"


@timer
def bad():
    raise RuntimeError("boom in timer")
```

```text
--- 正常函数 ---
ok took 0.100s
result: done

--- 会抛异常的函数，也用 @timer 装饰 ---
outer caught: RuntimeError boom in timer
```

`bad()` 抛异常时，计时那行**没有打印**，异常直接穿过 `wrapper` 冒到外面。`timer` 从未接住任何东西。

---

## 二、三个函数的真实差别

| 函数 | 装饰器 | 会不会向外抛异常 | 调用处要 `try` 吗 |
|---|---|---|---|
| `slow()` | `@timer` | **不会**（正常跑完） | 不用 |
| `flaky()` | `@retry` | **不会**（第 3 次成功，异常的中间失败被内部吞掉） | 不用，但要用 `print` 看结果 |
| `always_fail()` | `@retry` | **会**（3 次全失败，按设计抛出） | **必须** |

---

## 三、判定规则

> **看这次调用最终会不会向外抛异常，不是看它有没有被装饰。**

- `slow`：没有异常路径 → 无事发生。
- `flaky`：抛过异常，但被 `wrapper` 里的 `except` 消化 → 外部看不到。
- `always_fail`：抛了三次，最后一次 `raise` 出 `wrapper` → 必须有人接。

装饰器只是“包装”，它是否吞掉异常，取决于装饰器**自己的设计**：

| 装饰器 | 对异常的处理 |
|---|---|
| `@timer` | 不捕获，异常原样穿过（但会打断计时输出） |
| `@retry` | 捕获前 N-1 次并继续，最后一次 `raise` 交还 |
| `@logged`（待做） | 通常不捕获，只记录 |

---

## 四、为什么 `@retry` 必须保留抛出

如果最后一次不抛，函数会隐式返回 `None`（实测见 035 第五节），调用方会误以为调用成功。

重试的语义是“尽力而为，但最终失败要让调用方知道”，所以它**必然**有向外抛的路径。

---

## 五、`@timer` 的缺陷与修复

异常发生时，`end = time.perf_counter()` 和打印都没执行，无法得知耗时。

学习者自己尝试了一版 `except + raise`：

```python
def wrapper(*args, **kwargs):
    start = time.perf_counter()
    try:
        result = func(*args, **kwargs)
    except Exception as e:
        print("failed")
        raise
    end = time.perf_counter()
    print(f"{func.__name__} took {end - start:.3f}s")
    return result
```

实测异常路径：

```text
--- except + raise 版 ---
failed
outer caught: boom
```

**仍然没有耗时**。因为 `raise` 在 `except` 里会立即跳出 `wrapper`，后面的 `end = ...` 和 `print(耗时)` 都被跳过。

### 四种写法的对比

| 写法 | 正常结束 | 异常时 |
|---|---|---|
| 不加 `try` | 打印耗时 | 无任何耗时输出 |
| `except` + `raise` | 打印耗时 | 只打 `failed`，无耗时 |
| 只有 `finally` | 打印耗时 | 打印耗时，异常继续抛 |
| `except` + `raise` + `finally` | 打印耗时 | `failed` + 耗时 + 异常继续抛 |

### 推荐写法

```python
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        except Exception:
            print("failed")
            raise
        finally:
            print(f"{func.__name__} took {time.perf_counter() - start:.3f}s")
    return wrapper
```

实测：

```text
--- 异常路径 ---
failed
bad took 0.050s
outer caught: boom

--- 正常路径 ---
good took 0.050s
result: ok
```

### `except` 与 `finally` 的职责

| 关键字 | 职责 | 执行条件 |
|---|---|---|
| `except` | 处理异常：补信息、转换、记录 | 只有异常时 |
| `finally` | 收尾：释放资源、打印耗时 | **无论正常还是异常** |

另外：`time.time()` 建议换成 `time.perf_counter()`，后者单调递增，不受系统时间被调整的影响。

---

## 六、英语词（本节相关）

| 词 | 含义 | 例句 |
|---|---|---|
| propagate | 向上冒泡 | The exception **propagates** out of the wrapper. |
| swallow | 吞掉（异常） | `retry` swallows intermediate failures. |
| finally block | finally 块 | A **finally block** always runs. |
| control flow | 控制流 | `timer` does not change **control flow**. |

---

## 原对话摘录 / Original conversation excerpt

> **2026-11-17**
> 学习者提问：
> **“为啥 `slow()` 接住了，另外两个没接住？”**

> 助教：
> `slow` 没有异常，`timer` 也没接。`flaky` 的异常在 `wrapper` 内被消化。`always_fail` 第三次 `raise` 出去了，所以必须 `try`。

---

*本篇所有 `text` 输出来自 `~/learning/.venv/bin/python` 实跑（脚本 `/tmp/timer_does_not_catch.py`）。*
