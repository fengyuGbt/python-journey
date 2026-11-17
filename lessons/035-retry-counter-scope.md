# 035 — `@retry` 的计数为什么必须放在 `wrapper` 里

> Week 6 · Day 2 练习 · 2026-11-17

## 最终版本（已通过验收）

```python
import functools


def retry(times=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"第{i}次失败: {type(e).__name__}: {e}")
                    if i == times:
                        raise
        return wrapper
    return decorator
```

实测输出：

```text
第1次失败: ValueError: fail #1
第2次失败: ValueError: fail #2
flaky -> ok
第1次失败: RuntimeError: boom
第2次失败: RuntimeError: boom
第3次失败: RuntimeError: boom
final: RuntimeError boom
```

验收表：

| 检查项 | 结果 |
|---|---|
| 三层结构 | ✅ |
| `functools.wraps` 位置 | ✅ |
| 每轮打印次数 + 异常类型 + 消息 | ✅ |
| 全失败抛出原始异常 | ✅ |
| 成功返回原值 | ✅ |
| 计数在 `wrapper` 内，跨调用不累积 | ✅ |

**测试脚本必须自己 `print` 返回值、自己 `try` 接住异常**，否则成功看不到、失败直接崩。

---

## 学习者首版（跑不起来）

```python
def retry(times=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"第{times - retry_coune + 1}次失败: {type(e).__name__}: {e}")
                retry_count -= 1
                if retry_count > 0:
                    return wrapper(*args, **kwargs)
                else:
                    raise
        return wrapper
    return decorator
```

实测：

```text
--- flaky ---
ERR: NameError name 'retry_coune' is not defined
```

---

## 一、三个问题

### ① 变量名拼错且未定义

`retry_coune` 多了一个 `e`，而且整个函数里没有任何地方定义过它，所以进入 `except` 立刻 `NameError`。

### ② 就算改名，作用域也错

`retry_count` 需要初始化。如果写在 `decorator` 层（`retry_count = times`），它会**跨调用共享**：第一次调用把 3 减到 0，第二次调用直接不重试。

计数必须放在 `wrapper` 内部，**每次调用重新开始**。

### ③ 递归重试会叠栈

`return wrapper(*args, **kwargs)` 每失败一次就多一层调用栈。3 次没事，`times=100` 就会打深；而且计数器藏在闭包里，很难看清当前到第几次。

---

## 二、修正版（推荐：for 循环）

```python
import functools


def retry(times=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"第{i}次失败: {type(e).__name__}: {e}")
                    if i == times:
                        raise          # 最后一次，原样抛出
        return wrapper
    return decorator
```

实测三种场景：

```text
--- flaky ---
第1次失败: ValueError: fail #1
第2次失败: ValueError: fail #2
result: ok

--- flaky 再调一次 ---
result: ok

--- always_fail ---
第1次失败: RuntimeError: boom
第2次失败: RuntimeError: boom
第3次失败: RuntimeError: boom
final: RuntimeError boom

--- times=1 ---
第1次失败: ValueError: only once
final: ValueError only once
```

关键点：

- `i` 是 `range` 的局部变量，天然每次调用重置，不存在跨调用污染。
- `if i == times: raise` 写在 `except` 内，抛出时保留原始 traceback，比循环外 `raise last_exc` 更干净。
- 成功时 `return` 立刻跳出，不会继续重试。

---

## 三、如果坚持用递归

把次数变成参数，不要用外部变量递减：

```python
def wrapper(*args, **kwargs):
    def attempt(n):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"第{n}次失败: {type(e).__name__}: {e}")
            if n < times:
                return attempt(n + 1)
            raise
    return attempt(1)
```

好处：

- 不用 `-=`，也不用担心闭包被跨调用共享。
- `n` 显式传参，当前第几次一眼可见。

代价：仍然有递归栈深度。

---

## 四、结论

| 做法 | 计数放哪 | 每次调用重置 | 栈深度 |
|---|---|---|---|
| 闭包变量递减 | `decorator` 层 | ❌ 会累积 | 递归叠栈 |
| 循环 | `wrapper` 内 `range` | ✅ | 恒定 |
| 递归传参 | `attempt(n)` 参数 | ✅ | 叠栈 |

**计数属于“一次调用”的状态，就必须放在每次调用都会重新执行的那一层。**

---

## 五、补充：循环次数已定，为什么还要 `if i == times: raise`

学习者追问：

> 既然 `range` 已经确定了试几次，为什么还要加一个 `if`？

因为两件事分工不同：

| 代码 | 负责 |
|---|---|
| `for i in range(1, times + 1)` | 重复执行，**试几次** |
| `return func(...)` | 成功时提前跳出 |
| `if i == times: raise` | 最后一轮失败时**把异常交还调用方** |

循环只管“重复”，不管“跑完之后返回什么”。

### 去掉 if 的实测

```python
def wrapper(*args, **kwargs):
    for i in range(1, times + 1):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"第{i}次失败: {type(e).__name__}: {e}")
    # 没有 if i == times: raise
```

```text
第1次失败: RuntimeError: boom
第2次失败: RuntimeError: boom
第3次失败: RuntimeError: boom
result: None | type: NoneType
```

三次都试了，但函数掉出循环后没有 `return` 也没有 `raise`，Python 隐式返回 `None`——**异常被吞掉，调用方以为成功了**。

### 边界含义

- 前 `times - 1` 次失败 → “还有机会再试”，吞掉异常继续。
- 第 `times` 次失败 → “没机会了”，必须抛。

`if i == times` 判断的就是这个分界点。

### 其他写法对比

| 写法 | 额外成本 |
|---|---|
| `if i == times: raise` | 无，traceback 保留原位 |
| `for...else: raise last_exc` | 需保存 `last_exc`，traceback 重新开始 |
| 循环后 `raise last_exc` | 同上 |

---

## 六、补充：裸 `raise` 只能写在 `except` 里

第二版把 `if i == times: raise` 缩进了 `for` 层（与 `except` 同级），实测后果：

```text
第1次失败: RuntimeError: boom
第2次失败: RuntimeError: boom
第3次失败: RuntimeError: boom
外层收到: RuntimeError | No active exception to reraise
```

三次尝试都执行了，但抛出去的不是原始的 `boom`，而是 `No active exception to reraise`。

原因：裸 `raise` 的含义是“重新抛出**当前正在处理**的异常”。离开 `except` 块后，Python 已经清理了异常上下文（并在 3.x 中 `del e`），再 `raise` 就没有活动异常可抛。

正确缩进：

```python
for i in range(1, times + 1):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"第{i}次失败: {type(e).__name__}: {e}")
        if i == times:
            raise          # 必须留在 except 里
```

| 写法 | 结果 |
|---|---|
| `raise` 在 `except` 内 | 抛出原始异常，traceback 保留 |
| `raise e` 在 `except` 内 | 同样抛原始对象，但 traceback 从这一行重新开始 |
| `raise` 在 `except` 外 | `RuntimeError: No active exception to reraise` |
| `raise e` 在 `except` 外 | `UnboundLocalError: cannot access local variable 'e'` |

### 为什么不能放外面：成功路径根本不需要它

学习者追问：

> 正常运行时 `except` 会被跳过，那它没办法最后收尾呀？

要反过来看：

| 情形 | 是否需要这个 `if` |
|---|---|
| 成功 | **不需要**。`return` 已经提前结束函数，`if` 里外都碰不到 |
| 失败 | **需要**。而且只有此时 `if` 才会执行 |

所以决定因素全在失败路径：

| 放法 | 成功 | 失败 |
|---|---|---|
| `if` 在 `except` 内 | 不执行 | 正常抛出原始异常 |
| `if` 在 `except` 外 | 不执行 | 裸 `raise` 失效 / `e` 已删除 |

两种 `raise` 在 `except` 外都坏：

- **裸 `raise`**：依赖“当前正在处理的异常”。离开 `except`，上下文被清除 → `No active exception to reraise`。
- **`raise e`**：Python 3 在 `except` 结束时会 `del e`（防止异常对象与 traceback 形成引用环），外部访问报 `UnboundLocalError`。

一句话：**成功时不收尾是因为已经 `return` 了；失败时要收尾，而站在 `except` 外面就没有异常可抛。**

---

## 七、英语词（本节相关）

| 词 | 含义 | 例句 |
|---|---|---|
| scope | 作用域 | The counter has the wrong **scope**. |
| reset | 重置 | The counter must **reset** on every call. |
| recursion depth | 递归深度 | Retrying by recursion increases **recursion depth**. |
| retry policy | 重试策略 | A **retry policy** defines how many attempts to make. |

---

## 原对话摘录 / Original conversation excerpt

> **2026-11-17**
> 学习者提交首版 `@retry`（用 `retry_count -= 1` 递归重试）

> 助教：
> `retry_coune` 拼错且从未定义 → `NameError`。计数必须在 `wrapper` 内部初始化，否则跨调用累积；建议用 `for i in range(1, times+1)`。

---

*本篇所有 `text` 输出来自 `~/learning/.venv/bin/python` 实跑（脚本 `/tmp/retry_v1.py`、`/tmp/retry_v2.py`）。*
