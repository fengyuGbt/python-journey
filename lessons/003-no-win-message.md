# 003 · 猜中没提示 / No "you win" message

## 中文

**场景**：猜数字游戏，猜中后程序**静默退出**，没有任何恭喜。

**我的错误代码**：

```python
while your_number != secret and counter < 7:
    counter += 1
    if your_number > secret:
        print("大了")
    else:
        print("小了")
    your_number = int(input("再猜："))
# 循环退出后……什么都没有！
```

**现象**：我输入正确答案 `67` 后，终端没有任何输出，游戏直接结束。

**分析**：`while` 的条件是"**没猜中**才继续"。一旦猜中，条件为假，循环直接退出——但退出后的代码**不存在**。成功路径被设计漏掉了。

**根因**：只设计了"失败/继续"路径，忘了"成功"路径。**循环的退出条件要想清楚：退出时有几种情况？每种都要有输出。**

**教训**：
1. **每个循环都要检查所有退出路径**：正常退出（成功）、异常退出（失败）、中断（break）。
2. 用"先处理成功分支"的方式写：猜中 → 立即 `print` + `break`，不要依赖 while 条件的隐式退出。
3. 这个 bug 我在第 3 天犯过一次，第 5 天写 v2 又犯了一次——**同一个坑掉两次，说明要换策略：写完程序，先当用户跑一遍"成功路径"。**

**修复**：

```python
if guess == secret:
    print(f"恭喜！你猜中了，答案是 {secret}。")
    break
elif guess > secret:
    print("大了")
else:
    print("小了")
```

---

## English

**Situation**: in the number guessing game, winning made the program **exit silently** — no congratulations at all.

**My buggy code**: a `while guess != secret` loop with nothing after it.

**Symptom**: typing the correct answer `67` produced zero output; the game just ended.

**Analysis**: the `while` condition was "keep going **while not guessed**". The moment you guess right, the condition turns false and the loop exits — but there was **no code after the loop**. The success path was simply never designed.

**Root cause**: I designed the "keep trying / failed" path but forgot the "won" path. **Think about every exit path of a loop: normal success, failure, and break — each needs an outcome.**

**Lessons**:
1. Check **every exit path** of a loop; handle success explicitly instead of relying on the while condition's silent exit.
2. I made this mistake on Day 3 and again on Day 5 (v2) — falling into the same pit twice means: **change strategy — after writing a program, play through the "success path" as a user.**
