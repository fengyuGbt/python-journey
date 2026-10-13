# 019 · 周末项目翻车现场：快照竞态与真实工具验收 / Weekend project: snapshot race & real-world acceptance

## 中文

**背景**：第 3 周周末项目——文件整理工具（自动归档）。`argparse + pathlib + shutil + logging`，按扩展名分类移动到子目录，支持 `--dry-run`、`--log`、冲突重命名、异常保护。六个版本迭代，最后在**真实目录验收**时翻了一次大车，收获两个关键教训。

---

**坑 1（本次最大）：遍历目录的同时修改目录——快照竞态**

`src.iterdir()` 是**惰性迭代器**，循环处理文件时又 `mkdir`（创建分类目录）又 `move`（移动文件）——**你在修改一个正在被遍历的目录**。实测：处理第一个文件后新建的"图片/文档/代码/压缩包"目录被迭代器当成待处理条目，**被 move 进"其他"**；"其他"目录想把自己移进自己时报错，靠 per-file 异常保护才没崩。

dry-run 完美通过、真跑翻车——因为 dry-run 不创建目录、不移动文件，目录没变，竞态不触发。

**修复：遍历和修改分离——先取快照，再处理**：

```python
files = [f for f in src.iterdir() if f.is_file()]   # 快照：遍历结束
for file in files:                                   # 处理：随便 mkdir / move
    ...
```

**坑 2：分类映射不完整——规则漏了 `.css`**

"代码"集合只写了 `{".py", ".js", ".html"}`，`style.css` 按规则正确落入"其他"——**不是 bug，是规则不完整**。分类映射就是业务规则，扩展名覆盖不全就漏。补 `".css"` 后归位。

**坑 3：`FileHandler` 默认追加模式——新旧日志混叠**

`logging.FileHandler(path)` 默认 `mode="a"`（追加），两次运行日志堆在一起，新旧分不清，"可追溯"打折。用 `mode="w"`（每次运行覆盖）或运行开始写一条分隔行。

---

**过程坑（前五版，一笔带过）**：

- `classify` 的 `return "其他"` 缩进进 for 内——每轮循环都返回"其他"，只有第一类正确
- `des` 在函数外算、函数里直接用——作用域错误，NameError
- `logging.error(...)` 里是占位符 `...`——把助教示意抄进代码
- `basicConfig` 同时传 `filename` 和 `handlers`——ValueError，二选一
- `shutil.move` 缩进进 `if target.exists():` 里——冲突才移动，正常文件一个不动

**正向成果**：

1. **快照思维**：遍历与修改分离，是所有"批处理 + 写操作"工具的铁律
2. **验收四步**：dry-run → 真跑 → `ls` 验证 → `cat` 日志验证。dry-run 过了不等于真跑能过
3. **per-file 异常保护**：一个文件失败不影响其余文件
4. **dry-run + 日志 + 冲突重命名**：真实整理工具的安全三件套

---

## English

**Context**: Week 3 weekend project — file organizer (auto-archive). `argparse + pathlib + shutil + logging`, move files into category subdirectories by extension, with `--dry-run`, `--log`, conflict renaming, per-file error protection. Six iterations; acceptance on a real directory caught a big race bug.

---

**Trap 1 (the big one): modifying a directory while iterating it — snapshot race**

`src.iterdir()` is a **lazy iterator**. The loop both `mkdir`s category dirs and `move`s files — **you are modifying the directory you are iterating**. Observed: newly created "图片/文档/代码/压缩包" dirs were treated as pending entries by the iterator and got moved into "其他"; "其他" then failed trying to move itself into itself, saved only by per-file exception handling.

dry-run passed perfectly while the real run failed — because dry-run creates nothing and moves nothing, so the race never triggers.

**Fix: separate traversal from modification — take a snapshot first**:

```python
files = [f for f in src.iterdir() if f.is_file()]   # snapshot: traversal done
for file in files:                                   # processing: mkdir/move freely
```

**Trap 2: incomplete category map — missing `.css`**

The "代码" set only had `{".py", ".js", ".html"}`, so `style.css` correctly fell into "其他" — not a bug, an incomplete rule. The category map IS the business rule; missing extensions leak files.

**Trap 3: `FileHandler` defaults to append — old and new logs mix**

`logging.FileHandler(path)` defaults to `mode="a"`, so two runs pile up and you can't tell runs apart. Use `mode="w"` (overwrite per run) or write a separator line at each run start.

---

**Process traps (first five versions, in brief)**: `return "其他"` indented inside the for loop; `des` used in a function without being a parameter; `logging.error(...)` containing a literal `...` placeholder; `basicConfig` with both `filename` and `handlers`; `shutil.move` indented inside the `if target.exists():` block.

**Positives**: snapshot thinking (separate traversal from modification); four-step acceptance (dry-run → real run → `ls` → `cat log`); per-file exception protection; dry-run + log + conflict renaming as the safety kit of any real organizer tool.

---

## 原对话摘录 / Original conversation excerpt

> 摘自学习者与 AI 助教的真实对话（2026-10-13）。

**学习者**（真跑后贴出日志）：

> "INFO:root:Moved 压缩包 -> messy/其他/压缩包 / INFO:root:Moved 图片 -> messy/其他/图片 / ERROR:root:Error moving file 其他: Cannot move a directory 'messy/其他' into itself"

**助教**：

> "验收的价值就在这一刻体现——dry-run 完美通过，真跑却翻车了。iterdir() 是惰性迭代器，你在修改正在被遍历的目录——新建的'图片'目录被当成待处理条目移进了'其他'。修复：先取快照，再处理。"

**学习者**（修复后重跑）：

> "INFO:root:Moved style.css -> messy/代码/style.css / ls messy/代码: main.py page.html style.css"

**助教**：

> "终验通过——style.css 归位'代码'，14 行日志全干净。周末项目封板。"
