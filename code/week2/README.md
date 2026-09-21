# Week 2 exercises (L2)

Runnable, final versions of every exercise from L2 Week 1 (dict & set).

| File | Day | Notes |
|---|---|---|
| `word_freq.py` | Day 1 | `get()` counting + `lower()` normalization + Top 5 |
| `phone_book.py` | Day 1 | add/query/delete/list menu; see [010-clean-code](../..//lessons/010-clean-code-scaffolding.md) |
| `common_elements.py` | Day 1 | `set(a) & set(b)` one-liner |
| `squares.py` | Day 2 | list comprehension for even squares |
| `passed_students.py` | Day 2 | comprehension filter; see [011-deliberate-practice](../../lessons/011-deliberate-practice-new-tools.md) |
| `zip_sort_students.py` | Day 2 | `dict(zip(...))` + `sorted(key=lambda...)` |
| `calculator_lib.py` | Day 3 | functions + docstrings + `calculate()` dispatch; see [012-int-vs-float](../../lessons/012-int-vs-float.md); typed + ruff-clean (Day 5) |
| `format_amount.py` | Day 3 | `float()` + f-string thousands separator `:,.2f` |
| `args_kwargs_demo.py` | Day 3 | `*args` sum + `**kwargs` query string |
| `counter_closure.py` | Day 4 | `nonlocal` counter; independent closure state |
| `multiplier_factory.py` | Day 4 | closure factory `make_multiplier(n)` |
| `global_analysis.py` | Day 4 | LEGB + `global` analysis; see [013-global-modifies-global](../../lessons/013-global-modifies-global.md) |

Run any file with Python 3.10+:

```bash
python word_freq.py
```
