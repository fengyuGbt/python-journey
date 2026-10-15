# Week 4 exercises (L1 · knowledge patch-up)

Runnable, final versions of the Week 4 Day 1 trap-list review — every file hand-fixed and acceptance-run during the 014–019 redo.

| File | Lesson | Notes |
|---|---|---|
| `review-014-copy-paste-index.py` | [014-copy-paste-index-bug](../../lessons/014-copy-paste-index-bug.md) | command parser: `len(parts)` not `parts.__len__`, `parts[1]` not `parts[2]`, empty-input guard |
| `review-015-open-with-with.py` | [015-open-without-with](../../lessons/015-open-without-with.md) | one `with`, one loop — sum & count `squares.txt` together |
| `review-016-main-guard-ensure-ascii.py` | [016-main-never-called](../../lessons/016-main-never-called.md) | `if __name__ == "__main__"` guard; `ensure_ascii=False` in `dump`, `encoding="utf-8"` in `open` |
| `review-017-dead-comparison-except.py` | [017-dead-comparison-except-mismatch](../../lessons/017-dead-comparison-except-mismatch.md) | `else: raise ValueError` (fail fast); `raise ZeroDivisionError` matches `except ZeroDivisionError` |
| `review-018-cli-contract.py` | [018-cli-tooling-contracts-noise-copy-paste](../../lessons/018-cli-tooling-contracts-noise-copy-paste.md) | `is_dir()` check; extension contract normalized once, outside loop; `!=` continue |
| `review-019-snapshot-race.py` | [019-weekend-project-snapshot-race-acceptance](../../lessons/019-weekend-project-snapshot-race-acceptance.md) | snapshot first (`files = [...]`), then mkdir/move — deterministic, race-free |

## Comprehensive exercises (Day 2 · 20/20)

All 20 hand-written and acceptance-run during the 20-question drill (5-skill combination matrix: strings / lists / dicts / functions / files / exceptions).

| File | Notes |
|---|---|
| `exercise-01-reverse-list.py` | reverse two ways: `[::-1]` (new list) vs `.reverse()` (in-place, side effect) |
| `exercise-02-title-words.py` | word title case by hand — `split` + `capitalize` (avoids `str.title()` apostrophe trap) |
| `exercise-03-dict-safe-get.py` | `d.get("c", 0)` — safe read, no KeyError |
| `exercise-04-is-palindrome.py` | normalize (`replace` + `lower`) then compare `s == s[::-1]` |
| `exercise-05-file-sum-numbers.py` | one `with`, one loop; `int()` in try/except skips bad lines |
| `exercise-06-find-duplicates.py` | `Counter.items()` — dedupe first, slice later (no magic `[0:2]`) |
| `exercise-07-count-words.py` | `re.findall(r'\b\w+\b')` — `strip()` only trims ends, regex cleans all |
| `exercise-08-grade-book.py` | grade mapping; note: mutates input dict (side effect) |
| `exercise-09-read-scores.py` | `split(",")` + `len(parts) == 2` guard + int try/except |
| `exercise-10-word-count-file.py` | streaming `for line in f` — line & word counts, O(1) memory |
| `exercise-11-apply-all.py` | fold functions over x: `x = f(x)` |
| `exercise-12-top-n.py` | `sorted(d.items(), key=lambda item: item[1], reverse=True)[:n]` (+ generator alt) |
| `exercise-13-safe-float.py` | `except (ValueError, TypeError)` — `float(None)` raises TypeError |
| `exercise-14-json-storage.py` | `import json` at top; `open` owns encoding, `dump` owns `ensure_ascii` |
| `exercise-15-divisible-numbers.py` | list comprehension: `i % 3 == 0 and i % 5 != 0` (27 items) |
| `exercise-16-merge-counts.py` | `d1.copy()` + `get(k, 0)` — new dict, inputs untouched |
| `exercise-17-dedup-keep-order.py` | seen-set + result list |
| `exercise-18-copy-valid-lines.py` | `line.strip()` non-empty + `line.lstrip()[0].isdigit()` (leading spaces) |
| `exercise-19-char-stats.py` | `stats[ch] = stats.get(ch, 0) + 1` counting pattern |
| `exercise-20-word-analysis.py` | CLI: file → word freq → Top N via `(-count, word)` two-key sort |

Full story of the redo (including the traps hit *during* review, e.g. `is_file()` masking the race, and the stale-file `count=0` event): see [020-week4-trap-list-review](../../lessons/020-week4-trap-list-review.md).

New traps from the 20-exercise drill (magic slice, strip ends-only, TypeError miss, generator vs collection, test data in tools): see [021-week4-20-comprehensive-exercises](../../lessons/021-week4-20-comprehensive-exercises.md).
