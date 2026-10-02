# 016 · 定义了 main() 却没调用 / Defined main() but never called it

## 中文

**现象**：第 3 周 Day 2（记账本持久化）改造完成后运行：

```
$ python ledger_json.py
$   # ← 没有任何提示，直接退出
```

**原因**：`ledger_json.py` 只**定义了** `main()`，文件末尾没有任何一行**调用**它。Python 加载文件时 `def main():` 只是"登记"了函数，不执行；没有调用语句，程序跑完定义就结束了。

**修复**：文件末尾加模块保护（这是每个脚本的标准收尾）：

```python
if __name__ == "__main__":
    main()
```

**为什么不能直接写 `main()`**：
- `python ledger_json.py` 直接运行时，`__name__ == "__main__"` → 执行 `main()`。
- 未来别的文件 `from ledger_json import save_records` 时，`__name__` 变成 `"ledger_json"` → 保护块不执行，只导入函数，不弹交互。
- 裸 `main()` 会无条件执行——被导入时也会弹交互，违背"可被导入"原则。

**顺带第二个坑**（同天）：`ensure_ascii=False` 是 `json.dump()` 的参数，不是 `open()` 的——放错位置报 `TypeError: open() got an unexpected keyword argument 'ensure_ascii'`。**open() 管编码（`encoding`），dump() 管转义（`ensure_ascii`）**。

**核心原则**：
- 写了 `main()` 就一定要有调用入口：`if __name__ == "__main__": main()`。
- 函数定义 ≠ 函数执行。`def` 只登记，调用才执行。

---

## English

**Symptom**: After refactoring the ledger for persistence (Day 2):

```
$ python ledger_json.py
$   # ← no prompt, exits immediately
```

**Cause**: `ledger_json.py` only **defined** `main()`; the file ended without ever **calling** it. `def main():` just registers the function; with no call statement, the program finishes right after loading definitions.

**Fix**: standard module guard at the end of every script:

```python
if __name__ == "__main__":
    main()
```

**Why not a bare `main()`**:
- Running `python ledger_json.py` sets `__name__ == "__main__"` → `main()` runs.
- When another file does `from ledger_json import save_records`, `__name__` becomes `"ledger_json"` → guard skipped, only functions are imported.
- A bare `main()` always runs — it would pop up the REPL even on import.

**Second bug, same day**: `ensure_ascii=False` belongs to `json.dump()`, not `open()` — wrong position gives `TypeError: open() got an unexpected keyword argument 'ensure_ascii'`. **`open()` owns encoding (`encoding`), `dump()` owns escaping (`ensure_ascii`).**

**Core rules**:
- Every `main()` needs an entry point: `if __name__ == "__main__": main()`.
- Defining a function ≠ running it. `def` registers; a call executes.

---

## 原对话摘录 / Original conversation excerpt

> 摘自学习者与 AI 助教的真实对话（2026-10-02）。

**学习者**：

> "python ledger_json.py —— 没有提示输入，就直接退出了"

**助教**：

> "你定义了 main()，但从来没有调用它。程序加载完 def main():（只是'登记'了这个函数），然后没有任何一行去执行它。修复：文件末尾加 if __name__ == '__main__': main()"

**学习者修复后运行**：

> "Enter command (add/list/total/by/exit): list → Amount: 30.0, Category: 餐饮, Note: 午饭 / Amount: 50.0, Category: 交通, Note: 打车 → total → 80.0" — ✅ 重启后数据仍在，持久化生效
