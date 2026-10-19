# 022 — L1 验收项目：Ledger v2（记账本）

> Week 4 · Day 6 · 2026-10-19
> 状态：**验收通过** ✅ —— 命令式 CLI + JSON 持久化 + 损坏备份 + ruff 0 错

---

## 项目要求（Training Plan 附录）

| 验收项 | 结果 |
|---|---|
| 连续操作 20 次不崩溃（主循环兜底） | ✅ |
| 数据重启后仍在（增删改落盘 `ledger.json`） | ✅ |
| 代码 ≤ 400 行 | ✅（133 行） |
| 全部函数类型注解 + docstring | ✅ |
| `ruff check` 通过 | ✅（All checks passed） |
| 英文 README（5–8 行） | ✅（8 行） |

## 最终架构

```
命令式 CLI（9 命令：add/list/total/by/delete/edit/month/top/exit）
        │
        ├─ load_records()  启动加载：不存在→建空；损坏→备份 .bak + 提示
        ├─ handle_command() 解析一行命令 → 三件套（len 检查 → try 转换 → 调函数）
        ├─ 纯函数：add/delete/edit → save_records() 每次变更落盘
        └─ while True + try/except 兜底 → 任何错误都继续，不退出
```

记录结构：`{"id": 自增不重用, "date": "YYYY-MM-DD", "amount": 正收负支, "category", "note"}`

---

## 本轮 5 个真实坑（全部运行实锤）

### 坑 1：import 方式 = 调用方式（date 连环三崩）

同一行代码 `datetime.date()` 在不同 import 下是**三种不同的东西**：

| import | `datetime.date` 是什么 | 调用结果 |
|---|---|---|
| `import datetime` | date **类** | `datetime.date(2026,10,19)` ✅ |
| `from datetime import datetime` | date **方法**（method_descriptor） | `datetime.date.today()` → `AttributeError: 'method_descriptor' object has no attribute 'today'` |
| `from datetime import date` | date **类** | `date.today()` ✅ |

**教训**：换 import 写法，调用必须跟着换。三种写法混着抄（网上示例多是 `import datetime`）必崩。

### 坑 2：局部变量遮蔽 import（UnboundLocalError）

```python
from datetime import date

def add(...):
    date = date.today().isoformat()   # 函数内出现 date = 赋值
                                      # → date 变局部变量，右侧 date.today() 找局部
                                      # → 尚未赋值 → UnboundLocalError
```

实锤：`cannot access local variable 'date' where it is not associated with a value`

**规则**：函数内只要对某名字赋值，**整个函数里**该名字都是局部变量，右侧求值在赋值前 → 崩。修法：局部变量改名（`today = date.today()`），别和 import 名撞车。

### 坑 3：函数契约——"内部打印"和"返回列表"二选一

`by()` 改成内部打印（返回 None）后，`top()` 还依赖它的返回值判断：

```python
filtered_entries = by(ledger, category)  # by 返回 None
if not filtered_entries:                  # not None → 恒 True
    print("No entries found...")          # top 永远走"无记录"分支
```

**教训**：改函数签名/返回值 = 改函数契约，**所有调用方都要查**。要么 `by` 返回列表由调用方打印，要么内部打印返回 None——不能混。

### 坑 4：新旧混装（TypeError）

`handle_command` 已是新接口 `add(ledger, amount, category, note)`，被调用的 `add` 还是旧签名 `add(ledger)`：

实锤：`TypeError: add() takes 1 positional argument but 4 were given`

**教训**（016 的又一次现场）：改一半 = 全崩。重构时先列"签名对照表"，函数和调用方成对改。

### 坑 5：ruff 默认规则（4 个报错）

| 规则 | 含义 | 修法 |
|---|---|---|
| `I001` | import 排序 | `ruff check --fix` 自动修 |
| `DTZ011` | `date.today()` 无时区 | `# noqa: DTZ011`（本地日期是有意选择） |
| `SIM102` | 嵌套 if 可合并 | `if a and b:` |
| `BLE001` | 盲捕 `except Exception` | `# noqa: BLE001`（主循环兜底是有意的） |

**noqa 教学**：`# noqa: <CODE>` = "我知道这条规则，这是我刻意的选择"——比绕过检查诚实，代码审计可追溯。

---

## 概念问答（5 组）

**Q1：为什么菜单式必须改成命令式？**
A：规格验收按命令式设计（`delete 2`、`month 2026-09`），且命令式 = 一次输入一个动作，函数不收 input 变纯逻辑，可独立测试；菜单式每操作 3 次 input，无法自动验收。**验收方式驱动架构选择**。

**Q2：try 到底放哪？**
A：贴"会失败的那一行"。命令式下 `float(parts[1])` 在 handle_command → try 在 handle_command；加载时 `json.load` 在 load_records → try 在 load_records。**循环里 try = 出错继续下一轮；加载时 try = 出错返回兜底值**——同一个语法，两种用途。

**Q3：损坏备份为什么先 copy 再提示再返回空？**
A：读失败那一刻损坏文件还完整——**先 `shutil.copy` 保住原始数据**，再提示，再返回空列表继续。之后 save 覆盖 ledger.json 也不丢 .bak。

**Q4：`indent=2` 和 `ensure_ascii=False` 各管什么？**
A：016 坑：`ensure_ascii` 归 `json.dump`（中文不转义），`encoding` 归 `open`（UTF-8），`indent` 让 JSON 换行缩进可读——写盘三件套。

**Q5：变量遮蔽怎么提前发现？**
A：自查"函数内有没有和 import/全局名同名的赋值"。`date = date.today()`、`list = ...`、`input = ...` 都是同一个病。改名 + 跑一次（UnboundLocalError/TypeError 都只会在运行时报）。

---

## 英语 5 词（本轮技术词，造句作业 pending）

| 词 | 例句 |
|---|---|
| persist | Data must **persist** across restarts — that's why every change is saved to `ledger.json`. |
| fallback | The main-loop `try/except` is a **fallback**: any error just prints and continues. |
| shadowing | `date = date.today()` caused **shadowing** — the local variable hid the imported one. |
| contract | Changing a function's return value breaks its **contract** with all callers. |
| refactor | We **refactored** from a menu-driven loop to a command-line interface. |

---

## 归档产物

- `code/ledger-v2/ledger_v2.py`（133 行，最终验收版）
- `code/ledger-v2/README.md`（8 行英文）
- 验收命令：`python3 ledger_v2.py`（WSL: `/home/acer/learning/`）

## 下一环

L1 阶段测验（≥80 分）——验收项目完成后发起。
