# Week 3 exercises (L2)

Runnable, final versions of every exercise from L1 Week 3 (files & exceptions).

| File | Day | Notes |
|---|---|---|
| `squares.py` | Day 1 | write 1–100 squares to `squares.txt` (`w` mode, utf-8) |
| `read_squares.py` | Day 1 | read + count lines & sum; one loop, one `with`; see [015-open-without-with](../../lessons/015-open-without-with.md) |
| `list_files.py` | Day 1 | `pathlib.Path` iterate dir, print `.py` names |
| `json_basics.py` | Day 2 | JSON write/read round-trip; `ensure_ascii=False` goes to `dump`, not `open` |
| `ledger_json.py` | Day 2 | ledger v2 with JSON persistence (load on start, save on change); see [016-main-never-called](../../lessons/016-main-never-called.md) |
| `safe_divide.py` | Day 3 | try/except×2/else/finally; error-handling patterns; see [qa: raise or return None](../../qa/raise-or-return-none.md) |

Run any file with Python 3.10+:

```bash
python squares.py
```
