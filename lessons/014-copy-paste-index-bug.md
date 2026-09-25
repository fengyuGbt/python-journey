# 014 · 复制粘贴改了命令，没改下标 / Copy-pasted index bug

## 中文

**现象**：记账本 CLI 验收测试，其他命令全过，`by 餐饮` 直接崩：

```
Traceback (most recent call last):
  File "ledger.py", line 64, in main
    category = parts[2]
IndexError: list index out of range
```

**出错代码**：

```python
elif parts[0] == "by":
    if len(parts) < 2:            # 校验：至少 "by + 分类" 两段
        print("Usage: by <category>")
        continue
    category = parts[2]           # ← 崩！by 餐饮 只有 2 个元素，没有 parts[2]
```

**原因**：这段是从 `add` 分支**复制粘贴**来的。`add` 有 4 段（命令/金额/分类/备注），分类是 `parts[2]`；但 `by 餐饮` 只有 2 段（`["by", "餐饮"]`），分类应该是 `parts[1]`。命令改了，**下标没跟着改**。

**同类坑**：同一天还写过 `parts.__len__ < 3`——`__len__` 是方法不是属性，拿方法对象跟数字比较直接 TypeError。正确写法永远是 `len(parts)`（`len(x)` 是调用 `x.__len__()` 的语法糖）。

**怎么避免**：
1. 复制代码后，**先数清目标场景有几个元素**，再逐行核对下标（add 4 段 vs by 2 段）。
2. 边界测试每个命令都跑一遍（`by`、`by 分类`、`add`、`add 缺参`）。
3. 下标操作前想一句："这个列表最长几个元素？"

---

## English

**Symptom**: during acceptance testing of the ledger CLI, every command passed except `by 餐饮`, which crashed:

```
Traceback (most recent call last):
  File "ledger.py", line 64, in main
    category = parts[2]
IndexError: list index out of range
```

**The buggy code**:

```python
elif parts[0] == "by":
    if len(parts) < 2:            # check: at least "by + category"
        print("Usage: by <category>")
        continue
    category = parts[2]           # ← crash! ["by", "餐饮"] has no parts[2]
```

**Why**: this branch was **copy-pasted from the `add` branch**. `add` splits into 4 parts (command/amount/category/note) so the category is `parts[2]`; but `by 餐饮` splits into only 2 parts (`["by", "餐饮"]`), so the category is `parts[1]`. The command was changed, **the index was not**.

**Same-day sibling bug**: also wrote `parts.__len__ < 3` — `__len__` is a *method*, not an attribute; comparing a method object to a number raises TypeError. Always write `len(parts)` (`len(x)` is syntactic sugar for calling `x.__len__()`).

**How to avoid**:
1. After copying code, **count how many elements the target case actually has**, then check every index line by line.
2. Test every command including edge cases (`by`, `by 分类`, `add`, `add` with missing args).
3. Before indexing, ask: "what is the max length of this list?"

---

## 原对话摘录 / Original conversation excerpt

> 摘自学习者与 AI 助教的真实对话（2026-09-25）。

**学习者贴的报错**：

> "by 餐饮 → Traceback (most recent call last): File ledger.py line 64 in main → category = parts[2] → IndexError: list index out of range"

**助教点评**：

> "你八成是从 add 分支复制的——add 里 category = parts[2]（add 有 4 段），但 by 只有 2 段，分类是 parts[1]。这是经典 bug 来源：复制代码时忘了改下标。记住——从别的分支复制，先数一遍新场景有几个元素。"

**学习者修正后重测**：

> "by 餐饮 → Amount: 30.0, Category: 餐饮, Note: 午饭 ✅ / by 娱乐 → No records found ✅ / by → Usage ✅ / exit ✅"
