# 005 · 退出条件缺失 / Missing exit condition

## 中文

**场景**：猜数字 v2，"再来一局？(y/n)" 里按 **n**（不想玩了），程序却**不退出**，反而回到难度选择。

**我的错误代码**：

```python
def main():
    while True:
        secret, upper, guesses = choose_difficulty()
        play_round(secret, upper, guesses)
        again = input("再来一局？(y/n)：")
        if again == "y":
            secret, upper, guesses = choose_difficulty()   # 又开一局
            play_round(secret, upper, guesses)
        elif again == "n":
            break
```

**现象**：第一局结束按 n → `break` 跳出内层 while → ……等等，实际上 n 是能退出的？**不对**：我的 v1 写法里，`play_round` 内部处理"再来一局"，按 n 只是 `return` 回 main，main 的 `while True` 又从"选难度"开始——用户想退出却永远退不出去。

**分析**：**每个 `while True` 都要问自己：用户怎样才能结束它？** 主循环的退出条件（break）必须存在且可达。

**根因**：把"退出"逻辑埋在函数深处（`play_round` 内部），主循环没有清晰的退出路径。

**教训**：
1. `while True` 本身没错，错的是**没有可到达的退出路径**。
2. 主循环的退出决策应该放在**最外层、最显眼的位置**。
3. 简化：`main()` 里"再来一局？y → 继续循环，n → break"。用 `if input(...).lower() != "y": break` 一行搞定，还能少写重复的选难度代码（DRY）。

**修复**：

```python
def main():
    while True:
        secret, upper, guesses = choose_difficulty()
        play_round(secret, upper, guesses)
        if input("Play again? (y/n): ").lower() != "y":
            break
```

---

## English

**Situation**: in guessing game v2, pressing **n** ("play again?") did not quit — the game went back to the difficulty menu.

**Analysis**: in my v1, the "play again" logic lived inside `play_round`; pressing n just returned to `main`, whose `while True` restarted from "choose difficulty". **The user wanted to exit but there was no reachable exit.**

**Root cause**: the exit decision was buried deep in a function; the main loop had no clear exit path.

**Lessons**:
1. `while True` is not the problem — the problem is **no reachable exit path**.
2. Keep the "continue or quit" decision at the **outermost, most visible level**.
3. Simplify: `if input("Play again? (y/n): ").lower() != "y": break` — one line, no duplicated code (DRY).
