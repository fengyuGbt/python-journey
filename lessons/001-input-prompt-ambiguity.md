# 001 · 输入提示语歧义 / Input prompt ambiguity

## 中文

**场景**：BMI 计算器，提示语写着 `Enter your height in m`。

**我实际做的**：输入了 `177`（我以为是厘米）。

**结果**：`bmi = 80 / (177 ** 2) = 0.00` —— 输出了一个看起来"正常"但完全错误的结果。

**根因**：程序没错，是**提示语没说清单位**。"in m" 对我是模糊的，我按直觉填了 177。程序无法知道用户想要什么，只能按提示语的字面理解。

**教训**：
1. **提示语必须带示例单位**：`Enter your height in meters (e.g. 1.77): `
2. 提示语是"用户体验"的一部分——专业程序员的差异往往体现在这里。
3. 程序逻辑对 ≠ 程序好用。**要让用户猜不到、也猜不错。**

**修复**：

```python
height = float(input("Enter your height in meters (e.g. 1.77): "))
```

---

## English

**Situation**: a BMI calculator whose prompt said `Enter your height in m`.

**What I did**: typed `177` (I was thinking in centimeters).

**Result**: `bmi = 80 / (177 ** 2) = 0.00` — a plausible-looking but completely wrong output.

**Root cause**: the program was fine; the **prompt was ambiguous about the unit**. "in m" was vague to me, so I filled in 177 by intuition.

**Lessons**:
1. Prompts must include an **example unit**: `Enter your height in meters (e.g. 1.77): `
2. The prompt is part of UX — this is where professional developers differ.
3. Correct logic ≠ good program. **Make it impossible for the user to guess wrong.**

**Fix**:

```python
height = float(input("Enter your height in meters (e.g. 1.77): "))
```
