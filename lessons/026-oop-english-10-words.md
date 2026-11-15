# 026 — 第 5 周英语作业：10 个 OOP 核心词 + 首次复述批改

> Week 5 · 2026-11-15 · 状态：**首轮复述完成，8/10 覆盖，2 个待补**
> 任务来源：第 5 周英语任务——背 10 个面向对象词，每个词能用项目里的句子说出来。

---

## 一、总评

| 项 | 结果 |
|---|---|
| 说到的词 | 8 个（class / object / instance / attribute / method¹ / inherit / override / encapsulation¹） |
| 没说到 | 2 个（polymorphism / constructor） |
| 句子结构对 | 6 句 |
| 需要改的地方 | 类名大小写、单复数一致、`solution` 当动词用、主语选错（把类当对象） |

¹ `method` 与 `encapsulation` 是**推测**：语音转写成了 "measured" 和 "solution to feature"，按上下文判断原意应该是这两个词。如果实际说的是别的，以你为准。

**一句话结论**：词的"意思"基本抓住了，"用英语把话说圆"还差三处——**类名大写、单复数、词性**。

---

## 二、逐条批改

### 1. class ✅

> 你说：`Class, library is a class.`

**可用。** 唯一要修的是类名大写，并补一个冠词：

```text
✅ Library is a class.
✅ The Library class models a collection of books.
```

`class` 是可数名词，说"某某是一个类"要 `a class`；指具体那个类时说 `the Library class`。

---

### 2. object ⚠️ 结构对，主语错

> 你说：`Lip is an object created created from the class.`

三个问题：

1. `Lip` 应该是 `Library`（转写掉了 `rar`）。但更关键的是——**`Library` 是类，不是对象**。这句话等于说"类是对象"，逻辑反了。
2. `created created` 重复，删一个。
3. `the class` 太虚，指明是哪个类。

```text
✅ An object is created from a class.
✅ A Library instance is an object created from the Library class.
```

记忆点：**class 是图纸，object 是按图纸造出来的东西**。`is created from` 是被动语态，主语必须是造出来的那个东西。

---

### 3. instance ✅ 小修

> 你说：`Instance, every book is an instance of book.`

```text
✅ Every book is an instance of the Book class.
```

两处：

- 类名 `Book` **首字母大写**（Python 里类名就是这么写的，读的时候也要按名字读）。
- `of book` → `of the Book class`。说 `an instance of Book` 也能懂，但加 `class` 更清楚，面试时也更专业。

主谓一致这里是对的：`every book` 视为单数，配 `is`。

---

### 4. attribute ⚠️ 单复数不一致

> 你说：`Attribute title and author are attribute.`

```text
✅ Title and author are attributes of a book.
✅ Title and author are attributes of the Book object.
```

`are` 已经告诉你主语是复数（title **and** author 两个），后面的表语必须跟着变复数：`attributes`。这是中国学习者最高频的口语错误之一：**动词记得变，名词忘了变**。

顺带一个搭配：attribute 常跟 `of`，`an attribute of the object`。

---

### 5. method ⚠️（转写为 "measured"）

> 你说：`Our books is measured.`

按上下文推测，你想说的是 `borrow_book` 是个方法。正确说法：

```text
✅ borrow_book() is a method of the Library class.
✅ A method is a function that belongs to a class.
```

两个语法点：

- `method` 是可数名词，单数前面要 `a`：`is a method`。
- 如果真要用 `books` 当主语，动词得用 `are`：`Our books are ...`。`books is` 是主谓不一致。

术语区分（口试常考）：

| 词 | 是什么 | 例子 |
|---|---|---|
| function | 独立函数，不属于类 | `len()`、`print()` |
| method | 定义在类里、第一个参数是 `self` 的函数 | `lib.list_books()` |
| attribute | 类/对象上存的数据 | `book.title` |

---

### 6. inherit ✅ 小修

> 你说：`Dog inherits from animal dog`

```text
✅ The Dog class inherits from the Animal class.
✅ A dog inherits from an animal.        （日常英语版）
```

- 技术句里类名都大写：`Dog` / `Animal`。
- `animal dog` 语序反了——`dog` 是子类，`animal` 是父类，方向是 **Dog ← Animal**。
- 动词 `inherits` 第三人称单数，是对的 ✅。

固定搭配记牢：**`A inherits from B`**（A 继承 B），介词只用 `from`，不用 `of` 或 `by`。

---

### 7. override ⚠️（转写为 "owner is speak"）

> 你说：`dog dog owner is speak`

推测原意：`Dog overrides speak`。正确说法：

```text
✅ The Dog class overrides the speak() method.
✅ Dog overrides Animal.speak().
```

- `override` 是**及物动词**，后面直接跟宾语，中间不能插 `is`：`overrides the method`，不是 `is override`。
- 宾语是"被覆盖的那个方法"，所以要有 `the speak() method` 这一层。
- 被动版：`The speak() method is overridden by the Dog class.`

和 inherit 连起来记：**先 inherit 拿过来，再 override 改掉其中一个**。

---

### 8. polymorphism ❌ 本轮没说

标准句（背这一句就够）：

```text
✅ Polymorphism lets the same method name behave differently in different classes.
✅ Dog.speak() and Cat.speak() share one name but behave differently — that is polymorphism.
```

拆开记：`poly`（多）+ `morph`（形态）+ `-ism`（现象）→ "多种形态"。落到代码上就是**同名方法、不同实现**，调用方不用管传进来的是狗还是猫。

---

### 9. encapsulation ⚠️（`solution` 当动词用了）

> 你说：`I can solution to feature inside the class.`

这句的硬伤是词性：**`solution` 是名词，不能放在 `can` 后面当动词**。动词是 `solve`。情态动词 `can` 后面必须跟动词原形。

要表达"把实现放进类里"（封装），说：

```text
✅ Encapsulation keeps data and methods inside the class.
✅ I can put the implementation inside the class.
✅ The class hides its internals and exposes only methods.
```

`encapsulation` 的定义句值得原样背下来：**`Encapsulation keeps data and methods together inside a class and hides the internals.`**

---

### 10. constructor ❌ 本轮没说

```text
✅ __init__ is the constructor of a class.
✅ The constructor runs automatically when an object is created.
✅ Book("Santi", "Liu") calls the constructor.
```

和 023 那篇连起来：**constructor 负责装修（赋初值），不负责造房子**；造房子的是 `__new__`。英语里也说 `constructor` 或 `initializer`，`__init__` 严格说是 initializer，但口语里都叫 constructor。

---

## 三、跟读版：10 句一次说完

慢速读三遍，每句读完停一拍。句子都是短的，句子结构都套 `X is Y` / `X does Y`。

```text
1. class          Library is a class.
2. object         A book is an object created from the Book class.
3. instance       Every book is an instance of the Book class.
4. attribute      Title and author are attributes of a book.
5. method         borrow_book() is a method of the Library class.
6. inherit        The Dog class inherits from the Animal class.
7. override       The Dog class overrides the speak() method.
8. polymorphism   Polymorphism lets one method name behave differently in different classes.
9. encapsulation  Encapsulation keeps data and methods inside the class.
10. constructor   __init__ is the constructor; it runs when an object is created.
```

---

## 四、发音速查

| 词 | 音标（美） | 重音位置 | 易错点 |
|---|---|---|---|
| class | /klæs/ | 单音节 | 别读成 /klɑːs/ 的英音也行，但要一致 |
| object | /ˈɑːbdʒekt/（名词） | **OB**-ject | 动词重音在后 /əbˈdʒekt/，名词在前 |
| instance | /ˈɪnstəns/ | **IN**-stance | 结尾 /-stəns/，不要读成 /-stens/ |
| attribute | /ˈætrɪbjuːt/（名词） | **AT**-tri-bute | 动词重音在后 /əˈtrɪbjuːt/ |
| method | /ˈmeθəd/ | **ME**-thod | `th` 咬舌尖，别读成 /ˈmesəd/ |
| inherit | /ɪnˈherɪt/ | 在 **-HER-** | 别读成 /ˈɪnherɪt/ |
| override | /ˌoʊvərˈraɪd/ | 在 **-RIDE** | `over` 轻读 |
| polymorphism | /ˌpɑːliˈmɔːrfɪzəm/ | 在 **-MOR-** | 词很长，先拆 poly-morph-ism |
| encapsulation | /ɪnˌkæpsuˈleɪʃn/ | 在 **-LA-** | `capsule` 是"胶囊"，联想记忆 |
| constructor | /kənˈstrʌktər/ | 在 **-STRUC-** | 结尾 /-tər/ 轻读 |

名词重音陷阱值得单独记：`object` 和 `attribute` 都是**名词重音在前、动词重音在后**。你在句子里用的都是名词，重音放前面。

---

## 五、下一轮怎么练

1. 先照着"跟读版"读，**每句读到不打结**再换下一句。
2. 遮住中文，看英文词说句子；再遮住英文，看中文说句子。
3. 重点补两句没说的：`polymorphism` 和 `constructor`，这两句是面试里最常被问的。
4. 复述时留意三个高频错：**类名首字母大写、are + 复数名词、can 后面只能跟动词原形**。

---

## 原对话摘录 / Original conversation excerpt

> **2026-11-15**
> 你：`Class, library is a class. Lip is an object created created from the class. Instance, every book is an instance of book. Attribute title and author are attribute. Our books is measured. Dog inherits from animal dog dog owner is speak. I can solution to feature inside the class.`
>
> 助教批改结论：8/10 覆盖；`solution` 是名词不能当动词；`books is` 主谓不一致；`are attribute` 单复数不一致；object 那句主语把类当成了对象。

---

*对应课程：第 5 周 Day 5 英语任务（10 个 OOP 词）。词义与语法部分已在本会话中逐条实讲，本篇为验收归档。*
