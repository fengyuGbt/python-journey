# 037 — Day 2 装饰器四练收尾：`@lru_cache` 的 hits 为什么这么小

> Week 6 · Day 2 · 2026-11-17

## 本日四道练习总览

| 练习 | 层数 | 核心考点 | 状态 |
|---|---|---|---|
| `@timer` | 2 | 计时 + `try/finally` 异常路径也能计时 | ✅ 通过 |
| `@retry(times=3)` | 3 | 计数作用域、最后一次抛异常、裸 `raise` 位置 | ✅ 通过 |
| `@logged` | 2 | 打印函数名/args/kwargs/返回值，异常路径记录 | ✅ 通过 |
| `@lru_cache` | 2（库实现） | 缓存命中、`cache_info()` 解读 | ✅ 通过（缺第二次调用，已补测） |

---

## 一、`@lru_cache` 实测

```python
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


@functools.lru_cache(maxsize=None)
def fib_cached(n):
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)
```

实测输出：

```text
fib(30) took 0.247 seconds
fib(30) = 832040
fib_cached(30) took 0.000 seconds
fib_cached(30) = 832040
CacheInfo(hits=28, misses=31, maxsize=None, currsize=31)

--- 第二次调用 ---
fib_cached(30) again took 0.000001 seconds
same result: True
CacheInfo(hits=29, misses=31, maxsize=None, currsize=31)
```

---

## 二、hits 为什么只有 28

无缓存 `fib(30)` 约 **130 万次**函数调用，缓存版总共只调用 **59 次**。

| 指标 | 数值 | 含义 |
|---|---|---|
| `misses` | 31 | 真正执行函数体的次数，`n=0..30` 各一次 |
| `hits` | 28 | 直接返回缓存、没进函数体的次数 |
| 总调用 | 59 | 31 + 28 |
| `currsize` | 31 | 缓存中保存的结果条数（键是 `n`） |

机制：计算 `fib(30)` 会先调 `fib(29)`，这一路把 `29, 28, ..., 0` 全部算完并缓存；回到上层再要 `fib(28)` 时，值已存在，直接 hit。

所以 **每个 n 只算一次，第二次访问必然命中**。

- `hits` 统计的是“越过了函数体、直接返回缓存”的次数，不是“省下的总调用次数”。
- 耗时从 0.247s 降到微秒级，本质是**少算了 130 万次**，不是算得更快。

### 第二次调用的变化

| 指标 | 第一次后 | 第二次后 |
|---|---|---|
| `hits` | 28 | 29（+1） |
| `misses` | 31 | 31（不变） |
| `currsize` | 31 | 31（不变） |
| 耗时 | 0.000s | 0.000001s |

第二次调用只走一次 wrapper，直接命中根节点 `n=30`。

---

## 三、`lru_cache` 的几个要点

| 项 | 说明 |
|---|---|
| `maxsize=None` | 缓存不设上限；`maxsize=128` 是默认值 |
| 适用条件 | 函数必须是**纯函数**（同样输入永远同样输出），且参数可哈希 |
| 不适用 | 有副作用、依赖外部状态、参数是 list/dict 等不可哈希对象 |
| LRU 含义 | Least Recently Used，超出 `maxsize` 时淘汰最久未使用的条目 |
| `cache_clear()` | 清空缓存，测试时常用 |

---

## 四、Day 2 四个坑汇总

| # | 坑 | 现象 | 结论 |
|---|---|---|---|
| 1 | `retry_count` 未定义 / 拼成 `retry_coune` | `NameError` | 计数变量必须先初始化 |
| 2 | 计数放在 `decorator` 层 | 第二次调用不重试 | 一次调用的状态放 `wrapper` 内 |
| 3 | 裸 `raise` 跑到 `except` 外 | `No active exception to reraise` | `raise` 必须留在 `except` 内 |
| 4 | `except` + `raise` 代替 `finally` 计时 | 异常时无耗时输出 | 收尾逻辑必须放 `finally` |
| 5 | `@lru_cache` 忘记第二次调用 | 看不到 hits 增长 | 对比类实验要跑两次 |

---

## 五、英语词（本节相关）

| 词 | 含义 | 例句 |
|---|---|---|
| cache hit | 缓存命中 | A **cache hit** returns without running the body. |
| cache miss | 缓存未命中 | The first call is always a **cache miss**. |
| memoization | 记忆化 | `lru_cache` implements **memoization**. |
| pure function | 纯函数 | Caching only works safely on a **pure function**. |
| evict | 淘汰 | LRU **evicts** the least recently used entry. |

---

## 原对话摘录 / Original conversation excerpt

> **2026-11-17**
> 学习者提交 `@lru_cache` 版本的 `fib` 对比（只调用一次）

> 助教：
> 缺第二次调用和第二次 `cache_info`。`hits=28` 不是“省下的调用数”，而是“直接命中缓存的次数”；无缓存 130 万次调用，缓存版只走 59 次。

---

*本篇所有 `text` 输出来自 `~/learning/.venv/bin/python` 实跑（脚本 `/tmp/lru_cache_check.py`）。*
