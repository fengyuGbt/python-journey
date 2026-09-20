# 013 · global 让赋值修改全局变量 / global makes assignment modify the global

## 中文

**场景**：L2 Day 4 练习③（作用域分析题），要求预测三段代码的输出。

**学习者答案**：`20 / 10 / 10`，理由"全局变量没有改动"。

**正确答案**：`20 / 10 / 99`。

**错在哪**：前两段正确（`inner` 按 LEGB 找到外层 `x=20`；全局 `x` 未变仍是 10），但**第三段把 `global` 的作用理解反了**——`change()` 里写了 `global x`，所以 `x = 99` 修改的**正是全局变量**，`change()` 调用后全局 `x` 变成 99。

**核心认识**：`global` 恰恰是"让函数内赋值修改全局变量"的开关，它存在的意义就是这个。没有 `global` 声明时，函数内赋值只会创建新的局部变量（"开新房间"），全局不变；**有了 `global`，99 直接写进大厅的 x**。

**一张表记住三种写法的区别**：

| 写法 | `x = 99` 改的是谁 | 后果 |
|---|---|---|
| 函数内直接赋值（无声明） | 新局部变量 | 全局不变（还可能 UnboundLocalError） |
| `global x` 后赋值 | **全局变量** | 全局被改——这就是 global 的用途 |
| `nonlocal x` 后赋值（嵌套） | 外层函数的 x | 改的是"上一层房间" |

---

## English

**Situation**: L2 Day 4 exercise ③ (scope analysis), predict the output of three print statements.

**Learner's answer**: `20 / 10 / 10`, reason "the global variable wasn't changed."

**Correct answer**: `20 / 10 / 99`.

**What was wrong**: the first two were right (LEGB finds `outer`'s `x=20`; the global `x` is still 10), but the third **reversed the meaning of `global`** — `change()` declares `global x`, so `x = 99` **modifies the global variable itself**; after `change()` the global `x` is 99.

**Core insight**: `global` is precisely the switch that lets an assignment inside a function modify the global. Without it, an assignment creates a new local variable; **with it, the 99 goes straight into the global**.

**Three ways, one table**:

| Writing | What `x = 99` modifies | Result |
|---|---|---|
| plain assignment (no declaration) | a new local variable | global unchanged (may raise UnboundLocalError) |
| after `global x` | **the global variable** | global is modified — that's the point of `global` |
| after `nonlocal x` (nested) | the enclosing function's x | the "room above" is modified |

---

## 原对话摘录 / Original conversation excerpt

> 摘自学习者与 AI 助教的真实对话（2026-09-20）。

**学习者对练习③的分析**：

> "print(outer())：输出20，闭包内层函数记住外层变量；print(x)：输出10，全局变量；print(x)：输出10，全局变量没有改动"

**助教关键点评**：

> "前两个对，第三个错了——而且错得正好戳中 `global` 的核心作用。`global` 恰恰就是'让函数内赋值修改全局变量'的开关，它存在的意义就是这个！如果 `change()` 里没有 `global x`，那 `x = 99` 只会创建一个新的局部变量，全局 x 不动，输出才是 10。但有了 `global`，99 直接写进大厅的 x。运行验证：20 / 10 / 99。"
