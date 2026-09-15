# 008 · 提示语泄露答案 / Answer leaked in the prompt

## 中文

**场景**：猜数字 v2 的参考代码里，提示语写成：

```python
guess = int(input(f"请输入 1-{secret} 的数字："))
```

`secret` 是**答案**。比如答案是 42，提示语就显示"请输入 1-42 的数字"——**玩家直接知道答案了**。

**更有意思的是**：这行代码来自 AI 给的"参考答案"，是学习者（我）在当用户跑了一遍后才发现的。

**根因**：`play_round(secret, max_guesses)` 的参数里没有"范围上限"，提示语想显示范围却拿不到，就顺手用了 `secret`。**参数没给全，导致语义错误。**

**教训**：
1. **写完程序，当用户跑一遍**——这是最便宜的 Code Review。参考代码也要审。
2. 参数设计要想清楚：函数需要什么信息，就要传什么参数。这里是 `(secret, upper, max_guesses)` 三个。
3. "它看起来能跑"不等于"它是对的"——这个 bug 不跑一遍根本发现不了。

**修复**：

```python
def choose_difficulty():
    ...
    return random.randint(1, 50), 50, 10   # (secret, upper, guesses)

def play_round(secret, upper, max_guesses):
    guess = int(input(f"请输入 1-{upper} 的数字："))   # 用 upper，不是 secret
```

---

## English

**Situation**: in the reference code for guessing game v2, the prompt was:

```python
guess = int(input(f"Enter a number (1-{secret}): "))
```

`secret` **is the answer**. If the answer is 42, the prompt shows "Enter a number (1-42)" — **the player knows the answer immediately.**

**The fun part**: this line came from an AI-provided "reference solution", and I (the learner) only caught it by playing through as a user.

**Root cause**: `play_round(secret, max_guesses)` had no "upper bound" parameter, so the prompt couldn't show the real range and borrowed `secret`. **Missing parameters lead to semantic bugs.**

**Lessons**:
1. **Play through your own program as a user** — it's the cheapest code review. Review reference code too.
2. Design parameters deliberately: if a function needs information, pass it. Here: `(secret, upper, max_guesses)`.
3. "It seems to run" ≠ "it's correct" — this bug was invisible until you actually played.
