# 021 · 20 道综合练习题复盘 / Week 4 comprehensive exercises (20/20)

## 中文

**背景**：L1 第 4 周 Day 2「知识补漏」——培训计划要求"2 天完成 20 道综合练习题"，附录 A 只给了 L1 五题示意，按**五种能力组合矩阵**（字符串 / 列表 / dict / 函数 / 文件 / 异常）扩写成 20 题，分 4 批 × 5 题下发，每题**手写 + 运行验收**。20/20 全部通关，本 lesson 记录每题要点与**本轮新踩到的坑**。

---

### 20 题总览

| # | 能力组合 | 题目 | 验收结果 |
|---|---|---|---|
| 1 | 列表 | 反转 `[1,2,3,4,5]`（切片 + 就地两种） | ✅ |
| 2 | 字符串 | `"hello world"` 单词首字母大写 | ✅ |
| 3 | dict | `d.get("c", 0)` 安全取值 | ✅ |
| 4 | 函数 | `is_palindrome(s)` 忽略大小写和空格 | ✅ |
| 5 | 文件+异常 | 读 `data.txt` 数字行求和，坏行跳过 | ✅ |
| 6 | 列表+dict | 找重复元素（保序） | ✅ |
| 7 | 字符串+dict | `count_words` 词频统计（去标点） | ✅ |
| 8 | dict+函数 | `grade_book` 分数→等级 | ✅ |
| 9 | 文件+dict | 读 `name,score` 行，坏行跳过 | ✅ |
| 10 | 文件+函数 | 单词数 + 行数（一个 with） | ✅ |
| 11 | 列表+函数 | `apply_all(funcs, x)` 依次应用 | ✅ |
| 12 | dict+排序 | `top_n` 按值降序取前 n | ✅ |
| 13 | 字符串+异常 | `safe_float` 失败返回 None | ✅ |
| 14 | 文件+JSON | save/load JSON（encoding + ensure_ascii） | ✅ |
| 15 | 列表推导 | 1–100 能被 3 整除且不能被 5 整除（27 个） | ✅ |
| 16 | 综合 | `merge_counts` 合并词频，不改入参 | ✅ |
| 17 | 综合 | `dedup_keep_order` 去重保序 | ✅ |
| 18 | 综合 | `copy_valid_lines` 复制数字开头的非空行 | ✅ |
| 19 | 综合 | `char_stats` 字符计数过滤空白 | ✅ |
| 20 | 综合工具 | `word_analysis.py` CLI：读文件→词频 Top N | ✅ |

---

### 本轮新踩的坑（重点）

**坑 1 · `[0:2]` 魔法切片（题 6）**
错误版 `[item for item in items if count[item] > 1][0:2]`——列表推导会**重复保留**同一个元素（3 出现 3 次保留 3 个 3），切片切在**未去重的中间结果**上。验收用例 `[3, 1, 2, 3, 4, 1, 5, 3]` 恰好把两个重复元素的首次出现排前面，**碰巧蒙对**；换反例 `[3, 3, 1, 1]` 立即输出 `[3, 3]`（错）。正确写法：

```python
return [item for item, c in count.items() if c > 1]   # Counter 按首次出现顺序保存键，天然保序去重
# 要 limit 就再切：result[:limit]
```

**教训**：① 切片不能"补救"上游重复——**先保证结果集合正确，再谈取几个**；② **单个测试用例通过 ≠ 代码正确**，必须跑反例。

**坑 2 · `strip()` 只剥首尾（题 7）**
`text.strip(",.!?;:")` 只去掉**字符串开头和结尾**的标点，中间的标点一概不动——`"Hello, world!"` 会统计出带逗号的 `'hello,'`。`strip()` 是"剥首尾"，不是"清洗全文"。修复：逐词 `w.strip(...)` 或正则 `re.findall(r'\b\w+\b', text.lower())`。

**坑 3 · `except ValueError` 漏掉 TypeError（题 13）**
`float("abc")` 抛 `ValueError`，但 `float(None)`、`float([])` 抛 **`TypeError`**——只接 ValueError 挡不住"类型错"。修复：`except (ValueError, TypeError)`。

**坑 4 · 生成器 vs 集合（题 12）**
`yield` 版 `top_n` 功能正确但**只能遍历一次**、调用方必须 `list()` 包装；"返回结果集合"的场景 `return sorted(...)[:n]` 更直接。yield 是 L2 正式内容，先用 return。

**坑 5 · 测试数据写进工具脚本（题 20）**
`word_analysis.py` 里 `open("notes.txt", "w")` 造数据是测试行为，不属于工具本身——工具应该只读 `args.file`。测试数据用命令行生成，不写进产品代码。

**加分项（记录）**
- 题 18 用 `line.lstrip()[0].isdigit()` 处理**前导空格**行（`line[0]` 会取到空格误判）——比提示版本更稳。
- 题 20 的 `sorted(word_count.items(), key=lambda x: (-x[1], x[0]))`——**负号把频次变降序 + 同频按字母序**，一次 sort 双规则，词频 Top N 经典写法。
- 题 10 主动从 `readlines()` 整读改成流式 `for line in f`（内存 O(1)）。
- 题 13/14 采纳点评：`except (ValueError, TypeError)`、`import json` 移文件顶部。

---

## 对话摘录（概念问答）

**问：`except ValueError: continue` 里的 continue 能省略？**
能。`continue` 是"跳过本轮剩余代码直接进下一轮"；当 except 后面**没有剩余代码**时，跳不跳结果一样。什么时候必须留？except 后面**还有代码**时——出错行要跳过后续语句（否则 `print(n)` 会因 `n` 不存在而 `NameError`）。判断标准：**看 except 后面还有没有要执行的语句**。

**问：continue 和 break 的区别？**
`continue` = 跳过**当前这一轮**，回到循环顶部继续下一轮；`break` = 结束**整个循环**，执行循环之后的代码。**两者都只作用于最近一层循环**——内层 `break` 跳不出外层（要两层全退用标志变量或 `return`）。

**问：dict 是可变对象？**
是。增删改都是**原地操作**（`d["k"]=v` 改的是 d 自己）。可变对象（list/dict/set）**传参是引用**——函数里改 dict，外面原 dict 也变（题 8 的副作用）；要保护入参就 `dict(d1)` 复制（题 16）。不可变对象（str/int/tuple）传参安全，因为"一改就造新的"。

**问：`sorted(d.items(), key=lambda item: item[1], reverse=True)[:n]` 是啥？**
三步：① `d.items()` 拿 (键,值) 对子；② `key=lambda item: item[1]` 告诉 sorted"按每对的第 2 个字段（值）排"（默认按元组整体先比键，是字母序不是值序，所以必须写 key）；③ `reverse=True` 降序、`[:n]` 取前 n。lambda 等价于 `def f(item): return item[1]`。

**问：`s.replace(" ", "")` 为啥必须接返回值？**
字符串**不可变**——`replace()` 不修改 `s` 本身，而是**返回一个新字符串**。不赋值，新串就被丢弃，`s` 纹丝不动。列表的"动作类"方法（`reverse`/`sort`/`append`）是就地改、返回 None；字符串的方法全是"复印机"——**看到字符串方法，默认要赋值接住**。

---

## English

**Context**: Week 4 Day 2 "knowledge patch-up" — the plan says "20 comprehensive exercises in 2 days"; Appendix A only sketches 5, so they were expanded into 20 across a **five-skill combination matrix** (strings / lists / dicts / functions / files / exceptions), issued in 4 batches × 5, each **hand-written + acceptance-run**. 20/20 passed. This lesson records each exercise's point and the **new traps hit along the way**.

### New traps this round

1. **Magic slice `[0:2]` (Q6)**: `[item for item in items if count[item] > 1][0:2]` slices the **undeduplicated intermediate** — the comprehension keeps one entry per occurrence. The acceptance case happened to look right; counter-example `[3, 3, 1, 1]` printed `[3, 3]`. Fix: iterate `count.items()` (Counter preserves first-seen order) — dedupe first, slice later. **A single passing case ≠ correct code; run counter-examples.**
2. **`strip()` only trims the ends (Q7)**: punctuation in the middle survives; `"Hello, world!"` yields `'hello,'`. Use per-word strip or regex `\b\w+\b`.
3. **`except ValueError` misses `TypeError` (Q13)**: `float(None)` / `float([])` raise `TypeError`, not `ValueError`. Fix: `except (ValueError, TypeError)`.
4. **Generator vs collection (Q12)**: a `yield` version works but is single-pass and needs `list()`; `return sorted(...)[:n]` is more direct for "return a result set".
5. **Test data inside the tool (Q20)**: writing `notes.txt` inside `word_analysis.py` is test scaffolding, not tool behavior — keep tools reading only `args.file`.

**Credited**: Q18 `line.lstrip()[0].isdigit()` handles leading-space lines (better than `line[0]`); Q20 `key=lambda x: (-x[1], x[0])` — negative count for descending + alphabet for ties, the classic Top-N sort; Q10 upgraded from `readlines()` to streaming `for line in f` on the user's own initiative; Q13/Q14 adopted `except (ValueError, TypeError)` and top-level `import json`.

---

## Q&A highlights

- **Can `continue` be dropped in `except`?** Yes, when nothing follows the `except` block — "skip the rest of this round" skips nothing. Keep it when statements follow (else a failed line would hit `NameError` on the unbound name).
- **`continue` vs `break`?** `continue` skips this round and continues the loop; `break` ends the whole loop. **Both act on the nearest loop only** — an inner `break` cannot exit the outer one.
- **Is `dict` mutable?** Yes — in-place add/change/delete. Mutable objects pass by reference: mutating a dict in a function mutates the caller's dict (Q8 side effect); protect inputs with `dict(d1)` copy (Q16). Immutable objects (str/int/tuple) are safe to pass.
- **What is `sorted(d.items(), key=lambda item: item[1], reverse=True)[:n]`?** `items()` gives pairs; `key=lambda item: item[1]` sorts by the value field (default would sort by key first); `reverse=True` descends; `[:n]` takes the first n.
- **Why must `s.replace(...)` be assigned?** Strings are immutable — `replace()` returns a **new string**; without assignment the change is discarded. String methods are "copy machines"; list action methods (`reverse`/`sort`/`append`) mutate in place and return `None`.
