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

Full story of the redo (including the traps hit *during* review, e.g. `is_file()` masking the race, and the stale-file `count=0` event): see [020-week4-trap-list-review](../../lessons/020-week4-trap-list-review.md).
