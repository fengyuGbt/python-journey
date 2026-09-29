# 015 · 第二个 open() 没关 / An open() without with — leaked handle

## 中文

**现象**：记账本 → 第 3 周练习 2（统计 `squares.txt` 行数与总和），第一版代码：

```python
with open("squares.txt", "r") as f:
    total = 0
    for line in f:
        total += int(line.strip())
    print(total)
    count = sum(1 for line in open("squares.txt"))   # ← 又开了一次，且没有 with！
    print(count)
```

**问题**：
1. **句柄泄漏**：第二个 `open()` 没有 `with` 也没有 `close()`。文件一直占用着（Windows 下表现为"文件被占用、删不掉"）。程序退出时垃圾回收会兜底，但这是坏习惯——资源应该**显式、及时**释放。
2. **重复打开**：数行数明明可以在第一个循环里顺手做（`count += 1`），却把同一个文件又读了一遍，低效。

**正确写法**（一个 `with`、一个循环、两件事一起算）：

```python
with open("squares.txt", "r") as f:
    total = 0
    count = 0
    for line in f:
        total += int(line.strip())
        count += 1
print(f"行数: {count}")
print(f"总和: {total}")
```

**核心原则**：
- 所有 `open()` 都用 `with`（自动关闭，异常也关）。
- 一个文件**只开一次**；同一个循环里能一起算的（求和 + 计数）就一起算。
- `with` 只管文件生命周期，数据算完存进变量，文件即可关闭。

**顺带**：`p.exists` 忘了加括号（方法要调用才执行）——同 014 的 `__len__` 一类：**方法后面永远带 `()`**。

---

## English

**Symptom**: Week 3 practice 2 (count lines & sum of `squares.txt`), first version:

```python
with open("squares.txt", "r") as f:
    total = 0
    for line in f:
        total += int(line.strip())
    print(total)
    count = sum(1 for line in open("squares.txt"))   # ← opened again, no with!
    print(count)
```

**Problems**:
1. **Leaked handle**: the second `open()` has no `with` and no `close()`. The file stays locked (on Windows: "file in use, cannot delete"). GC cleans up on exit, but resources should be released explicitly.
2. **Double reading**: counting lines could be done inside the first loop (`count += 1`), instead of reading the same file a second time.

**Correct** (one `with`, one loop, two results):

```python
with open("squares.txt", "r") as f:
    total = 0
    count = 0
    for line in f:
        total += int(line.strip())
        count += 1
print(f"lines: {count}")
print(f"total: {total}")
```

**Core rules**:
- Every `open()` uses `with` (auto-close, even on exceptions).
- Open each file **once**; compute together what one loop can compute.
- `with` owns the file's lifecycle — once data is in variables, close it.

**Also**: `p.exists` without parentheses (methods must be called) — same family as 014's `__len__`: **methods always end with `()`**.

---

## 原对话摘录 / Original conversation excerpt

> 摘自学习者与 AI 助教的真实对话（2026-09-29）。

**学习者第一版代码**（练习 2）：

> "with open('squares.txt','r',) as f: total = 0; for line in f: total += int(line.strip()); print(total); count = sum(1 for line in open('squares.txt')); print(count)"

**助教点评**：

> "第二个 open() 没关（句柄泄漏）——这正是在 Windows 下文件被占用删不掉的根因。更不合理的是：你为了数行数把文件又打开了一遍，第一遍明明就能同时数。改法：一个循环同时干两件事。"

**学习者修正后**：

> "with open('squares.txt','r',encoding='utf8') as f: total = 0; count = 0; for line in f: total += int(line.strip()); count += 1; print(total); print(count)" — ✅ 通过（338350 / 100）
