# Python Journey — Lessons Index

Real bug post-mortems from the journey, in Chinese and English. Read each one *after* you hit the same bug — the lesson sticks when you've felt the pain.

| # | Lesson | Core lesson |
|---|---|---|
| 001 | [Input prompt ambiguity](./001-input-prompt-ambiguity.md) | Prompts need example units; vague prompts cause wrong input. |
| 002 | [Boolean-logic bug](./002-boolean-logic-bug.md) | Complex `not (A and not B)` hides bugs — count conditions instead. |
| 003 | [No "you win" message](./003-no-win-message.md) | Handle every loop exit path, especially success. |
| 004 | [Recursion overuse](./004-recursion-overuse.md) | Input loops → `while`, not recursion (RecursionError risk). |
| 005 | [Missing exit condition](./005-exit-condition-missing.md) | Every `while True` needs a reachable exit path. |
| 006 | [Over-validation & swallowed errors](./006-over-validation.md) | Block bad input, allow normal input; don't hide errors. |
| 007 | [Output-format checklist](./007-output-format-checklist.md) | Check requirements item by item before delivery. |
| 008 | [Answer leaked in prompt](./008-answer-leaked-in-prompt.md) | Play through your code as a user — even reference code. |
| 009 | [break exits one loop only](./009-break-exits-one-loop.md) | `break` exits one loop level; signal the caller with `return`. |
| 010 | [Remove scaffolding](./010-clean-code-scaffolding.md) | No comment corpses, no leftover hints — ship clean code. |

---

# Python Journey — 错误复盘索引

学习路上真实踩过的坑（中英双语）。建议**先自己踩一遍，再回来读**——痛过才记得住。

| # | 复盘 | 核心教训 |
|---|---|---|
| 001 | [输入提示语歧义](./001-input-prompt-ambiguity.md) | 提示语要带示例单位；模糊提示导致错误输入。 |
| 002 | [布尔逻辑 bug](./002-boolean-logic-bug.md) | 复杂 `not (A and not B)` 藏 bug——改数条件个数。 |
| 003 | [猜中没提示](./003-no-win-message.md) | 每个循环退出路径都要处理，尤其是成功路径。 |
| 004 | [递归滥用](./004-recursion-overuse.md) | 输入循环用 `while`，不用递归（有 RecursionError 风险）。 |
| 005 | [退出条件缺失](./005-exit-condition-missing.md) | 每个 `while True` 都要有可达的退出路径。 |
| 006 | [过度校验与吞错误](./006-over-validation.md) | 挡住真坏输入、放过正常输入；别把错误藏起来。 |
| 007 | [输出格式对照清单](./007-output-format-checklist.md) | 交付前逐项对照需求检查。 |
| 008 | [提示语泄露答案](./008-answer-leaked-in-prompt.md) | 写完当用户跑一遍——参考代码也要审。 |
| 009 | [break 只跳一层](./009-break-exits-one-loop.md) | `break` 只退一层循环；函数传信号给调用方用 `return`。 |
| 010 | [清理脚手架](./010-clean-code-scaffolding.md) | 不留注释尸体、不留提示注释——交付干净代码。 |

---

## 格式约定 / Format

- **001–008**：提炼式复盘（无原对话摘录）。
- **009 起**：每篇末尾附「原对话摘录 / Original conversation excerpt」，保留学习者的原始代码与助教的关键点评，增强现场感。
- All lessons stay bilingual (中文 + English) unless noted.
