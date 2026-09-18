# 011 · 刻意练习：用新方法重做旧任务 / Deliberate practice: redo familiar tasks with new tools

## 中文

**场景**：L2 第 2 天练习②（成绩筛选），要求"用推导式"筛出及格学生名字。学习者先用 `for` 循环 + `if/else` 完成了功能。

**学习者第一版**（功能正确，但没按需求）：

```python
for student, score in students.items():
    if score >= 60:
        print(f"{student} passed with a score of {score}.")
    else:
        print(f"{student} failed with a score of {score}.")
```

**问题**：功能跑通了，但**没用今天要练的新工具**（推导式）——练习的验收标准不是"功能完成"，而是"**用了今天的方法**"。

**分析**：能用旧方法完成 ≠ 完成练习。刻意练习的本质，就是**用新方法重做已经会做的事**，直到新方法成为肌肉记忆。骑自行车类比：目的地走路也能到，但今天必须骑车去。

**教训**：
1. **动手前先看"今天要练什么工具"**——练习的验收标准是方法，不是功能。
2. 写完自查：**我用了今天的新工具吗？还是绕回了旧路？**
3. 输出格式也要对照需求（呼应 007 课的清单习惯）。

**修复**（推导式一行版）：

```python
passed = [name for name, score in students.items() if score >= 60]
print(passed)   # ['Alice', 'Carol', 'Dave']
```

---

## English

**Situation**: L2 Day 2 exercise ② (filter passing students) required using a **comprehension**. The learner first solved it with a `for` loop + `if/else`.

**Problem**: it worked, but it didn't use the new tool of the day. The acceptance criterion of an exercise is not "it runs" — it's "**you used today's method**".

**Analysis**: being able to do it the old way ≠ completing the exercise. Deliberate practice is precisely about **redoing familiar tasks with a new tool until the new way becomes muscle memory**. Bicycle analogy: you can walk to the destination, but today you must ride.

**Lessons**:
1. Before coding, check "**what tool am I supposed to practice today?**" — the criterion is the method, not the feature.
2. Self-check after writing: **did I use today's new tool, or did I fall back to the old path?**
3. Output format must also match the requirement (echoes lesson 007's checklist habit).

**Fix**: the one-line comprehension shown in the Chinese section.

---

## 原对话摘录 / Original conversation excerpt

> 摘自学习者与 AI 助教的真实对话（2026-09-18）。

**学习者贴出的第一版（for 循环完成功能）**：

```python
students = {"Alice": 85, "Bob": 58, "Carol": 73, "Dave": 61, "Eve": 44}
for student, score in students.items():
    if score >= 60:
        print(f"{student} passed with a score of {score}.")
    else:
        print(f"{student} failed with a score of {score}.")
```

**助教关键点评**：

> "逻辑完全正确——但今天的练习要求是'用推导式'，你没用推导式。能用旧方法完成 ≠ 完成练习。刻意练习的本质，就是用新方法重做已经会做的事，直到新方法成为肌肉记忆。就像学自行车：目的地走路也能到，但今天必须骑车去。"

**学习者修正版**：

```python
passed = [name for name, score in students.items() if score >= 60]
print("及格的学生有:", passed)
```
