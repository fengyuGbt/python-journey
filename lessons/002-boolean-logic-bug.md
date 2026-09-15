# 002 · 密码检查的布尔逻辑 bug / Boolean-logic bug in password check

## 中文

**场景**：密码强度检查。规则：长度 ≥ 8、含字母、含数字。满足 3 个 = 强，2 个 = 中，否则 = 弱。

**我的错误代码**（weak 分支）：

```python
elif not len(password) > 7 and not (any(c.isalpha() for c in password) and not any(c.isdigit() for c in password)):
    print("Password safety is weak")
```

**现象**：输入 `a`（长度 1、只有字母、没数字）被判成"中"，应该是"弱"。

**分析**：用德摩根律化简 `not (A and not B)`：

```
weak = 长度≤7 且 (不含字母 或 含数字)
```

方向写反了——我想表达"缺字母或缺数字"，实际写成了"不含字母 **或** 含数字"。

**根因**：把"数一数满足几个条件"的事，写成了层层嵌套的布尔表达式。**复杂条件就是 bug 温床。**

**教训**：
1. 条件超过一个，先给每个条件起个清晰的名字（`length` / `has_letter` / `has_digit`），再组合。
2. **可读性 = 正确性**。
3. Python 里 `True` 等于 `1`，`sum([...])` 可以"数条件"。

**修复**：

```python
length = len(password) > 7
has_letter = any(c.isalpha() for c in password)
has_digit = any(c.isdigit() for c in password)
score = sum([length, has_letter, has_digit])

if score == 3:
    print("strong")
elif score == 2:
    print("medium")
else:
    print("weak")
```

---

## English

**Situation**: a password strength checker. Rules: length ≥ 8, has letter, has digit. 3 met = strong, 2 = medium, else weak.

**My buggy code** (weak branch):

```python
elif not len(password) > 7 and not (any(c.isalpha() for c in password) and not any(c.isdigit() for c in password)):
    print("Password safety is weak")
```

**Symptom**: input `a` (length 1, letter only) was judged "medium"; it should be "weak".

**Analysis**: by De Morgan's law, `not (A and not B)` simplifies to:

```
weak = length ≤ 7 and (no letter OR has digit)
```

The direction was wrong — I meant "missing letter OR missing digit", but wrote "no letter **OR** has digit".

**Root cause**: I turned "count how many conditions are met" into nested boolean expressions. **Complex conditions are a bug nest.**

**Lessons**:
1. When you have more than one condition, name each one first (`length` / `has_letter` / `has_digit`), then combine.
2. **Readability = correctness.**
3. In Python `True` equals `1`, so `sum([...])` counts conditions.

**Fix**: see the Chinese section above.
