# 007 · 输出格式对照清单 / Output-format checklist

## 中文

**场景**：`enumerate` 练习。要求输出 `1. Alice / 2. Bob / 3. Carol`。

**我的第一版**：

```python
for i, name in enumerate(names):
    print(f"{i}: {name}")
```

输出是 `0: Alice / 1: Bob / 2: Carol` —— 序号从 0 开始、分隔符是 `:`，**两处都不符合要求**。

**修改第一处后**：

```python
print(f"{i+1}: {name}")
```

序号对了（`1.` 变 `1:` 了……不，是 `1: Alice`），但**分隔符还是 `:`**，要求是 `.`。又漏了第二处。

**分析**：`enumerate` 默认从 0 计数（`enumerate(names, start=1)` 或 `i + 1` 可以改）；要求的分隔符是 `.` 不是 `:`。

**根因**：修改时只盯着"序号"，没对照完整需求逐项检查。

**教训**：
1. **交付前逐项对照需求检查**：① 序号起点 ② 分隔符 ③ 标点 ④ 每行内容——逐项打勾。
2. 需求就是"客户要求"。hello.py 的提示语歧义、这次的输出格式——都是"没对照需求"的同类问题。
3. 检查清单化：改一处，过一遍全部项。

**修复**：

```python
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")
```

---

## English

**Situation**: an `enumerate` exercise required output `1. Alice / 2. Bob / 3. Carol`.

**My first version** printed `0: Alice / 1: Bob / 2: Carol` — the index started at 0 and the separator was `:`. **Both were wrong.**

**After fixing the index** (`{i+1}`) the separator was still `:` instead of `.`. I fixed one item and missed the other.

**Root cause**: I stared at "the index" and never checked the full requirement item by item.

**Lessons**:
1. Before delivery, check **every item** against the requirement: ① starting index ② separator ③ punctuation ④ content of each line — tick them off one by one.
2. The requirement is the client's spec. Ambiguous prompts (lesson 001) and wrong output format are the same disease: **not checking against the requirement.**
3. Checklist mindset: after changing one thing, re-verify everything.

**Fix**:

```python
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")
```
