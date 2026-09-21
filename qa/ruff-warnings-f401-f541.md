# QA · ruff 常见告警：F401 / F541 是什么？/ What do ruff warnings F401 and F541 mean?

## 中文

**问题**：第一次跑 `ruff check` 报了一堆 F401、F541，它们是什么意思？

**背景**：ruff 是代码检查工具（lint），它按规则编号报告警。F 开头 = pyflakes 规则（逻辑/整洁问题），E/W 开头 = 风格问题（行宽、空行）。

### F401：导入但未使用（imported but unused）

```python
from typing import Optional   # 导入了
...
def choose_difficulty() -> tuple[int, int, int]:   # 但代码里没用 Optional
```

- **为什么是问题**：未使用的导入 = 死代码。浪费一行、误导读者（别人以为代码依赖它）。
- **修法**：删掉；或真正用上它。
- **自动修复**：`ruff check --fix` 直接删。

### F541：f-string 里没有占位符（f-string without any placeholders）

```python
print(f"本局得分：0 分")   # 里面没有 {}，f 前缀多余
```

- **为什么是问题**：`f` 的作用是插值 `{变量}`，没有占位符时它就是普通字符串，写 `f` 让读者去找不存在的变量。
- **修法**：去掉 `f`：`print("本局得分：0 分")`。
- **自动修复**：`ruff check --fix` 直接改。

### 处理流程（通用）

```bash
ruff check <文件>          # 看全部告警
ruff check --fix <文件>    # 自动修安全的（删未用导入、去多余 f、格式类）
ruff check <文件>          # 复查：目标 All checks passed!
ruff format <文件>         # 统一格式（缩进、空行、引号、行宽）
```

**哪些会被 `--fix` 自动修**：未用导入、多余 f 前缀、多余括号、格式类。**哪些不会**：可能改变行为的（如未使用变量要自己判断）、逻辑问题。

### 顺带：`float | None` vs `Optional[float]`

Python 3.10+ 支持新写法（PEP 604）：

```python
def divide(a: float, b: float) -> float | None:   # 新写法，等价于 Optional[float]
```

`float | None` 更简洁，且不需要 `from typing import Optional`。这也是为什么代码里 `Optional` 导入"未使用"——你已经用新语法了，导入就是多余的。

---

## English

**Question**: first `ruff check` run reported F401 and F541 — what do they mean?

**Background**: ruff is a linter that reports warnings by rule code. `F` = pyflakes rules (logic/cleanliness), `E`/`W` = style (line length, blank lines).

### F401: imported but unused

```python
from typing import Optional   # imported
...
def choose_difficulty() -> tuple[int, int, int]:   # never used
```

- **Why it matters**: an unused import is dead code — wastes a line and misleads readers into thinking the code depends on it.
- **Fix**: remove it, or actually use it.
- **Auto-fix**: `ruff check --fix` removes it.

### F541: f-string without any placeholders

```python
print(f"本局得分：0 分")   # no {} inside — the f prefix is pointless
```

- **Why it matters**: `f` exists for interpolating `{variables}`; without placeholders it's a plain string, and the `f` makes readers look for a variable that isn't there.
- **Fix**: drop the `f`.
- **Auto-fix**: `ruff check --fix` handles it.

### General workflow

```bash
ruff check <file>          # see all warnings
ruff check --fix <file>    # auto-fix the safe ones
ruff check <file>          # re-check: target "All checks passed!"
ruff format <file>         # normalize style
```

### Bonus: `float | None` vs `Optional[float]`

Python 3.10+ (PEP 604) allows:

```python
def divide(a: float, b: float) -> float | None:   # equivalent to Optional[float]
```

`float | None` is shorter and needs no `from typing import Optional` — which is exactly why the `Optional` import in the code was flagged as unused.

---

## 原对话摘录 / Original conversation excerpt

> 摘自学习者与 AI 助教的真实对话（2026-09-21）。

**学习者贴出的 ruff 输出**：

> "F401 [*] `typing.Optional` imported but unused → guess_v2.py:9:20 … F541 [*] f-string without any placeholders → guess_v2.py:59:11 … Found 9 errors. [*] 9 fixable with the `--fix` option."

**助教讲解要点**：

> "F401：导入了但没用到 = 死代码，删掉或用上。F541：f-string 里没有占位符，f 前缀多余，去掉。这 9 个错误全都能自动修：`ruff check --fix guess_v2.py`。"

**学习者执行结果**：

> "ruff check --fix guess_v2.py → Found 3 errors (3 fixed, 0 remaining). / ruff check guess_v2.py → All checks passed!"
