# 024 — 类型注解怎么写：`-> "Library"`、`@classmethod` 到底返回什么、类方法有什么用

> Week 5 · OOP · 2026-11-15
> 类型：概念澄清 + 注解规范（承接 023）

---

## 原始疑问（三连问）

1. 「举个加注释的例子」——给 library_cli 的方法补类型注解，想看具体对照。
2. 「类方法返回的是啥？」——看到 `@classmethod def load(cls, path: str) -> "Library":` 时追问。
3. 「类方法的作用？」——想弄清 `@classmethod` 到底解决什么问题。

---

## 一、注解的写法：5 个真实例子

判断口诀：**参数看传进来是什么，`->` 看 return 出去是什么；没有 return 就写 `None`。**

### 例 1：不返回东西 → `-> None`

改前：
```python
def add_book(self, title, author):
    self.books.append(Book(title, author))
```
改后：
```python
def add_book(self, title: str, author: str) -> None:
```
`append` 只改内部状态，没有 `return` → 返回 `None`。

### 例 2：有返回值 → 跟 return 的类型

改前：
```python
def borrow_book(self, book_name, member_name):
    ...
    return f"{member.name} 成功借阅了《{book.title}》"
```
改后：
```python
def borrow_book(self, book_name: str, member_name: str) -> str:
```
四条 return 分支都返回字符串 → `str`。

⚠️ 自查：所有 return 分支类型必须一致，不能一条返回字符串、另一条返回 `None`。

### 例 3：`__init__` → 一律 `-> None`

```python
def __init__(self, title: str, author: str, is_borrowed: bool = False) -> None:
```

### 例 4：可选参数 → `| None = None`

```python
def __init__(self, name: str, borrowed_books: list[str] | None = None) -> None:
```
默认值 `None` 说明参数可为空 → `list[str] | None`（"字符串列表或 None"）。

### 例 5：classmethod 返回本类实例 → 用字符串写类名

```python
@classmethod
def load(cls, path: str) -> "Library":
```
`return lib`，而 `lib = cls()` → 返回 `Library` 实例。类还没定义完，直接写 `Library` 会 `NameError`，所以用引号（前向引用）。

---

## 二、`load` 返回的到底是什么？

**返回的是 `Library` 类的一个实例对象，不是类本身。**

```python
@classmethod
def load(cls, path: str) -> "Library":
    ...
    lib = cls()      # cls() → 用 Library 造了一个实例
    ...
    return lib       # 返回这个实例
```

`cls` 本身就是类；`cls()` 等价 `Library()`。验证：

```python
lib = Library.load("library.json")
print(type(lib))                  # <class 'models.library.Library'>
print(isinstance(lib, Library))   # True
```

### 为什么注解要加引号

执行到 `def load(...) -> Library:` 时，类体还没执行完，`Library` 这个名字尚未绑定：

```
NameError: name 'Library' is not defined
```

引号让注解变成**前向引用**（forward reference）：先存文字，类型检查时再解析。

### 返回"类本身"的话怎么写

```python
@classmethod
def get_class(cls):
    return cls          # 这才是返回类
```

| 方法体 | 返回什么 | 注解 |
|---|---|---|
| `return cls()` / `lib = cls(); return lib` | 实例 | `-> "Library"` |
| `return cls` | 类 | `-> type` 或 `-> type[Library]` |

Python 3.11+ 也可以用：

```python
from typing import Self

@classmethod
def load(cls, path: str) -> Self:
```

`Self` = "和 `cls` 同类型的实例"，和 `"Library"` 等价，且子类继承后自动正确。

---

## 三、`@classmethod` 的作用（4 条）

### 作用 1：工厂方法 / 替代构造器（最常见）

`__init__` 只能一种构造方式；classmethod 可以加多种"从别的形态创建实例"：

| 项目里的例子 | 从什么创建 | 为什么不放 `__init__` |
|---|---|---|
| `BankAccount.from_balance(cls, amount)` | 从余额数字 | `__init__` 要 owner，工厂只要金额 |
| `Config.from_json(cls, path)` | 从 JSON 文件 | `__init__` 不收文件路径 |
| `Library.load(cls, path)` | 从持久化数据 | 见作用 3 |

### 作用 2：操作"类"本身，不需要实例

`cls` 是类，可以读类属性、调用 `cls()`；实例方法必须先有实例才能调（鸡生蛋）。

```python
Config.DEFAULT          # 类属性，classmethod 里用 cls.DEFAULT 访问
```

### 作用 3：解决"还没有实例"的问题

`load` 是**实例方法不行**的典型场景：实例方法必须 `lib.load(path)`，可 `lib` 还不存在，正是要 load 出来的东西。

```python
lib = Library()          # 先造空实例
lib.load(path)           # 再加载 —— 别扭且容易忘
```

classmethod 直接 `Library.load(path)`，一步到位。

### 作用 4：继承友好

子类调用工厂方法时 `cls` 自动变成子类：

```python
class SpecialLibrary(Library):
    pass

s = SpecialLibrary.load(path)   # cls = SpecialLibrary → s 是子类实例
```

如果工厂方法写成 `return Library()` 硬编码，子类就永远拿不到自己的类型。

### 三者对比

| 类型 | 第一个参数 | 何时可用 | 典型用途 |
|---|---|---|---|
| 实例方法 | `self`（实例） | 必须先有实例 | 操作对象数据（借书、还书） |
| `@classmethod` | `cls`（类） | 有类即可 | 工厂方法、从文件/外部数据创建 |
| `@staticmethod` | 无 | 有类即可 | 与类无关的纯工具函数 |

---

## 四、常见误解：方法里有 `self` 就返回 `None`？

**不是。** `self` 只声明"这是实例方法"，返回什么由 `return` 决定，与 `self` 无关。

同一个类里三个都带 `self` 的方法：

```python
def add_book(self, title: str, author: str) -> None:    # 无 return → None
def borrow_book(self, book_name: str, member_name: str) -> str:   # return 字符串 → str
def list_books(self) -> str:                             # return 字符串 → str
```

判断顺序：

```
有 return 吗？
├─ 没有 → -> None
└─ 有 → 按 return 出去的类型写（字符串 str / 数字 int / 对象 "类名"）
```

`__init__` 返回 `None` 的原因是"没有 return 值 + Python 强制规定"，不是因为它带 `self`。

反例：`def get_balance(self) -> int: return self.balance` —— 有 `self`，返回 `int`。

口诀：**`self` 决定方法归属，`return` 决定注解。**

---

## 五、实证实验（自己跑）

```python
# 实验 1：TypeError——__init__ 不许返回非 None
class A:
    def __init__(self):
        return "x"
A()   # TypeError: __init__() should return None, not 'str'

# 实验 2：前向引用——不加引号会 NameError
class B:
    @classmethod
    def make(cls) -> B:     # NameError
        return cls()

# 实验 3：类方法与继承
class Base:
    @classmethod
    def create(cls):
        return cls()

class Child(Base):
    pass

print(type(Child.create()))   # <class '__main__.Child'>
```

---

## 六、踩坑：类型注解 ≠ 默认值（member.py 实战翻车）

补注解时，把这一行：

```python
def __init__(self, name, borrowed_books=None):
```

改成这样（**错的**）：

```python
def __init__(self, name: str, borrowed_books: list[str] | None) -> None:
```

默认值 `= None` 被弄丢了，`borrowed_books` 从"可省略"变成"必填"。

实锤（虚拟环境里真跑）：

```
TypeError: Member.__init__() missing 1 required positional argument: 'borrowed_books'
```

`Member("张三")` 直接崩。

正确写法：

```python
def __init__(self, name: str, borrowed_books: list[str] | None = None) -> None:
```

### 三个要素缺一不可

| 部分 | 作用 | 丢了会怎样 |
|---|---|---|
| `borrowed_books` | 参数名 | 语法错误 |
| `: list[str] \| None` | 类型注解（给人和类型检查工具看） | 不影响运行 |
| `= None` | 默认值（给调用方） | 参数变必填，调用时 TypeError |

### 教训

**补注解是在原参数后面"加"，不是"替换"。** 参数名、默认值、类型注解三段都要保留，顺序是：

```
参数名 : 类型 = 默认值
```

验收一行：

```bash
python -c "from models.member import Member; Member('张三'); print('ok')"
```

---

## 七、英语 4 词

| 词 | 例句 |
|---|---|
| annotation | Add a type **annotation** to every parameter and return value. |
| forward reference | `"Library"` is a **forward reference** — the class is not defined yet. |
| classmethod | A **classmethod** receives `cls` instead of `self`. |
| factory method | `from_balance` is a **factory method**: another way to create an instance. |

---

## 原对话摘录

**问**：类方法返回的是啥？

**答**：`load` 返回的是 `Library` 的实例对象，不是类本身。`cls()` 造实例，`return lib` 返回它；注解用 `"Library"` 是因为类还没定义完，需要前向引用。

**问**：类方法的作用？

**答**：①工厂方法（`from_balance` / `from_json` / `load`，多种创建入口）；②操作类本身不需要实例；③解决"还没有实例"（load 的鸡生蛋问题）；④继承友好（`cls` 自动指向子类）。

**问**：如果方法里有 `self`，返回类型就是 `None`？

**答**：不是。`self` 只说明这是实例方法；返回什么只看 `return`。`add_book` 没有 return → `None`，`borrow_book` 有 return 字符串 → `str`。`__init__` 返回 `None` 是因为没有 return 值 + Python 强制规定，与 `self` 无关。

**问**（验收时发现）：补注解为什么会把 `Member("张三")` 跑崩？

**答**：改注解时把默认值 `= None` 弄丢了。`borrowed_books: list[str] | None` 只是类型注解，`= None` 才是默认值；少了默认值，参数变必填，`Member("张三")` 就报 `TypeError: missing 1 required positional argument`。

---

## Original conversation excerpt (English)

**Q**: What does a classmethod return?

**A**: `load` returns an **instance** of `Library`, not the class. `cls()` creates the instance and `return lib` returns it. The annotation `"Library"` is a forward reference because the class body is still being defined.

**Q**: What is a classmethod for?

**A**: Four uses: ① factory methods (`from_balance`, `from_json`, `load`) — multiple ways to construct an instance; ② operating on the class itself without an instance; ③ solving the "no instance yet" problem (`load` cannot be an instance method); ④ inheritance-friendly — `cls` automatically points to the subclass.

**Q**: Does a method with `self` always return `None`?

**A**: No. `self` only marks an instance method; the return type depends on the `return` statement. `add_book` has no `return` → `None`; `borrow_book` returns a string → `str`. `__init__` returns `None` because it has no return value and Python enforces that — not because of `self`.
