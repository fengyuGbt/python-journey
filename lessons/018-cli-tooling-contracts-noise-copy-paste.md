# 018 · CLI 工具化：契约、噪音与复制残留 / CLI tooling: contracts, noise, copy-paste residue

## 中文

**背景**：第 3 周 Day 5（命令行参数与实用脚本）。用 `argparse` 写两个真工具：`finder.py`（递归搜索文件）和 `rename.py`（批量重命名）。从"交互脚本"升级为"命令行工具"，踩了四个典型坑。

---

**坑 1：方法调用不接返回值（死代码，017 复刻）**

```python
p = Path(args.dir).expanduser()
p.exists()          # ← 调用但没用返回值，这行什么都不是
```

**修复**：判断必须被使用：

```python
if not p.is_dir():
    print(f"{p} is not a directory")
    exit(1)         # 非零退出码 = 告诉调用方出错
```

`is_dir()` 对不存在的路径返回 False，一个条件就够。

**坑 2：参数输入格式与内部数据结构的契约**

`Path.suffix` 返回 `".py"`（带点），但命令行用户按习惯输 `--ext py`（不带点）——`file.suffix == "py"` 永远 False，一个都搜不到。**输入格式和内部结构的约定必须统一**：

```python
ext = args.ext if args.ext.startswith(".") else "." + args.ext
```

**坑 3：判断逻辑写反（== 写成跳过目标）**

```python
for file in p.rglob(f"*{ext}"):
    if file.suffix.lower() == ext.lower():
        continue    # ← 反了！匹配的反而被跳过
```

`rglob(f"*{ext}")` 已只返回匹配文件，二次检查要么删掉、要么写成 `!=`。

**坑 4：复制残留（014 复刻）**

`rename.py` 的 `--prefix` help 写着 `"File extension to search for"`——从 finder.py 复制时没改，词义完全对不上。**复制代码后必须检查名字、help、默认值是否还说得通。**

---

**正向成果：真实工具的三个素质**

1. **排除噪音目录**：递归搜索会翻进 `.venv`、`.git`、`__pycache__`——用路径段集合过滤：

```python
EXCLUDE = {".venv", ".git", "__pycache__", "node_modules"}
if any(part in EXCLUDE for part in file.parts):
    continue
```

2. **显示路径而非裸文件名**：递归下 `wheel.py` 可能出现三次，`print(file.name)` 分不清；用 `file.relative_to(p)` 打印相对路径。

3. **dry-run 安全阀**：批量操作（改名/删除/移动）标配 `--dry-run`，先打印清单不真操作：

```python
parser.add_argument("--dry-run", action="store_true", help="只预览，不实际改名")
```

---

## English

**Context**: Week 3 Day 5 (command-line arguments & practical scripts). Two real tools with `argparse`: `finder.py` (recursive file search) and `rename.py` (batch rename). Four classic traps on the way from "interactive script" to "CLI tool".

---

**Trap 1: method call with unused result (dead code, repeat of 017)**

```python
p.exists()   # called but result never used
```

**Fix**: use the result; `is_dir()` already covers non-existent paths:

```python
if not p.is_dir():
    print(f"{p} is not a directory")
    exit(1)   # non-zero exit code tells the caller it failed
```

**Trap 2: contract between input format and internal structure**

`Path.suffix` returns `".py"` (with dot), but users naturally type `--ext py` (no dot) — `file.suffix == "py"` is never True. **Input format and internal conventions must be unified.**

**Trap 3: inverted logic (== became "skip the targets")**

`rglob(f"*{ext}")` already returns only matching files; the double check either gets deleted or must use `!=`.

**Trap 4: copy-paste residue (repeat of 014)**

`rename.py`'s `--prefix` help still said `"File extension to search for"` — copied from finder.py without updating. **After copying code, check that names, help texts, and defaults still make sense.**

---

**Positive: three qualities of a real tool**

1. **Exclude noise directories**: recursive search crawls into `.venv`, `.git`, `__pycache__`; filter by path segments (`file.parts`).
2. **Print paths, not bare names**: under recursion `wheel.py` may appear three times; use `file.relative_to(p)`.
3. **dry-run safety valve**: batch operations (rename/delete/move) ship with `--dry-run` as standard.

---

## 原对话摘录 / Original conversation excerpt

> 摘自学习者与 AI 助教的真实对话（2026-10-12）。

**学习者**（finder.py 第一版）：

> "p.exists() / for file in p.iterdir(): if file.suffix == args.ext and args.keyword in file.read_text(): print(file.name)"

**助教**：

> "`p.exists()` 又是死代码——调用了，但返回值没被使用。还有 `--ext` 的带点契约坑：Path.suffix 返回 '.py'，但命令行用户会输 'py'。"

**学习者**（改版后 rglob 判断写反）：

> "if file.suffix.lower() == ext.lower(): continue"

**助教**：

> "逻辑反了！rglob(f'*{ext}') 已经只返回匹配的文件，你却又'匹配就跳过'——等于把所有目标文件全部跳过。"

**学习者**（真跑 finder 后发现）：

> "tall.py / show.py / list.py / ...（pip 源码文件）"

**助教**：

> "你的 venv 在 ~/learning/.venv 里，rglob 递归把它底下的 site-packages 全翻了一遍。真实搜索工具必须排除 .venv、.git、__pycache__ 这些噪音目录。"

**学习者**（rename.py 完成后）：

> "Dry run: a.jpg would be renamed to trip_1.jpg / Renamed a.jpg to trip_1.jpg / trip_1.jpg trip_2.jpg trip_3.jpg"

**助教**：

> "dry-run 预览、真跑、ls 确认三件套全齐——Day 5 封板。"
