# 020 · 第 4 周知识补漏：前三周坑清单复盘 / Week 4 trap-list review (014–019 redone)

## 中文

**背景**：L1 第 4 周 Day 1「知识补漏」——把前三周六个 lesson（014–019）的坑逐一重做。规则：每题**手写修复，不抄 lesson**，运行验收通过才算过。六题全部通关，本复盘记录每题的实际修复与**新踩到的坑**。

---

### 第 1 题（014 · 复制粘贴下标）

坑版：`by` 分支 `category = parts[2]`（从 `add` 复制，只改了命令没改下标，`by 餐饮` 只有 2 段）+ `parts.__len__ < 2`。

修复：

```python
if not parts:                    # ← 新补的边界：空输入！cmd.split() 返回 []，parts[0] 会 IndexError
    return "no command provided"
if len(parts) < 2:              # len() 是方法调用的语法糖，不是属性
    ...
category = parts[1]             # 复制后逐行数下标：by 只有 2 段
```

验收 5 用例全过（含空字符串 `""`）。**新教训**：边界测试必须包含空输入——`handle("")` 时 `parts[0]` 直接崩，测试列表里没有空串就发现不了。

### 第 2 题（015 · open 无 with）

坑版：第二个 `open()` 无 `with`、同文件读两遍。修复为一个 `with` 一个循环，求和计数一起算：

```python
with open("squares.txt", "r") as f:
    total = 0
    count = 0
    for line in f:
        total += int(line.strip())
        count += 1
```

**翻车事件**：第一次运行输出 `338350 / 0`（count 应为 100）——贴的代码是对的，但**运行的文件是旧的**（没保存）。教训（再次验证）：**代码贴出来 ≠ 文件内容 ≠ 运行结果**，一切以 `cat` + 运行输出为准。

### 第 3 题（016 · main 没调用 + ensure_ascii 错位）

坑版：`def main()` 无调用入口；`ensure_ascii=False` 放进了 `open()`。

修复：

```python
with open("people.json", "w", encoding="utf-8") as f:   # open 管编码
    json.dump(data, f, ensure_ascii=False)              # dump 管转义

if __name__ == "__main__":                              # 写了 main 必有入口
    main()
```

验收：`python review2.py` 输出中文人名，`cat people.json` 落盘中文无 `\uXXXX` 转义。

### 第 4 题（017 · 死比较表达式 + except 不匹配）

坑 1：`operation == '/'` 当独立语句是死代码。**第一次只删了那行，else 分支仍是 `return divide(a, b)`——"删了表演没改剧情"**：`evaluate(1, 2, 'x')` 返回 0.5 不报错。死代码的本质是 else 的逻辑错误（任何未知操作符静默走除法），修复为 fail fast：

```python
else:
    raise ValueError("Invalid operation")   # 输入非法就该炸，不该悄悄算个 0.5 骗人
```

坑 2：`divide` 里 `raise ValueError` 与调用方 `except ZeroDivisionError` 不匹配。修复用语义正确的原生类型：

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
```

### 第 5 题（018 · CLI 三坑）

三坑全修：`p.exists()` 死代码 → `if not p.is_dir()`；`--ext py` vs `suffix == ".py"` 契约 → `ext = args.ext if args.ext.startswith(".") else "." + args.ext`；`== ext: continue` 判断反 → `!= ext: continue`。

两个 P1 工程细节（不阻塞功能但真实工具要改）：
1. **契约计算只做一次，放循环外**——放在 for 里每次迭代重算是冗余（幂等但奇怪）
2. **`is_dir()` 比 `exists()` 稳**——`exists()` 对"存在但是个文件"的路径返回 True，`iterdir()` 会崩；`is_dir()` 一个条件同时覆盖"不存在"和"不是目录"

### 第 6 题（019 · 快照竞态）

**复盘大发现**：原坑版 `for file in src.iterdir(): ... mkdir + move` **带了 `is_file()` 过滤，新建的"归档"目录被跳过——结构性不会翻车**。连跑 5 次全正常不是运气，是保护在起作用。真正的翻车现场（organizer 历史 log 为证）是**无过滤版本**：分类目录被当成条目，`classify(目录名)` 返回"其他"，目录被移进"其他"，`Cannot move a directory into itself`。

**确定性复现**（不靠运气）：去掉过滤 + 预建"归档"目录：

```python
for file in src.iterdir():            # 无 is_file 过滤
    dst = src / "归档"
    dst.mkdir(exist_ok=True)
    shutil.move(file, dst / file.name)
```

→ `OSError: Cannot move a directory 'messy2/归档' into itself 'messy2/归档/归档'`。

快照修复后连跑 3 次，结果每次都一样：

```python
files = [f for f in src.iterdir() if f.is_file()]   # 快照：遍历结束
for file in files:                                   # 处理：随便 mkdir / move
    ...
```

**核心结论**：`is_file()` 只挡得住"目录被移走"这一种后果，挡不住"遍历时修改目录"本身的不确定性（跳过未处理文件、顺序漂移、清单不一致）。快照是**结构保证**——遍历和修改物理隔离，行为确定。**"本地测过没翻"不可信**：未定义行为的意思就是可能在你机器上永远正常、在用户机器上随机发作。

---

## 对话摘录（概念问答）

**问：`__len__` 是方法不是属性，为啥我理解是反的？**
因为 `len(x)` 用起来太像"读属性"——但 `parts` 前面的括号属于 `len` 函数，不是读 `parts` 的属性。真实形态是 `parts.__len__()`（方法调用，带括号）。判断法："**要不要括号**"——属性直接出值（`file.suffix`、`parts[0]`），方法必须带括号（`file.is_dir()`、`parts.split()`、`parts.__len__()`）。

**问：`parts.__len__()` 和 `len(parts)` 等效，为啥不常用？**
`len()` 是**公共 API**，`__len__()` 是**内部钩子**。①可读性：`len(parts)` 表达意图，`parts.__len__()` 暴露实现；②协议统一：list/str/dict 全用 `len(x)`，不必知道类型；③封装：公共 API 稳定，内部实现可换；④规范：dunder 是给解释器和内置函数准备的（PEP 8 不鼓励直接调）。同族：`str(x)`/`x.__str__()`、`x == y`/`x.__eq__(y)`、`y in x`/`x.__contains__(y)`。

**问：`{cmd!r:>20}` 是啥？**
两个符号各管一件事：`!r` 用 `repr()` 显示（字符串带引号，debug 标配——空串显示为 `''` 而不是空白）；`:>20` 右对齐占 20 字符宽（`<` 左对齐、`^` 居中）。纯排版手段，让验收输出对齐。

**问：死代码的本质？**
比较表达式不 if 判断、不赋值，结果被丢弃，这一行什么都不做。但**死代码的"剧情"在 else 分支**——`else: return divide(a, b)` 才是"管你输什么一律除"的根源。删表演（那行比较）不算修完，要改剧情（else 分支 raise）。

---

## English

**Context**: Week 4 Day 1 "knowledge patch-up" — redo the traps from six earlier lessons (014–019), one by one. Rule: **hand-fix every trap, no copying from the lesson**, pass only after running the acceptance check. All six passed; this lesson records the actual fixes and the **new traps hit during review**.

### #1 (014 · copy-pasted index bug)

`by` branch had `category = parts[2]` (copied from `add`; `by 餐饮` has only 2 parts) and `parts.__len__ < 2`. Fix:

```python
if not parts:                    # ← new edge case: "" → [] → parts[0] would IndexError
    return "no command provided"
if len(parts) < 2:              # len() is sugar for calling the method
    ...
category = parts[1]             # count elements after copy-paste
```

**New lesson**: edge tests must include empty input — `handle("")` crashes on `parts[0]`, and you won't see it unless the test list has an empty string.

### #2 (015 · open without with)

Second `open()` had no `with`; same file read twice. Fix: one `with`, one loop, sum & count together. **Crash event**: first run printed `338350 / 0` — the pasted code was correct but the **file on disk was stale (unsaved)**. Lesson: what you pasted ≠ what's in the file ≠ what ran; trust `cat` + run output.

### #3 (016 · main never called + ensure_ascii misplaced)

`open()` owns `encoding`, `json.dump()` owns `ensure_ascii`. Script ends with `if __name__ == "__main__": main()`. Verified: Chinese names print, `people.json` stores real Chinese, no `\uXXXX`.

### #4 (017 · dead comparison + except mismatch)

First fix only deleted the dead line — the `else` still did `return divide(a, b)`, so `evaluate(1, 2, 'x')` silently returned `0.5`. **Deleting the showpiece isn't fixing the plot**: the real bug was the else branch. Fix: `raise ValueError("Invalid operation")` (fail fast). And `raise ZeroDivisionError` to match `except ZeroDivisionError` — use the semantically native type.

### #5 (018 · CLI three traps)

All three fixed: `p.exists()` dead code → `if not p.is_dir()`; extension contract → normalize `py` to `.py`; inverted `== ... continue` → `!= ... continue`. Two P1 details: compute the contract once *outside* the loop; prefer `is_dir()` over `exists()` (a path that exists but is a file passes `exists()` and then crashes `iterdir()`).

### #6 (019 · snapshot race)

**Review discovery**: the trap version with `is_file()` filtering **structurally cannot crash** — new directories are skipped. Five clean runs weren't luck, they were protection. The real crash scene (proven by the organizer log) is the **no-filter version**: category dirs get treated as entries, moved into "其他", then `Cannot move a directory into itself`.

**Deterministic reproduction** (no luck involved): drop the filter + pre-create the target dir → guaranteed `OSError: Cannot move a directory ... into itself`. Snapshot fix (`files = [...]` first, then process) ran 3× with identical results.

**Core conclusion**: `is_file()` only blocks one consequence (dirs being moved); it cannot fix the undefined behavior of "modifying a directory while iterating it" (skipped files, drifting order, inconsistent listing). Snapshot is a **structural guarantee** — iterate and modify are physically separated. **"It passed on my machine" is not evidence**: undefined behavior may never fire on your box and fire randomly on a user's.

---

## Q&A highlights

- **Why did I get `__len__` backwards?** `len(x)` *looks* like attribute access, but the parens belong to `len()`; the real form is `x.__len__()` — a method call. Test: "does it need parens?" Attributes give values directly (`file.suffix`); methods need `()` (`parts.split()`, `parts.__len__()`).
- **Why `len(x)` and not `x.__len__()`?** Public API vs internal hook: readability, protocol uniformity (works for list/str/dict without knowing the type), encapsulation (public API stable, internals swappable), and convention (dunders are for the interpreter).
- **What is `{cmd!r:>20}`?** `!r` = repr() (quoted string, debug-friendly); `:>20` = right-align, width 20. Pure formatting.
- **What is the essence of dead code?** A comparison with no `if` and no assignment discards its result — the line does nothing. But the *plot* lives in the `else` branch; deleting the line isn't fixing the logic.
