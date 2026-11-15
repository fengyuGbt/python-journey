# 025 — 历史提问合集：容器、参数、初始化与类方法

> Week 4–5 · 补录于 2026-11-15 · 提问时间 2026-09-18 ～ 2026-10-29

本篇把这些天散落在对话里的提问集中归档。规则照旧：**问题 → 结论 → 代码实证 → 口诀**。
已经单独成篇的（023、024）只在末尾列索引，正文不重复。

本篇所有代码都在本机 WSL 的 Python 3 上实跑过，文中 `text` 块是真实输出，不是手写。

---

## 目录

| # | 提问 | 一句话答案 |
|---|---|---|
| Q1 | `set` 和 `tuple` 的区别只是可变/不可变吗？ | 还有顺序、去重、能否下标、查找方式四类差异 |
| Q2 | `split(maxsplit=3)` 的 3 是什么意思？ | 是"切几刀"，不是"切成几段" |
| Q3 | "带 docstring"是什么意思？ | 函数体第一行的字符串，存进 `__doc__`，不是注释 |
| Q4 | 什么时候用 `is`，什么时候用 `==`？ | `is` 问身份，`==` 问值 |
| Q5 | `Book` 初始化三个属性都必须写进参数吗？ | 外部创建时可能要指定的才进参数，其余内部给默认 |
| Q6 | `Timer` 类为什么没有初始化函数？ | 构造只是"拿秒表"，`with` 进来才"按开始" |
| Q7 | `Config` 里 `cls({...})` 和 `__init__` 什么关系？`**` 是什么？ | `cls(...)` 造实例并调 `__init__`；`**` 把字典拆成键值对 |
| Q8 | `list_books` 里的 print 能不能挪到主函数？ | 能，而且应该：方法返回数据，调用方负责显示 |

---

## Q1 · `set` 和 `tuple` 的区别只是"可变/不可变"吗？

> **你当时的原话**（2026-09-24）
> "Set 和 tuple 它们是不是唯一区别就是 set 是可变的，tuple 是不可变的呀？"

**结论**：可变性只是第一层。四个维度一起看才准确。

| 维度 | `tuple` | `set` |
|---|---|---|
| 可变性 | 不可变，建好不能增删改 | 可变，`add` / `remove` |
| 顺序与下标 | 有序，可以 `t[0]` | 无序，不能 `s[0]` |
| 重复元素 | 保留重复，`(1,2,2,1)` 是 4 个 | 自动去重，`{1,2,2,1}` 只剩 2 个 |
| 元素要求 | 元素可哈希即可（能放 tuple，不能放 list） | 元素必须可哈希 |
| 按值查找 | `in` 要逐个比，O(n) | `in` 走哈希，平均 O(1) |

**代码实证**

```python
t = (1, 2, 2, 1)
s = {1, 2, 2, 1}
print("tuple:", t, "len", len(t))
print("set:", s, "len", len(s))
try:
    hash(([1], [2]))          # tuple 里塞 list
except TypeError as e:
    print("tuple 里放 list -> TypeError:", e)
try:
    s[0]                      # set 取下标
except TypeError as e:
    print("set 下标 -> TypeError:", e)
print("set() =", set(), "| type(set()) =", type(set()).__name__,
      "| type({}) =", type({}).__name__)
```

```text
tuple: (1, 2, 2, 1) len 4
set: {1, 2} len 2
tuple 里放 list -> TypeError: unhashable type: 'list'
set 下标 -> TypeError: 'set' object is not subscriptable
set() = set() | type(set()) = set | type({}) = dict
```

两个附带知识点：

- **`{}` 是空字典，不是空集合**。空集合只能写 `set()`。这个坑一年能踩好几次。
- `tuple` 本身不可变，但"不可变"是浅层的：里面装 list 仍然可以改那个 list。这也是为什么 `tuple` 里塞 list 不报错构造，只是不能拿它当 dict 的键（不可哈希）。

**口诀**：tuple 是排队的号牌——有序、可重复、只读；set 是去重的名单——无序、唯一、按值查得快。

---

## Q2 · `split(maxsplit=3)` 的 3 是什么意思？

> **你当时的原话**（2026-09-25）
> "`Max split` 等于 3 是什么意思？"

**结论**：`maxsplit` 是**最多切几刀**，不是"切成几段"。切 3 刀 → 最多 4 段，剩下的原样留在最后一段。

**代码实证**

```python
print('"a b c d e".split(maxsplit=3) ->', "a b c d e".split(maxsplit=3))
print('"a b c d e".split(maxsplit=0) ->', "a b c d e".split(maxsplit=0))
print('"a b c d e".split() ->', "a b c d e".split())
```

```text
"a b c d e".split(maxsplit=3) -> ['a', 'b', 'c', 'd e']
"a b c d e".split(maxsplit=0) -> ['a b c d e']
"a b c d e".split() -> ['a', 'b', 'c', 'd', 'e']
```

- `maxsplit=3`：切 `a`、`b`、`c` 三刀，`d e` 不再动。
- `maxsplit=0`：一刀不切，整个串作为唯一元素。
- 不写参数（等于 `-1`）：全切。

顺带一句：`split()` 无参时会**顺带丢掉多余空白和换行**；`split(" ")` 不会，连续两个空格会切出一个空字符串。处理用户输入永远用无参版本。

**口诀**：maxsplit 数的是刀，不是段；段数 = 刀数 + 1。

---

## Q3 · "带 docstring"是什么意思？

> **你当时的原话**（2026-09-18）
> "第一个练习说要带这个 docstring 是什么意思？"

**结论**：docstring 是**函数/类/模块体的第一条语句位置上的字符串**。它不是注释，它是对象的一个属性。

| | 注释 `# ...` | docstring `"""..."""` |
|---|---|---|
| 位置 | 任意行 | 必须是 def / class / 模块的第一条语句 |
| 运行时 | 被解释器丢弃 | 存进 `对象.__doc__`，一直可读 |
| 谁能看到 | 只有读源码的人 | `help()`、IDE 悬停、`pydoc` 都能显示 |
| 用途 | 给写代码的人留便签 | 给调用者看的说明书 |

**代码实证**

```python
def area(r):
    """返回圆面积。"""
    return 3.14 * r * r

print("area.__doc__ ->", area.__doc__)
print("area(2) ->", area(2))
```

```text
area.__doc__ -> 返回圆面积。
area(2) -> 12.56
```

写法要点：

- 三引号，第一行写"做什么"，空一行再写细节。
- 放在 `def` 下面第一句；前面先写 `# 注释` 会让它失效（那就变成普通字符串表达式了）。
- 函数有 docstring，IDE 里悬停就有提示；没有，就只能翻源码。

**口诀**：docstring 是写进对象里的说明书，注释是编译完就没了的便签。

---

## Q4 · 什么时候用 `is`，什么时候用 `==`？地址相同，内容不也必然相同吗？

> **你当时的原话**（2026-10-29）
> "帮我温习一下，什么时候用 is，什么时候用那个等号等号？"
> "如果用 is 的话，既然是内存地址相同了，那它的内容不是也应该是相同吗？因为内存地址只有一个呀。"

**结论**：你的推理**前半段是对的，后半段不成立**。

1. `==` 比的是**值**（内容长得一样吗）。
2. `is` 比的是**身份**（是不是同一个对象、同一块内存）。
3. `is` 为 `True` ⇒ 内容必然相同。同一块内存只有一份内容，这不可能是假的。
4. **反过来不成立**：内容相同，完全可以是两块不同的内存。`[1,2,3]` 和 `[1,2,3]` 值一样，但不是同一个列表。

所以判断"值相等"必须用 `==`；`is` 的结果取决于解释器的对象复用细节，不能拿来比值。

**代码实证**

```python
a = [1, 2, 3]
b = [1, 2, 3]
print("a == b:", a == b, "| a is b:", a is b)      # 值同、对象不同

c = a                                              # 不是复制，只是多一个名字
print("c = a -> c is a:", c is a)

x = None
print("x is None:", x is None, "| x == None:", x == None)

s1 = "hello"
s2 = "".join(["hel", "lo"])
print("s1 == s2:", s1 == s2, "| s1 is s2:", s1 is s2)

print("int('257') is int('257'):", int("257") is int("257"))
lit1 = 257
lit2 = 257
print("同一处字面量 257 is 257:", lit1 is lit2)
print("int('128') is int('128'):", int("128") is int("128"))
u1 = "hello world!"
u2 = "hello world!"
print("同字面量长字符串 is:", u1 is u2)
t1 = " ".join(["hello", "world!"])
t2 = " ".join(["hello", "world!"])
print("运行期拼出的长字符串 is:", t1 is t2, "| ==:", t1 == t2)
```

```text
a == b: True | a is b: False
c = a -> c is a: True
x is None: True | x == None: True
s1 == s2: True | s1 is s2: False
int('257') is int('257'): False
同一处字面量 257 is 257: True
int('128') is int('128'): True
同字面量长字符串 is: True
运行期拼出的长字符串 is: False | ==: True
```

逐条读这张输出：

- `a is b` 是 `False`：两个独立列表，两块内存。
- `c = a` 后 `c is a` 是 `True`：赋值只是给同一个对象再加一个名字，没复制。
- `s1` / `s2` 内容一样、`is` 为 `False`：`join` 在运行期造了个新字符串。
- `int("257") is int("257")` 为 `False`，但 `int("128") is int("128")` 为 `True`——**小整数缓存**：`-5 ~ 256` 的整数在解释器启动时就建好了，重复取返回同一个对象；257 不在范围里，每次都新建。
- 同一处写两个 `257` 字面量 `is` 为 `True`——**常量折叠**：编译时同一个 code object 里的相同常量会被合并成一个对象。
- 长字符串字面量 `is` 为 `True`——**字符串驻留**（interning）：源码里的字符串常量会被复用，但运行期拼出来的不会。

这就是关键结论：**`is` 的结果随实现和优化变化，你无法靠它判断值**。别用 `is` 代替 `==`。

**什么时候才该用 `is`**

| 场景 | 写法 |
|---|---|
| 判空值 | `if x is None:` / `if x is not None:` |
| 自定义哨兵 | `_MISSING = object()`，然后 `if v is _MISSING:` |
| 判断"是不是同一个对象" | 缓存命中、单例、模块/类对象比较 |

还有一条规范：**`x == None` 不要写**。它虽然能跑，但 `==` 会去调对象的 `__eq__`，那个方法可以被重写成任何返回值，`None` 的比较结果就不再可靠。`is` 不走 `__eq__`，永远稳。

**口诀**：`==` 问"你俩长得一样吗"，`is` 问"你俩是同一个人吗"。只有问 `None` 和哨兵的时候才问身份。

**英语**：identity（身份）↔ equality（相等）。`is` checks **identity**, `==` checks **equality**.

---

## Q5 · `Book` 初始化三个属性都必须写进参数吗？`is_borrowed` 能不能不放？

> **你当时的原话**（2026-10-29）
> "Book 初始化……里面有图书的 name 和作者，还有一个是否借出，这三个初始化的属性，是不是都要写上去？还是说我可以把，比如说是否借出这个属性，就是不放在这个方法参数里面。"

**结论**：不必"三个都写"。判断标准只有一条——

> **创建对象时，外部有没有可能需要指定它？**
> 需要 → 放参数（给默认值）；永远由内部决定 → 不进参数，在 `__init__` body 里直接赋值。

对 `Book` 来说，`is_borrowed` 应该**留在参数里，带默认 `False`**。理由是 `Library.load()`：从 JSON 恢复时，必须能造出"已经借出去"的书。

**代码实证**

```python
class BookA:                                  # 带参数 + 默认值
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    def __repr__(self):
        return f"Book({self.title!r}, is_borrowed={self.is_borrowed})"

class BookC:                                  # 参数里不放 is_borrowed
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    def __repr__(self):
        return f"Book({self.title!r}, is_borrowed={self.is_borrowed})"

print("A 新建一本新书      ->", BookA("三体", "刘慈欣"))
print("A 从 JSON 还原已借出 ->", BookA("三体", "刘慈欣", True))
try:
    BookC("三体", "刘慈欣", True)
except TypeError as e:
    print("C 想还原已借出      -> TypeError:", e)
print("C 能造出来的只有    ->", BookC("三体", "刘慈欣"))
```

```text
A 新建一本新书      -> Book('三体', is_borrowed=False)
A 从 JSON 还原已借出 -> Book('三体', is_borrowed=True)
C 想还原已借出      -> TypeError: BookC.__init__() takes 3 positional arguments but 4 were given
C 能造出来的只有    -> Book('三体', is_borrowed=False)
```

`BookC` 的毛病不在"少写一个参数"，在于：**对象的状态有 3 个，构造入口只开了 2 个**。于是这个类的对象永远不可能是"已借出"，`load()` 恢复出来的图书馆全部变成全部可借——数据静默出错，比报错更坏。

那什么时候**真的**不该放参数？派生值、算出来的值：

```python
class Order:
    def __init__(self, price: float, qty: int) -> None:
        self.price = price
        self.qty = qty
        self.total = price * qty        # 算出来的 → 不进参数
```

`total` 如果也放进参数，调用方就能传一个和 `price*qty` 不一致的假总数，等于自己给自己开了后门。

**口诀**：**外部要指定 → 进参数带默认；内部算得出 → body 里算。**

---

## Q6 · `Timer` 类为什么没有初始化函数？`__enter__` / `__exit__` 是专门配 `with` 的吗？

> **你当时的原话**（2026-10-27）
> "为什么 Time 类它没有一个那个初始化的那个函数呢？"
> "进入时和退出时是专门和 with 配套使用的吗？"

**结论**：

1. `__init__` **不是必须的**。类里不写，就继承 `object` 那个"什么都不接"的默认版本。
2. `Timer` 是**故意不写**的。因为"开始计时"这件事不该发生在构造时。
3. `__enter__` / `__exit__` 就是 `with` 协议的两个钩子，进入和退出时由 `with` 自动调用。

**为什么计时起点必须放 `__enter__`**

`Timer()` 只是"把秒表从兜里拿出来"；`with Timer()` 才是"按下开始"。如果 `__init__` 里就记 `start`，那么从你 `t = Timer()` 到真正 `with t:` 之间的时间（可能几秒、可能是等用户输入）会被算进耗时里，测出来的数完全不能用。

**代码实证**

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"[Timer] 计时结束，耗时 {self.elapsed*1000:.1f} ms")
        return False

print("1) 构造 Timer()")
t = Timer()
print("   构造后 __dict__ =", t.__dict__, "（空，说明还没有 start）")

print("2) 空闲 0.20s —— 不该被计入")
time.sleep(0.20)

print("3) 进入 with，块内只做 0.10s 的活")
with Timer() as t2:
    time.sleep(0.10)
print("   t2.elapsed =", round(t2.elapsed, 3), "s")
print("   t2.__dict__ =", {k: round(v, 4) for k, v in t2.__dict__.items()})
```

```text
1) 构造 Timer()
   构造后 __dict__ = {} （空，说明还没有 start）
2) 空闲 0.20s —— 不该被计入
3) 进入 with，块内只做 0.10s 的活
[Timer] 计时结束，耗时 100.2 ms
   t2.elapsed = 0.1 s
   t2.__dict__ = {'start': 3019.2002, 'elapsed': 0.1002}
```

注意：中间故意 idle 了 0.20 秒，最终 elapsed 仍然是 **0.100**——因为 `start` 是在 `__enter__` 里才写的。

**`with` 的执行顺序**

```python
with Timer() as t:     # 1. 构造 Timer()  → 2. 调 __enter__() → 3. 返回值绑定给 t
    do_something()     # 4. 执行块
                       # 5. 无论正常还是抛异常，都调 __exit__(exc_type, exc, tb)
```

- `__enter__` 的返回值绑定到 `as` 后面的名字。`return self` 很常见，但不是必须——也可以 `return` 一个数字/句柄。
- `__exit__` 三个参数是异常信息；块内没异常时都是 `None`。
- `__exit__` 返回 `True` 会**吞掉异常**；返回 `False` / `None` 就让异常继续往上抛。写 `return False` 是最安全的老实写法。

所以回答你的问题：**是的，`__enter__` 和 `__exit__` 是专门给 `with` 用的**，方法名是协议规定的，不能改名。

**口诀**：构造不等于开始，`with` 才是开关；秒表出厂不按开始。

---

## Q7 · `Config` 里的 `cls({...})` 和 `__init__` 是什么关系？`**` 双星号又是什么？

> **你当时的原话**（2026-10-27）
> "Config 那个类里面，初始化那一块和最终返回那块之间有什么联系吗？没有这个初始化不行吗？"
> "cls 返回那个字典里面，那个两个星号加上，是什么意思？"

**结论**：

1. `cls(...)` 就是"用这个类造一个实例"，和 `Config(...)` 一样，**必然调用 `__init__`**。
2. 所以 `cls({...})` 是把那个 dict 当作**一个位置参数**交给 `__init__`；`__init__` 的签名必须能接住它（`def __init__(self, cfg)`）。
3. 类里不写 `__init__` 而直接 `cls(参数)`，就是 `TypeError`——默认 `__init__` 一个参数都不收。
4. `**` 是**字典解包**：把 `{"a":1}` 摊成 `a=1` 摆进去。两个 `**` 写在一个字典字面量里，就是**合并**，键冲突时后写的覆盖先写的。

**代码实证**

```python
class Config:
    DEFAULTS = {"debug": False, "level": "info"}

    def __init__(self, cfg):                 # 接住 cls({...}) 传进来的那个 dict
        self.cfg = cfg

    @classmethod
    def build(cls, **kw):                    # 调用方按关键字传参
        return cls({**cls.DEFAULTS, **kw})   # 合并后再交给 __init__

print("Config.build(level='debug').cfg ->", Config.build(level="debug").cfg)
print("dict 解包合并 ->", {**{"a": 1, "b": 2}, **{"b": 9}})

class NoInitConfig:
    DEFAULTS = {"debug": False, "level": "info"}

    @classmethod
    def build(cls, **kw):
        return cls({**cls.DEFAULTS, **kw})   # 没有 __init__ 接

try:
    NoInitConfig.build(level="debug")
except TypeError as e:
    print("类里不写 __init__ -> TypeError:", e)
```

```text
Config.build(level='debug').cfg -> {'debug': False, 'level': 'debug'}
dict 解包合并 -> {'a': 1, 'b': 9}
类里不写 __init__ -> TypeError: NoInitConfig() takes no arguments
```

把这条链拆开看：

```text
Config.build(level="debug")
  → kw = {"level": "debug"}
  → {**DEFAULTS, **kw} = {"debug": False, "level": "debug"}
  → cls({"debug": False, "level": "debug"})     # 造实例
  → Config.__init__(新实例, {"debug": False, "level": "debug"})
  → self.cfg = 那个 dict
  → 返回这个实例
```

三处容易混淆的点：

- `**kw` 在 `def` 里是**收集**：把散着的关键字参数收成一个 dict。
- `**cls.DEFAULTS` 在调用/字面量里是**展开**：把 dict 摊成键值对。
- 同一个符号，两个方向。看它在左边还是右边：`def f(**kw)` 收，`f(**d)` 放。

关于"没有这个初始化行不行"：能行，但必须有个地方接住传参。常见替代是 `__new__` 或者干脆不用类造、直接返回 dict。在 `Library` 这种需要保存状态的场景，`__init__` 是最省事的。

**口诀**：`cls(...)` 造房子，`__init__` 收家具；`**` 是把整箱家具拆开摆进屋里。

**英语**：unpacking（解包）/ packing（打包）。`**kwargs` **collects**, `**d` **spreads**.

---

## Q8 · `list_books` 里的 print，能不能挪到主函数去？

> **你当时的原话**（2026-10-29）
> "就是 list_books 这个方法，你说这里面要加一个 print，我可不可以把它加在主函数去？"

**结论**：**能，而且推荐这么做。** 但要做彻底——选一种模式，别两边都写。

- **模式 A（推荐）**：方法 `return` 字符串（数据层），`main` 里 `print(lib.list_books())`（显示层）。
- **模式 B（不推荐）**：方法内部 `print`，调用方拿不到东西。

**代码实证**

```python
class Lib:
    def __init__(self):
        self.books = ["Book A", "Book B"]

    def list_return(self):
        return "\n".join(self.books)          # 只返回，不打印

    def list_print(self):
        for bk in self.books:
            print("  " + bk)                  # 只打印，不返回

lib = Lib()
r = lib.list_return()
print("list_return() 拿到 ->", repr(r))

out = lib.list_print()
print("list_print() 拿到 ->", repr(out))

print("调用方统一 print 的效果：")
print(r)
```

```text
list_return() 拿到 -> 'Book A\nBook B'
  Book A
  Book B
list_print() 拿到 -> None
调用方统一 print 的效果：
Book A
Book B
```

`list_print()` 返回 `None`——这就是模式 B 的死穴：**调用方什么都拿不到**。想加一句标题、想写进文件、想返回给网页、想写单元测试，全都做不到，因为字符串已经直接喷到终端了。

模式 A 的好处：

- 能测：`assert lib.list_return() == "Book A\nBook B"`。
- 能复用：同一份数据可以打印、写文件、发 HTTP，格式由调用方决定。
- 能换界面：今天 CLI，明天 Web，模型层不用改。

**唯一的坑：别混着写。** 如果方法里 `print` 了，`main` 里又 `print(lib.list_books())`，你会看到一份内容 + 一个 `None`；如果方法里既不 `print` 也不 `return`，`main` 里 `print` 出来是 `None`，看起来像"没数据"。

回到你项目里的实际选型：`borrow_book` / `return_book` 已经 `return` 提示字符串了，`list_books` 就跟着 `return`，`main` 统一 `print`。一套契约，不要两套。

**口诀**：模型层返回数据，界面层负责显示；print 是界面的活，return 是模型的活。

---

## 已单独成文的问题（023 / 024）

下面这些提问当时已经写进专门文档，这里只留索引，方便回查。

| 提问 | 一句话结论 | 文档 |
|---|---|---|
| `__init__` 返回类型为啥是 `None`，不是应该返回对象吗？ | `__init__` 只装修不造对象；造对象的是 `__new__`，类调用才返回实例 | [023](./023-init-returns-none.md) |
| 类方法返回的是啥？`-> "Library"` 为什么要引号？ | 返回 `Library` **实例**（`cls()` 造出来的），不是类；引号是因为类还没定义完 | [024](./024-typing-annotations-classmethod.md) |
| 类方法的作用是什么？ | 工厂方法、操作类本身、解决"还没有实例"的鸡生蛋、继承时 `cls` 自动指向子类 | [024](./024-typing-annotations-classmethod.md) |
| 如果方法里有 `self`，返回类型就是 `None`？ | 无关。`self` 决定方法归属，`return` 决定注解 | [024](./024-typing-annotations-classmethod.md) |
| 举个加注解的例子 | 5 个例子 + 口诀"参数看传进来，`->` 看 return 出去，没 return 写 None" | [024](./024-typing-annotations-classmethod.md) |
| `Load` 为什么是类方法？直接用实例方法不行吗？ | 不行：`load` 要在"还没有实例"时被调用，实例方法进不去这个门 | [024](./024-typing-annotations-classmethod.md) |

---

## 英语词（本篇 8 个）

| 词 | 词性 | 含义 | 项目里的句子 |
|---|---|---|---|
| mutable | adj. | 可变的 | `list` and `set` are **mutable**. |
| immutable | adj. | 不可变的 | `tuple` and `str` are **immutable**. |
| identity | n. | 身份（是不是同一个对象） | `is` compares **identity**. |
| equality | n. | 相等（值是否一样） | `==` compares **equality**. |
| hashable | adj. | 可哈希的（能放进 set / 当 dict 的键） | A `list` is not **hashable**. |
| unpacking | n. | 解包（把容器拆成一个个元素） | `**config` performs **unpacking**. |
| docstring | n. | 文档字符串 | Every public function should have a **docstring**. |
| sentinel | n. | 哨兵值（用来标记"没有/未设置"的特殊对象） | Compare against the **sentinel** with `is`. |

---

## 原对话摘录 / Original conversation excerpt

> **2026-09-25**
> 你：`Max split 等于 3 是什么意思？`

> **2026-10-27**
> 你：`为什么 Time 类它没有一个那个初始化的那个函数呢？`
> 你：`进入时和退出时是专门和 with 配套使用的吗？`

> **2026-10-27**
> 你：`那个就是 cls 返回那个字典里面，那个那对字典是什么意思？就是星号，两个星号加上，对，就是这个是什么意思？`
> 你：`Config 那个类里面那个嗯初始化那一块和最终返回那块之间有什么联系吗？嗯，没有这个初始化不行吗？`

> **2026-10-29**
> 你：`帮我温习一下，什么时候用 is，什么时候用那个等号等号？`
> 你：`如果用 is 的话，既然是内存地址相同了，那它的内容不是也应该是相同吗？因为内存地址只有一个呀。`
> 助教：`你这句话前半句对、后半句错得很关键——is 为 True 时内容必然相同（同一块内存只有一份内容）；但内容相同不代表 is 为 True，两块内存可以装一模一样的东西。`
> 助教：`判断 None 一律用 is None。x == None 能跑，但 == 会调 __eq__，那个方法可以被重写。`

> **2026-10-29**
> 你：`Book 初始化……这三个初始化的属性，是不是都要写上去？还是说我可以把是否借出属性，就是不放在这个方法的参数里面。`
> 助教：`判断标准只有一条：创建对象时，外部有没有可能需要指定它。Book 的 is_borrowed 必须留在参数里，因为 load() 要造出"已借出"的书。`

> **2026-10-29**
> 你：`就是 list_books 这个方法，你说这里面要加一个 print，我可不可以把它加在主函数去？`
> 助教：`可以，但要做彻底：方法 return 字符串，main 里 print。别两边都写。`

---

*本篇所有 `text` 输出均来自 `~/learning/.venv/bin/python` 实跑（验证脚本 `_qa_check.py` ～ `_qa_check4.py`，与本文件同批生成）。*
