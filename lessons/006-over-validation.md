# 006 · 过度校验与吞错误 / Over-validation & swallowed errors

## 中文

**场景**：句子统计程序。输入 `Hello, world!` 被拒绝，提示"invalid characters"。

**我的错误代码**：

```python
while not sentence.replace(" ", "").isalpha():
    print("The sentence contains invalid characters.")
    sentence = input("Enter a sentence: ")
```

**现象 1**：`Hello, world!` 里的逗号和感叹号被判为"无效字符"。但**标点不是无效字符，是正常句子的一部分**。

**分析**：`isalpha()` 只认字母。我把"只允许字母"当成了校验规则——这是**过度校验**：挡住了正常输入。

**现象 2**：

```python
except Exception as e:
    print("An error occurred while processing the sentence.")
```

异常被捕获了，但**错误信息 `e` 没打印**。如果程序真出错，我只看到一句笼统的"出错了"，**根本不知道错在哪**——调试的大敌。

**根因**：
1. 校验的哲学搞反了：**挡住真正的坏输入，放过正常输入**。空输入要挡，标点不用挡。
2. 防御过头：这个程序里没有会崩的语句（没有 `int()` 转换），根本不需要 try。**让错误暴露（traceback），才能修。**

**教训**：
1. 校验要"够用"，别过度。写校验前问："什么才是真正的坏输入？"
2. **不要用大 try 包住全部代码**，尤其不要吞掉异常详情。要打印 `e`，或干脆让它抛出来。
3. "到处 try" 不是防御，是**把 bug 藏起来**。

**修复**：

```python
sentence = input("Enter a sentence: ")
while not sentence.strip():
    print("Empty input. Try again.")
    sentence = input("Enter a sentence: ")
# 其余逻辑正常执行，出错就让 traceback 暴露
```

---

## English

**Situation**: the sentence statistics program rejected `Hello, world!` with "invalid characters".

**Symptom 1**: commas and exclamation marks were treated as invalid. But **punctuation is not invalid — it's part of a normal sentence**. `isalpha()` only accepts letters; I over-validated and blocked legitimate input.

**Symptom 2**: `except Exception as e: print("An error occurred...")` caught the error but **never printed `e`** — if something fails, you see a vague message and can't debug.

**Root cause**: got the philosophy backwards — validation should **block genuinely bad input and let normal input pass** (empty input: block; punctuation: let it through). And over-defensive try/except hides bugs.

**Lessons**:
1. Keep validation "enough", not "maximum". Ask: what is *actually* bad input?
2. Don't wrap everything in a big try; if you catch, print the error (`e`) or let it raise.
3. Blanket try/except isn't defense — it's **hiding bugs**.
