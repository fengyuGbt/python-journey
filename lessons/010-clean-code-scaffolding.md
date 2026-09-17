# 010 · 清理脚手架：交付干净的代码 / Remove scaffolding: ship clean code

## 中文

**场景**：电话簿练习（L2 第 1 天）完成后，代码里还留着两类"历史痕迹"：① 上一版被注释掉的旧代码；② 助教留给学习者的两行提示注释（"这部分留给你…"、"提示：先 if name in phone_book…"）。

**问题**：

```python
elif command == "d":
    name = input("删谁: ")
    # ← 这部分留给你：del phone_book[name] 如果键不存在会 KeyError（坑 2 变体）
    # 提示：先 if name in phone_book: 判断再删，或者用 phone_book.pop(name, "查无此人")
    # if name in phone_book:      ← 上一版的注释尸体
    #     del phone_book[name]
    # else:
    #     print("查无此人")
    if phone_book.pop(name, None) is None:
        ...
```

**分析**：练习的功能已经完成，但"脚手架"没拆：

1. **注释掉的旧代码（注释尸体）**——直接删。git 已经保存了每一版历史，旧版随时能找回；留着只会让读代码的人分不清哪个是有效逻辑。
2. **提示注释**——那是"施工过程"的痕迹，不是代码的一部分。交付前要拆干净。

**教训**：
1. **改了就用新版覆盖，不保留注释尸体**。
2. **交付的代码 = 干净的生产版**：没有提示语、没有草稿、没有注释尸体。
3. 判断标准：把代码交给一个陌生人（或未来的自己），他能只靠代码本身读懂逻辑——**不需要你的解释**。

**最终版**（干净版）：

```python
elif command == "d":
    name = input("删谁: ")
    if phone_book.pop(name, None) is None:
        print("查无此人")
    else:
        print(f"{name} 已删除")
```

完整代码见 [`code/week2/phone_book.py`](../code/week2/phone_book.py)。

---

## English

**Situation**: after finishing the phone book exercise (L2 Day 1), the code still contained two kinds of leftover "construction traces": ① commented-out old code from the previous version; ② two hint comments the tutor had left for the learner ("this part is for you...", "hint: check with `if name in phone_book` first...").

**Analysis**: the feature was done, but the **scaffolding** was not removed:

1. **Commented-out old code (comment corpses)** — delete it. Git already keeps every version of history; you can always look up the old one. Leaving it makes readers unable to tell which logic is live.
2. **Hint comments** — traces of the construction process, not part of the code. Remove them before delivery.

**Lessons**:
1. **When you change code, overwrite with the new version — don't keep comment corpses.**
2. **Delivered code = clean production code**: no hints, no drafts, no commented-out leftovers.
3. Test: hand the code to a stranger (or future you) — they should understand it from the code alone, **without your explanation**.

**Final version**: see the Chinese section above; full code in [`code/week2/phone_book.py`](../code/week2/phone_book.py).

---

## 原对话摘录 / Original conversation excerpt

> 摘自学习者与 AI 助教的真实对话（2026-09-17）。

**学习者贴出的代码（脚手架未拆）**：

```python
    elif command == "d":
        name = input("删谁: ")
        # ← 这部分留给你：del phone_book[name] 如果键不存在会 KeyError（坑 2 变体）
        # 提示：先 if name in phone_book: 判断再删，或者用 phone_book.pop(name, "查无此人")
        if phone_book.pop(name, None) is None:
            print("查无此人")
        else:
            print(f"{name} 已删除")
```

**助教关键点评**：

> "注释掉的旧代码应该直接删掉。理由：git 已经帮你保存了每一版历史，需要旧版随时能翻回来；留在代码里只会越长越乱，让读代码的人分不清哪个是有效逻辑。以后写代码养成习惯：改了就用新版覆盖，不保留注释尸体。"

> "这两行是我给你留的'脚手架'——练习完成就该全部拆掉。交付的代码应该是干净的生产版：没有提示语、没有草稿、没有注释尸体，只有有效的逻辑。"

**学习者的最终处理**：删除全部提示注释与旧代码，保留干净的 `pop` 删除逻辑（见 `code/week2/phone_book.py`）。
