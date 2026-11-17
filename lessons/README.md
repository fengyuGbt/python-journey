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
| 011 | [Deliberate practice](./011-deliberate-practice-new-tools.md) | Redo familiar tasks with new tools — the criterion is today's method. |
| 012 | [int() rejects decimals](./012-int-vs-float.md) | Amounts / measurements / division → `float()`, not `int()`. |
| 013 | [global modifies the global](./013-global-modifies-global.md) | `global` is the switch that makes assignment write to the global. |
| 014 | [Copy-pasted index bug](./014-copy-paste-index-bug.md) | Changed the command, forgot the index — count elements before indexing. |
| 015 | [open() without with](./015-open-without-with.md) | Every `open()` needs `with`; open each file once; methods need `()`. |
| 016 | [Defined main(), never called](./016-main-never-called.md) | `def` only registers; end scripts with `if __name__ == "__main__": main()`. |
| 017 | [Dead comparison; except type must match raise](./017-dead-comparison-except-mismatch.md) | A bare comparison does nothing; catch exactly the type that was raised. |
| 018 | [CLI tooling: contracts, noise, copy-paste residue](./018-cli-tooling-contracts-noise-copy-paste.md) | A CLI's output is a contract; strip debug noise and copy residue. |
| 019 | [Weekend project: snapshot race & real-world acceptance](./019-weekend-project-snapshot-race-acceptance.md) | Snapshot the directory before mutating it; accept with real files. |
| 020 | [Week 4 trap-list review (014–019 redone)](./020-week4-trap-list-review.md) | Redo old traps from memory, not by copying the lesson. |
| 021 | [Week 4 comprehensive exercises (20/20)](./021-week4-20-comprehensive-exercises.md) | 20 mixed tasks, each hand-written and run: 20/20. |
| 022 | [L1 acceptance: Ledger v2](./022-ledger-v2.md) | Command CLI + JSON persistence, accepted with ruff clean. |
| 023 | [`__init__` returns `None` — who creates the object?](./023-init-returns-none.md) | `__init__` furnishes the object; `__new__` creates it; the class call returns it. |
| 024 | [Typing annotations & `@classmethod`](./024-typing-annotations-classmethod.md) | `self` decides ownership, `return` decides annotation; `cls()` builds instances. |
| 025 | [Python question collection (Sept–Oct)](./025-python-qa-collection.md) | `is` vs `==`, constructor params, `with` protocol, `**` unpacking, return vs print. |
| 026 | [10 OOP words — spoken recap](./026-oop-english-10-words.md) | Say each term in a full sentence: class-name case, plurals, part of speech. |
| 027 | [Week 6 Day 1: iterators & generators](./027-w6d1-iterators-generators.md) | One-shot, stateful, forward-only: `yield from`, lazy read, sort before `groupby`. |
| 028 | [`yield from` — how it works](./028-yield-from-mechanism.md) | A for-loop plus delegation: sub-generator `return`, any iterable, PEP 380 channels. |
| 029 | [How two iterators “merge” into one list](./029-chain-how-two-iterators-merge.md) | `chain` only orders, `list()` collects; one source active at a time. |
| 030 | [Why the inner `StopIteration` does not break](./030-why-inner-stopiteration-does-not-break.md) | It is swallowed inside `yield from`; only a finished generator signals outward. |
| 031 | [`*args` vs `**kwargs`](./031-args-vs-kwargs.md) | `*` gathers positional into a tuple, `**` gathers keyword into a dict; at the call site they unpack. |
| 032 | [The two `return`s in a decorator](./032-two-returns-in-decorator.md) | Inner returns the data, outer returns the function; drop either and it breaks. |
| 033 | [How to remember and write decorators](./033-how-to-remember-decorators.md) | Five-line skeleton; brackets after `@` decide two layers vs three. |
| 034 | [`functools.wraps` and why multi-layer](./034-wraps-and-why-multiple-layers.md) | Keep name/doc/signature; layers exist because values arrive at different times. |
| 035 | [Why the `@retry` counter must live inside `wrapper`](./035-retry-counter-scope.md) | Per-call state belongs in the per-call layer; loop beats recursive retry. |
| 036 | [When does a call need `try`](./036-when-call-needs-try.md) | Judge by whether the call ultimately propagates an exception, not by decoration. |
| 037 | [Day 2 wrap-up: `@lru_cache` and its tiny `hits`](./037-day2-four-decorators-and-lru-cache.md) | Four decorator drills; hits counts cache returns, not saved calls. |

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
| 011 | [刻意练习](./011-deliberate-practice-new-tools.md) | 用新方法重做旧任务——验收标准是"用了今天的方法"。 |
| 012 | [int() 拒绝小数](./012-int-vs-float.md) | 金额/测量/除法结果 → 用 `float()`，别用 `int()`。 |
| 013 | [global 让赋值修改全局](./013-global-modifies-global.md) | `global` 恰恰是"让函数内赋值改全局"的开关。 |
| 014 | [复制粘贴改了命令没改下标](./014-copy-paste-index-bug.md) | 复制代码要逐行核对下标；取值前先数清有几个元素。 |
| 015 | [第二个 open() 没关](./015-open-without-with.md) | 每个 `open()` 都要 `with`；一个文件只开一次；方法要带 `()`。 |
| 016 | [定义了 main() 却没调用](./016-main-never-called.md) | `def` 只登记；脚本末尾写 `if __name__ == "__main__": main()`。 |
| 017 | [比较表达式当语句用是死代码；except 类型必须匹配 raise](./017-dead-comparison-except-mismatch.md) | 单写一行比较什么都不做；`except` 要抓对 `raise` 的类型。 |
| 018 | [CLI 工具化：契约、噪音与复制残留](./018-cli-tooling-contracts-noise-copy-paste.md) | CLI 的输出就是契约；清掉调试噪音和复制残留。 |
| 019 | [周末项目：快照竞态与真实工具验收](./019-weekend-project-snapshot-race-acceptance.md) | 边遍历边改目录会翻车——先做快照；拿真实目录验收。 |
| 020 | [第 4 周坑清单复盘（014–019 重做）](./020-week4-trap-list-review.md) | 靠记忆重做旧坑，不抄 lesson。 |
| 021 | [20 道综合练习题复盘（20/20）](./021-week4-20-comprehensive-exercises.md) | 20 题每题手写并运行验收，20/20。 |
| 022 | [L1 验收项目：Ledger v2（记账本）](./022-ledger-v2.md) | 命令式 CLI + JSON 持久化，ruff 0 错验收通过。 |
| 023 | [`__init__` 为什么返回 `None`](./023-init-returns-none.md) | `__init__` 只装修，`__new__` 造对象，类调用才返回实例。 |
| 024 | [类型注解与 `@classmethod`](./024-typing-annotations-classmethod.md) | `self` 决定归属，`return` 决定注解；`cls()` 负责造实例。 |
| 025 | [历史提问合集（9–10 月）](./025-python-qa-collection.md) | `is` vs `==`、构造参数、`with` 协议、`**` 解包、返回与打印的分工。 |
| 026 | [10 个 OOP 词英语作业（首次复述批改）](./026-oop-english-10-words.md) | 每个词要能说成整句；类名大写、单复数、词性三处最容易错。 |
| 027 | [第 6 周 Day 1：迭代器与生成器](./027-w6d1-iterators-generators.md) | 一次性、有状态、只能往前；`groupby` 前先排序，每组当场 `list()`。 |
| 028 | [`yield from` 的原理](./028-yield-from-mechanism.md) | 等于 for+delegate：接住子生成器 return、可接任意 iterable、PEP 380 双向通道。 |
| 029 | [两个迭代器怎么“合并”成列表](./029-chain-how-two-iterators-merge.md) | `chain` 只负责顺序，`list()` 才负责收集；同一时刻只有一个源在活动。 |
| 030 | [内层 StopIteration 为什么不会 break](./030-why-inner-stopiteration-does-not-break.md) | 子迭代器的结束在 `yield from` 内部被吞；只有整个生成器结束才对外发信号。 |
| 031 | [`*args` 与 `**kwargs` 的区别](./031-args-vs-kwargs.md) | 单星号收位置参数成 tuple，双星号收关键字成 dict；调用时反过来是拆包。 |
| 032 | [装饰器里的两个 return](./032-two-returns-in-decorator.md) | 里层交回数据、外层交回函数；缺任一个都会坏。 |
| 033 | [装饰器怎么记、怎么写](./033-how-to-remember-decorators.md) | 五行骨架；看 `@` 后有无括号判断两层还是三层。 |
| 034 | [`functools.wraps` 有什么用、为什么包多层](./034-wraps-and-why-multiple-layers.md) | 保住名字/文档/签名；层数取决于参数到达时机，压成一层必崩。 |
| 035 | [@retry 的计数为什么必须放在 wrapper 里](./035-retry-counter-scope.md) | 一次调用的状态要放在每次调用都重跑的那层；循环优于递归。 |
| 036 | [什么时候调用需要 try 接住](./036-when-call-needs-try.md) | 看这次调用最终会不会向外抛异常，不看它有没有被装饰。 |
| 037 | [Day 2 四练收尾：lru_cache 的 hits 为什么这么小](./037-day2-four-decorators-and-lru-cache.md) | 四道装饰器练习汇总；hits 统计命中次数，不是省下的调用数。 |

---

## 格式约定 / Format

- **001–008**：提炼式复盘（无原对话摘录）。
- **009 起**：每篇末尾附「原对话摘录 / Original conversation excerpt」，保留学习者的原始代码与助教的关键点评，增强现场感。
- **023 起**：概念澄清 / 提问归档式——结论前置，配可复现实证（代码 + 真实终端输出）。**025** 为历史提问合集，其余新增提问按编号继续单独成篇。
- All lessons stay bilingual (中文 + English) unless noted.
