# 033 — 装饰器怎么记、怎么写

> Week 6 · Day 2 · 2026-11-17

## 问题

装饰器结构老是记不住，怎么才能记住？写的时候应该按什么顺序？

---

## 一、先背一句话

> **收一个函数 → 包一层 → 把新函数还回去。**

`@deco` 就是 `f = deco(f)`。本质只有这一件事。

---

## 二、手写顺序：固定 5 步

```python
def deco(func):                          # ① 收一个函数
    def wrapper(*args, **kwargs):        # ② 造一个能接任意参数的新函数
        result = func(*args, **kwargs)   # ③ 调原函数
        return result                    # ④ 交回数据
    return wrapper                       # ⑤ 交回函数
```

这 5 行就是全部骨架，其余全是填空。

| 想要的功能 | 填在哪 |
|---|---|
| 计时 | ③ 前记 `start`，④ 前打印耗时 |
| 重试 | 把 ③ 包进 `while` + `try` |
| 日志 | ③ 前打印入参，④ 前打印返回值 |
| 权限校验 | ③ 前判断，不通过就 `raise` |

记动作序列比记功能容易：

```text
def deco(func) → def wrapper → result = func(...) → return result → return wrapper
```

---

## 三、两层还是三层：看 `@` 后面有没有括号

| 写法 | 层数 | 展开 |
|---|---|---|
| `@deco` | **2 层** | `deco(func)` 返回 `wrapper` |
| `@deco(arg)` | **3 层** | `deco(arg)` 返回 `inner`，`inner(func)` 返回 `wrapper` |

**多一个参数，多包一层。** 这是最实用的判别法。

带参模板：

```python
def deco(arg):                    # ① 收参数
    def inner(func):              # ② 收函数
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        return wrapper            # ③ 交回函数
    return inner                  # ④ 交回装好的装饰器
```

和无参版的差别只有一点：最外面多套了一层 `deco(arg)`，里面三层完全一样。

---

## 四、口诀

> 外层收函数，内层干活，末尾还回去；
> 有括号多一层，无括号少一层；
> `wraps` 贴内层，两个 `return` 别漏。

---

## 五、怎么练才真的记住

### ① 白纸默写

不看答案，3 分钟写一遍（无参 + 带参）。连续 3 天每天两遍；之后隔 3 天、隔 7 天各一遍。

写不出来，说明只是“看懂了”，没进肌肉记忆。

### ② 默写后跑 4 项检查

- [ ] `@functools.wraps(func)` 贴在 `wrapper` 上方
- [ ] `wrapper` 参数是 `*args, **kwargs`
- [ ] 有 `return result`
- [ ] 最后有 `return wrapper`（带参版是 `return inner`）

这 4 项对应三类真实故障：

| 漏了 | 症状 |
|---|---|
| `wraps` | `f.__name__` 变成 `"wrapper"`，日志全错 |
| `return result` | 返回值变 `None`（见 032） |
| `return wrapper` | `TypeError: 'NoneType' object is not callable`（见 032） |

### ③ 最小自测

```python
@deco
def add(a, b):
    return a + b

print(add(1, 2))
```

能正常打印并保留函数名，骨架就对了。

### ④ 变式一次才算会

用同一个骨架写三种功能：计时、日志、重试。骨架不变、填空不同——这才叫“会写装饰器”，而不是“背下了一个装饰器”。

---

## 六、英语词（本节相关）

| 词 | 含义 | 例句 |
|---|---|---|
| skeleton | 骨架 | A decorator has a fixed **skeleton**. |
| fill in | 填空 | You **fill in** the timing logic. |
| muscle memory | 肌肉记忆 | Write it from memory until it becomes **muscle memory**. |
| variant | 变式 | Practice **variants** with the same skeleton. |

---

## 原对话摘录 / Original conversation excerpt

> **2026-11-17**
> 学习者提问：
> **“装饰器我要怎么才能记住？应该怎么写？”**

> 助教：
> 背 5 行骨架（收函数 → 包 wrapper → 调原函数 → return result → return wrapper），功能都是填空。看 `@` 后面有没有括号判断两层还是三层。

---

*本篇为学习法总结，无新增实测输出；引用的实测见 032。*
