# Python Journey: From Zero to Senior (L1 → L5)

> A real, honest record of a Chinese learner going from "read about Python for years but rarely wrote code" to a senior-level Python developer — **including every mistake, every fix, and every AI-assisted Q&A along the way.**

## Why this repo exists

Most "learn Python" repos show polished, perfect code. This one does the opposite:

- ✅ **Real mistakes, documented**: each bug I hit is analyzed — why it happened, how to spot it next time, how to fix it.
- ✅ **Real code as it evolved**: `code/week1/` holds the *fixed, runnable* versions; `lessons/` holds the bug → fix story for each one.
- ✅ **Bilingual (中文 / English)**: every lesson and Q&A is written in both languages — because learning code and learning technical English go together.
- ✅ **Full training plan**: `docs/training-plan.md` is the complete L1–L5 curriculum (36 weeks, full-time, ~6–8h/day).

## Status

| Level | Theme | Weeks | Status |
|---|---|---|---|
| L1 | Syntax basics | 1–4 | 🔄 In progress (week 1 done) |
| L2 | Core advanced (OOP, generators, decorators, pytest, scraping) | 5–8 | ⏳ |
| L3 | Data & Web (Pandas, SQL, FastAPI, deployment) | 9–14 | ⏳ |
| L4 | Engineering (testing, Docker, CI/CD, design patterns) | 15–22 | ⏳ |
| L5 | Expert polish (source code, system design, open source) | 23–36 | ⏳ |

## Repository structure

```
python-journey/
├── README.md              # English entry point
├── README.zh-CN.md        # 中文入口
├── LICENSE                # MIT
├── docs/
│   └── training-plan.md   # Full L1–L5 curriculum (中文)
├── code/
│   └── week1/             # Fixed, runnable exercise code (L1 week 1)
├── lessons/               # Bug post-mortems (bilingual) — the heart of this repo
└── qa/                    # Learning Q&A (bilingual)
```

## The lessons (so far)

| # | Lesson | What I learned |
|---|---|---|
| 001 | [Prompt: input prompt ambiguity](./lessons/001-input-prompt-ambiguity.md) | A vague prompt made me type 177 for "height in m" → BMI 0.00. Prompts need examples. |
| 002 | [Boolean-logic bug in password check](./lessons/002-boolean-logic-bug.md) | Complex `not (A and not B)` conditions hide bugs. Count conditions instead. |
| 003 | [No "you win" message](./lessons/003-no-win-message.md) | `while guess != secret` exits silently when you win. Handle the success case explicitly. |
| 004 | [Recursion overuse](./lessons/004-recursion-overuse.md) | Using recursion for input loops → RecursionError after ~1000 bad inputs. Use `while`. |
| 005 | [Exit condition missing](./lessons/005-exit-condition-missing.md) | Pressing "n" didn't quit the game. Every loop needs a verified exit path. |
| 006 | [Over-validation & swallowed errors](./lessons/006-over-validation.md) | Rejecting punctuation rejects valid sentences; bare `except` hides bugs. |
| 007 | [Output format checklist](./lessons/007-output-format-checklist.md) | `enumerate` starts at 0; `:` vs `.` — check requirements item by item before delivery. |
| 008 | [Answer leaked in the prompt](./lessons/008-answer-leaked-in-prompt.md) | The prompt showed the secret answer. Even reference code needs a user-eye review. |

## Q&A (bilingual)

- [What is `while True` and why use it?](./qa/while-true.md)
- [What does the English word `enumerate` mean?](./qa/enumerate-word.md)

## How to use this repo

- **Learners**: read `docs/training-plan.md` for the roadmap; do the exercises yourself first, then compare with `code/week1/`. Read the `lessons/` *after* you hit the same bug — the lesson sticks when you've felt the pain.
- **Contributors**: typo fixes, better explanations, and additional lessons are all welcome. Keep it bilingual, keep it honest.

## Roadmap

- [x] L1 Week 1: environment, syntax, control flow, strings, lists
- [ ] L1 Week 2–4: dictionaries, functions, files, exceptions, modules → project: ledger CLI
- [ ] L2–L5: as planned in `docs/training-plan.md`

## License

[MIT](./LICENSE)
