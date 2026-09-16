# Python 进阶之旅：从零到高级（L1 → L5）

> 一个真实的学习记录：中文学习者从"学了十几年 Python 却很少写代码"到高级程序员的完整过程——**包括每一个错误、每一次修复、每一次与 AI 的问答**。

## 为什么有这个仓库

市面上的 Python 学习项目展示的都是打磨好的完美代码。这个仓库反其道而行：

- ✅ **真实错误记录**：每踩一个坑都写成复盘——为什么发生、下次怎么识别、怎么修。
- ✅ **真实的代码演化**：`code/week1/` 放的是**修复后可运行**的版本；`lessons/` 讲每个 bug 的"出错 → 修复"全过程。
- ✅ **中英双语**：每篇复盘和问答都用两种语言写——因为学代码和学技术英语是同一件事。
- ✅ **完整培训计划**：`docs/training-plan.md` 是完整的 L1–L5 课程（36 周、全职、每天 6–8 小时）。

## 进度

| 等级 | 主题 | 周数 | 状态 |
|---|---|---|---|
| L1 | 语法基础 | 1–4 | 🔄 进行中（第 1 周已完成） |
| L2 | 进阶核心（OOP、生成器、装饰器、pytest、爬虫） | 5–8 | ⏳ |
| L3 | 数据与 Web（Pandas、SQL、FastAPI、部署） | 9–14 | ⏳ |
| L4 | 工程化（测试、Docker、CI/CD、设计模式） | 15–22 | ⏳ |
| L5 | 专家打磨（源码、系统设计、开源） | 23–36 | ⏳ |

## 目录结构

```
python-journey/
├── README.md              # 英文入口
├── README.zh-CN.md        # 中文入口
├── LICENSE                # MIT
├── docs/
│   └── training-plan.md   # L1–L5 完整培训计划
├── code/
│   └── week1/             # 修复后可运行的练习代码（L1 第 1 周）
├── lessons/               # 错误复盘（双语）——本仓库的核心
└── qa/                    # 学习问答（双语）
```

## 错误复盘清单（持续更新）

| # | 复盘 | 学到了什么 |
|---|---|---|
| 001 | [输入提示语歧义](./lessons/001-input-prompt-ambiguity.md) | 提示语没给示例，我把 177 当"身高米数"输入 → BMI 0.00。提示语必须带示例。 |
| 002 | [密码检查的布尔逻辑 bug](./lessons/002-boolean-logic-bug.md) | 复杂的 `not (A and not B)` 藏 bug。改用"数条件个数"。 |
| 003 | [猜中没提示](./lessons/003-no-win-message.md) | `while guess != secret` 猜中时静默退出。成功分支要显式处理。 |
| 004 | [递归滥用](./lessons/004-recursion-overuse.md) | 用递归处理输入循环 → 输错 1000 次就 RecursionError。用 `while`。 |
| 005 | [退出条件缺失](./lessons/005-exit-condition-missing.md) | 按 n 退不出游戏。每个循环都要有验证过的退出路径。 |
| 006 | [过度校验与吞错误](./lessons/006-over-validation.md) | 拒绝标点等于拒绝合法句子；裸 `except` 把 bug 藏起来。 |
| 007 | [输出格式对照清单](./lessons/007-output-format-checklist.md) | `enumerate` 从 0 开始、`:` 和 `.` 的区别——交付前逐项对照需求。 |
| 008 | [提示语泄露答案](./lessons/008-answer-leaked-in-prompt.md) | 提示语把正确答案打出来了。参考代码也要用"用户视角"审查。 |
| 009 | [break 只跳一层](./lessons/009-break-exits-one-loop.md) | `break` 只退出最近一层循环；函数要传退出信号给调用方，用 `return`，不能靠 `break`。 |

## 问答（双语）

- [`while True` 是什么？为什么用它？](./qa/while-true.md)
- [英文单词 `enumerate` 是什么意思？](./qa/enumerate-word.md)

## 如何使用

- **学习者**：先看 `docs/training-plan.md` 规划路线；练习先自己做，再对照 `code/week1/`；等自己踩到同样的坑**之后**再看 `lessons/`——痛过才记得住。
- **贡献者**：欢迎修正错别字、补充解释、新增复盘。保持双语、保持真实。

## 路线图

- [x] L1 第 1 周：环境、语法、控制流、字符串、列表
- [ ] L1 第 2–4 周：字典、函数、文件、异常、模块 → 项目：记账本 CLI
- [ ] L2–L5：按 `docs/training-plan.md` 推进

## 许可证

[MIT](./LICENSE)
