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
| `calc.py` | Day 4 | calculator as a module (pure logic, no input); divide raises `ZeroDivisionError`; see [017-dead-comparison-except-mismatch](../../lessons/017-dead-comparison-except-mismatch.md) |
| `use_calc.py` | Day 4 | imports `calc`, interactive CLI, `if __name__ == "__main__"` guard |
| `word_count_counter.py` | Day 4 | character frequency with `collections.Counter` in one line (`isalpha()` filters all non-letters) |
| `countdown.py` | Day 4 | `date.fromisoformat` countdown with past/today/bad-input handling |

Run any file with Python 3.10+:

```bash
python squares.py
```
