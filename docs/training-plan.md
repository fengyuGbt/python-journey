# Python 高级程序员培训计划（L1 → L5）

> 适用对象：有一定 Python 阅读基础、但动手写代码偏少的学员（"看了十几年，写得少"）。
> 投入强度：全职，每天 6–8 小时，其中动手写代码时间 ≥ 2/3。
> 总周期：约 36 周（8–9 个月），分 5 个能力等级，逐级考核、逐级升级。
> 学习主线：语法基础 → 进阶核心 → 数据与 Web → 工程化 → 专家打磨。
> 变现主线：第 8 周起可接自动化/数据小单 → 第 14 周起接 Web 服务单 → 第 5 阶段冲击海外远程岗位与高客单价单子。
> 语言主线：全程同步技术英语（词汇 → 读文档 → 写英文注释/README → 英文技术沟通）。

---

## 0. 使用说明

### 0.1 学习方法五原则（每天对照检查）

1. **动手 ≥ 2/3**：每学 1 小时理论，必须配 2 小时写代码。看视频/看书不算练习。
2. **费曼输出**：每天用 10 分钟，把当天学的 1 个知识点用"给别人讲"的方式写下来或说出来（中文即可，L3 起用英文）。
3. **项目驱动**：每个周末必须完成一个完整小项目，不追求大，追求"从 0 到 1 独立跑通"。
4. **每日复盘**：每天睡前 10 分钟记录：今天学会了什么 / 卡在哪 / 明天做什么。
5. **英语同步**：每天 30–60 分钟技术英语（具体见第 6 章），不许中断。

### 0.2 升级规则

- 每个等级结束时做"阶段测验 + 项目验收"，两项都通过才能进入下一等级。
- 测验为闭卷手写（可查文档，不可抄代码）；项目验收标准见各等级末尾。
- 卡壳超过 2 天的问题：先自己查官方文档 → 再查 Stack Overflow → 还不行记下来，次日问 AI 或社区。禁止"卡住就刷视频麻痹自己"。

### 0.3 每日时间模板（全职）

| 时段 | 内容 | 时长 |
|---|---|---|
| 上午 | 学新概念 + 跟随练习（每节配代码） | 3h |
| 下午 | 独立练习 / 周末项目 / 接单任务 | 3h |
| 晚上 | 技术英语（读文档、写英文注释、听力） | 1–2h |
| 睡前 | 复盘 + 明日计划 | 10min |

---

## 1. L1 语法基础（第 1–4 周）

**等级目标**：能独立编写 300 行以内的完整脚本；会用 Git 和虚拟环境；代码可被他人运行。
**考核**：L1 测验 ≥ 80 分 + 记账本项目通过验收。

### 1.1 第 1 周：环境与核心语法

#### 第 1 天：环境搭建与第一天程序

- 知识点：Python 3.12+ 安装（勾选 Add to PATH）；VS Code 安装与插件（Python、Pylance）；终端基础（cd/ls/dir、运行 `python xx.py`）；`pip` 与 `venv` 虚拟环境（`python -m venv .venv`、激活、装包、requirements.txt）。
- 动手练习：
  1. 建一个 `learning/` 目录，激活虚拟环境，装 `requests` 并卸载。
  2. 写第一个程序：`print("Hello, Python!")`，用终端运行。
  3. 给变量赋值并打印：名字、年龄、城市。
- 英语任务：背诵并默写 10 个环境词：install、virtual environment、terminal、command、run、error、package、import、file、directory。

#### 第 2 天：变量、数据类型与类型转换

- 知识点：`int` / `float` / `str` / `bool`；`type()`；`input()`；类型转换（`int()`、`str()`、`float()`）；字符串拼接与 `+` 的坑；`None`。
- 动手练习：
  1. 写一个"自我介绍"程序：输入姓名和年龄，输出"我叫 X，明年 Y 岁"。
  2. 写一个 BMI 计算器：输入身高（米）和体重（kg），输出 BMI（体重/身高²），保留 2 位小数。
  3. 故意写一个 `"5" + 3` 看报错，然后用 `int()` 修复。
- 常见坑：`input()` 永远返回字符串；除法的结果是 `float`；`round()` 的银行家舍入。

#### 第 3 天：运算符与控制流

- 知识点：算术/比较/逻辑/赋值运算符；`if / elif / else`；`while`；`for ... in range()`；`break` / `continue` / `pass`；`match` 语句（了解）。
- 动手练习：
  1. 写"成绩等级"程序：0–59 不及格，60–69 及格，70–84 良好，85–100 优秀。
  2. 写"猜数字"游戏：随机数 1–100，循环猜，提示大了/小了，最多 7 次。
  3. 用 `for` 打印 1–100 中能被 3 整除的数。
- 英语任务：列出 10 个条件/循环相关词汇：if、else、while、loop、condition、break、continue、range、compare、nested。

#### 第 4 天：字符串进阶

- 知识点：索引与切片（`s[0]`、`s[-1]`、`s[1:4]`、`s[::-1]`）；常用方法（`upper/lower/strip/split/join/replace/find/count/startswith`）；f-string 格式化（含对齐、小数位、千分位）；`len()`。
- 动手练习：
  1. 写程序：输入一句英文，统计单词数、字母数、首字母大写。
  2. 写"手机号脱敏"：`13812345678` → `138****5678`。
  3. 写"密码强度"检查：长度 ≥ 8、含数字、含字母，输出"强/中/弱"。
- 常见坑：字符串不可变；切片是"左闭右开"；f-string 里大括号转义 `{{}}`。

#### 第 5 天：列表与元组

- 知识点：`list` 增删改查（`append/extend/insert/remove/pop/index/sort/reverse`）；切片；嵌套列表；`in` 判断；列表复制 `[:]` 与 `copy()`；`tuple` 的不可变性与解包（`a, b = 1, 2`）；`enumerate()`。
- 动手练习：
  1. 写"班级成绩统计"：一个列表存 5 个成绩，输出最高、最低、平均、及格人数。
  2. 写"去重排序"：输入一个列表，去重后按降序输出（用 set 和 sorted）。
  3. 用 `enumerate` 打印列表的"序号: 值"。
- 常见坑：`list.sort()` 原地排序返回 None；`sorted()` 返回新列表；`*` 复制嵌套列表的坑（`[[]] * 3`）。

#### 周末项目（第 6–7 天）：猜数字游戏 v2 + 简易计算器

- 要求：
  1. 猜数字 v2：含难度选择（3 个档位）、计分、历史记录打印、非法输入处理（try/except 提前用起来）。
  2. 简易计算器 CLI：支持 `+ - * / %`、连续运算、输入 `q` 退出、除零保护。
- 验收标准：程序能独立运行；代码有函数拆分；至少处理 2 种错误输入。
- 英语任务：用英文给项目写 5 行 README（可以查词典）。

### 1.2 第 2 周：数据结构与函数

#### 第 1 天：字典与集合

- 知识点：`dict` 增删改查（`get/setdefault/keys/values/items/update/pop`）；字典遍历；字典推导式；`set` 运算（`& | - ^`）；何时用 dict 而非 list。
- 动手练习：
  1. 写"词频统计"：给一段英文文本，统计每个单词出现次数，输出 Top 5。
  2. 写"电话簿"：用 dict 存联系人，支持添加、查询、删除、列出全部。
  3. 两个列表找共同元素（用 set 交集）。
- 常见坑：字典键必须可哈希（list 不能当键）；`d[k]` 键不存在会 KeyError，用 `get`；遍历时不能直接删元素（要拷贝或收集键）。

#### 第 2 天：推导式与高级容器操作

- 知识点：列表/字典/集合推导式；带条件的推导式；`zip()`；`*` 与 `**` 解包；`sorted` 的 `key` 参数（`lambda` 初识）。
- 动手练习：
  1. 一行代码生成 1–100 偶数的平方列表。
  2. 用推导式筛选：成绩 ≥ 60 的学生名字（数据：名字-成绩 dict）。
  3. `zip` 合并两个列表成 dict，再用 `sorted(..., key=...)` 按值排序。
- 常见坑：推导式不要嵌套过深（超过 2 层改用循环）；`key=lambda x: x[1]` 的写法要熟。

#### 第 3 天：函数基础

- 知识点：定义与调用；参数：位置参数、关键字参数、默认参数、`*args`、`**kwargs`；返回值（多个返回值本质是元组）；`lambda`；函数文档字符串 `docstring`。
- 动手练习：
  1. 写"计算器函数库"：`add/sub/mul/div` 4 个函数，再写一个 `calculate(op, a, b)` 分发调用。
  2. 写"金额格式化"：输入 1234567.891，输出 `1,234,567.89`（用 f-string 千分位）。
  3. 写一个 `*args` 求和的函数，和 `**kwargs` 拼接查询字符串的函数。
- 常见坑：默认参数别用可变对象（`def f(x, lst=[])` 的坑，L1 就记住）；可变参数顺序 `位置 → *args → 默认 → **kwargs`。

#### 第 4 天：作用域与闭包入门

- 知识点：局部/全局作用域；`global` 与 `nonlocal`；闭包概念（函数内返回函数）；`LEGB` 规则（了解）。
- 动手练习：
  1. 写计数器：用 `nonlocal` 实现"调用一次 +1"的函数。
  2. 写"乘法表工厂"：`make_multiplier(n)` 返回乘 n 的函数，生成 3 个实例测试。
  3. 分析一段含 `global` 的代码，说出输出。
- 常见坑：函数内直接给全局变量赋值会创建新局部变量；循环里创建闭包的经典坑（`i` 延迟绑定）。

#### 第 5 天：代码规范与类型注解入门

- 知识点：PEP8 要点（命名、缩进、空行）；`typing` 基础：`List[int]`、`Dict[str, int]`、`Optional`、`Union`、返回类型 `->`；`docstring` 规范；`ruff` 安装与使用。
- 动手练习：
  1. 把本周写过的 3 个程序加上类型注解，并用 `ruff check` 检查（修复所有告警）。
  2. 给每个函数写 docstring（功能、参数、返回）。
- 英语任务：背 10 个函数相关词：function、argument、parameter、return、default、keyword、scope、local、global、nested。

#### 周末项目：记账本 CLI v1

- 要求：
  1. 命令：`add 金额 分类 备注`、`list`、`total`、`by 分类`、`exit`。
  2. 数据暂时存在内存里（第 3 周升级为文件存储）。
  3. 输入校验：金额必须为数字，分类不能为空；非法输入给友好提示。
  4. 代码拆分成多个函数，每个函数有 docstring 和类型注解。
- 验收标准：所有命令可用；`ruff check` 无错误；函数拆分合理。

### 1.3 第 3 周：文件、异常与模块

#### 第 1 天：文件读写

- 知识点：`open()` 模式（`r/w/a/rb/wb`）；`with` 上下文管理器；`read/readline/readlines`；写入与追加；编码 `utf-8`（Windows 注意 `encoding='utf-8'`）；路径处理 `os.path` / `pathlib` 入门。
- 动手练习：
  1. 写文件：把 1–100 的平方写入 `squares.txt`，每行一个。
  2. 读文件：统计 `squares.txt` 的行数、总和。
  3. 用 `pathlib.Path` 遍历一个目录，打印所有 `.txt` 文件名。
- 常见坑：Windows 下中文文件编码；忘记 `with` 导致句柄泄漏；路径拼接用 `os.path.join` 而非 `+`。

#### 第 2 天：CSV 与 JSON

- 知识点：`csv` 模块读写（`csv.reader/writer/DictReader/DictWriter`）；`json` 模块（`dump/load/dumps/loads`、ensure_ascii=False）；结构化数据思维。
- 动手练习：
  1. 生成 `students.csv`（姓名,城市,成绩 10 条），读取并打印城市分组统计。
  2. 把学生数据转成 JSON 存盘，再读回来打印。
  3. 写"数据备份"函数：dict → JSON 文件；JSON 文件 → dict。
- 常见坑：CSV 中文编码（`encoding='utf-8-sig'` 防 Excel 乱码）；JSON 键必须是字符串。

#### 第 3 天：异常处理

- 知识点：`try / except / else / finally`；捕获特定异常（`ValueError/FileNotFoundError/KeyError`）；`except Exception as e`；`raise` 与自定义异常类；`assert`。
- 动手练习：
  1. 写"健壮除法"：输入两个数，处理除零、非数字、负数三种异常，分别给不同提示。
  2. 给记账本项目加异常处理：文件不存在、JSON 损坏时给友好提示。
  3. 自定义 `MoneyError` 异常，金额为负时抛出。
- 常见坑：空 `except:` 吞掉所有错误（禁止）；`finally` 里别 return 覆盖主逻辑；异常粒度要合适。

#### 第 4 天：模块与包、标准库巡礼

- 知识点：`import` 机制；`if __name__ == "__main__":`；自己写模块和包（`__init__.py`）；标准库常用：`random`、`datetime`、`os`、`sys`、`collections`（`Counter`、`defaultdict`）、`math`。
- 动手练习：
  1. 把自己写的计算器函数封装成 `calc.py` 模块，在另一个文件导入使用。
  2. 用 `collections.Counter` 重写词频统计（一行）。
  3. 用 `datetime` 写"倒计时"程序：输入日期，输出还有多少天。
- 常见坑：文件名与标准库重名（`random.py`）；`import` 路径问题用 `__file__` 排查。

#### 第 5 天：命令行参数与实用脚本

- 知识点：`sys.argv`；`argparse`（`add_argument`、`type`、`help`）；脚本的"工具化"思维：输入 → 处理 → 输出。
- 动手练习：
  1. 用 `argparse` 写"文件搜索工具"：`python finder.py --dir . --ext py --keyword class`。
  2. 写"批量重命名"：`python rename.py --dir photos --prefix trip`，把目录下文件批量改名。
- 英语任务：背 10 个文件词：file、folder、path、read、write、append、encoding、directory、delete、rename。

#### 周末项目：文件整理工具（自动归档）

- 要求：
  1. 扫描指定目录，按扩展名分类（图片/文档/压缩包/代码/其他）移动到对应子目录。
  2. 支持 `--dry-run`（只打印不移动）、`--log`（输出操作日志到文件）。
  3. 用 `argparse` 做命令行；用 `logging` 或 print 记录操作。
  4. 处理异常：目标已存在、无权限、路径不存在。
- 验收标准：能对真实目录安全执行（先 dry-run）；日志可追溯。

### 1.4 第 4 周：综合冲刺与记账本 v2

#### 第 1–3 天：知识补漏与强化练习

- 内容：把前三周"常见坑"重做一遍（每题必须手写通过）；用 2 天完成 20 道综合练习题（见附录 A 样题）。
- 练习重点：字符串处理、列表/dict 操作、函数封装、文件读写、异常处理五种能力的组合题。

#### 第 4–6 天：记账本 v2（L1 验收项目）

- 要求（在 v1 基础上）：
  1. 数据持久化到 `ledger.json`（增删改都落盘）。
  2. 新增命令：`delete 编号`、`edit 编号 新备注`、`month 2026-09`（按月份统计收支）、`top 分类`。
  3. 启动时自动加载文件，损坏时提示并备份为 `.bak`。
  4. 全部函数带类型注解 + docstring；`ruff check` 通过。
  5. 写一个英文 README（5–8 行：项目名、功能、运行方式）。
- 验收标准：连续操作 20 次不崩溃；数据重启后仍在；代码 ≤ 400 行；README 可读。

#### 第 7 天：L1 阶段测验

- 形式：闭卷，60 分钟，25 题（选择/填空/改错/小代码题），覆盖第 1–4 周全部知识点。
- 通过线：80 分。未通过：补考一次（题目换新），补考仍未过则把错题对应知识点重学 2 天。

**L1 完成标志**：测验 ≥ 80 分 + 记账本 v2 验收通过 + 完成 10 次每日英语任务。

---

## 2. L2 进阶核心（第 5–8 周）

**等级目标**：能写出结构良好的模块化代码；掌握 OOP 与进阶语法；会用日志、命令行参数、测试；能独立完成"爬虫 → 清洗 → Excel 导出"的接单级任务。
**考核**：爬虫+数据处理项目通过验收（可交付客户）。

### 2.1 第 5 周：面向对象编程

#### 第 1 天：类与实例

- 知识点：`class` 定义；`__init__` 构造；实例属性与方法；`self` 的含义；`__str__` 与 `__repr__`；创建多个实例。
- 动手练习：
  1. 定义 `BankAccount` 类：`deposit`、`withdraw`、`balance` 属性，禁止透支。
  2. 定义 `Student` 类：姓名/成绩，`get_grade_level()` 方法返回等级。
  3. 把记账本的记录抽象成 `Record` 类（金额、分类、备注、时间）。
- 常见坑：忘记 `self`；属性在方法内赋值才存在（先 `__init__` 初始化全部属性）。

#### 第 2 天：继承与多态

- 知识点：继承语法；`super()`；方法重写；多态（同一方法不同实现）；`isinstance`；`__slots__`（了解）。
- 动手练习：
  1. `Animal` 基类 → `Dog/Cat` 子类，各自实现 `speak()`。
  2. `Shape` 基类 → `Circle/Rectangle`，各自实现 `area()`，写一个函数接收任意 Shape 打印面积（体现多态）。
  3. 用继承重构记账本：`BaseCommand` → `AddCommand/ListCommand/TotalCommand`。
- 常见坑：`super().__init__()` 忘记调用；菱形继承（MRO）了解即可。

#### 第 3 天：魔法方法

- 知识点：`__init__/__str__/__repr__/__eq__/__lt__/__len__/__getitem__/__contains__/__call__/__enter__/__exit__`。
- 动手练习：
  1. 给 `Student` 实现 `__eq__`（按学号相等）和 `__lt__`（按成绩排序）。
  2. 写 `Playlist` 类：实现 `__len__`、`__getitem__`、`__contains__`，让 `playlist[0]`、`len(playlist)`、`"歌" in playlist` 可用。
  3. 写 `Timer` 类：用 `__enter__/__exit__` 实现上下文管理器（with 块执行时长）。
- 常见坑：`__eq__` 会令对象不可哈希（要同时定义 `__hash__`）；魔法方法名不要拼错。

#### 第 4 天：类方法、静态方法与 property

- 知识点：`@classmethod`（操作类本身，如工厂方法）；`@staticmethod`；`@property`（受控属性访问）+ `@x.setter`；封装的意义。
- 动手练习：
  1. 给 `BankAccount` 加 `@classmethod from_balance(cls, amount)` 工厂方法。
  2. 给 `Student` 的 `score` 加 `@property`，设置时自动校验 0–100。
  3. 写一个 `Config` 类：类属性存默认配置，`@classmethod` 从 JSON 加载。
- 常见坑：`@property` 与 `@x.setter` 方法名必须一致；类方法与静态方法的区别要能讲清。

#### 第 5 天：OOP 综合与代码组织

- 知识点：模块化组织（一个类一个文件）；类之间组合关系（has-a）；简单 UML 思维（画类的关系草图）。
- 动手练习：
  1. 设计"图书馆管理系统"模型：`Book`、`Member`、`Library` 三个类，Library 组合 Book/Member，实现借书、还书、查询。
  2. 用 `typing` 给所有方法加类型注解。
- 英语任务：背 10 个 OOP 词：class、object、instance、attribute、method、inherit、override、polymorphism、encapsulation、constructor。

#### 周末项目：图书馆管理系统 CLI

- 要求：完整的类设计 + 文件持久化（JSON）+ 异常处理 + 命令行菜单；至少 3 个类、5 个功能；写英文 README。
- 验收标准：多轮操作不崩溃；重启后数据保留；代码按类拆分文件（`models/` 包）。

### 2.2 第 6 周：进阶语法

#### 第 1 天：迭代器与生成器

- 知识点：可迭代对象 vs 迭代器；`iter()` / `next()`；`yield` 生成器；生成器表达式 `(x for x in ...)`；`itertools` 常用（`count/cycle/chain/groupby/islice`）。
- 动手练习：
  1. 写"无限偶数生成器" `even_numbers()`，用 `next` 取前 10 个。
  2. 写"逐行读取大文件"的生成器函数（不用 `readlines()`，防止内存爆炸）。
  3. 用 `itertools.chain` 合并多个列表，用 `groupby` 分组。
- 常见坑：生成器只能遍历一次；生成器不立即执行（惰性）；`yield` 在函数内任何位置都使其成为生成器函数。

#### 第 2 天：装饰器

- 知识点：装饰器原理（函数即对象）；无参装饰器；`functools.wraps`；带参装饰器（三层嵌套）；多个装饰器叠加顺序；`functools.lru_cache`。
- 动手练习：
  1. 写 `@timer` 装饰器：打印函数执行时间。
  2. 写 `@retry(times=3)` 装饰器：函数抛异常时重试。
  3. 写 `@logged` 装饰器：记录函数名、参数、返回值到日志。
  4. 用 `@lru_cache` 优化斐波那契（对比性能）。
- 常见坑：忘记 `@wraps` 导致函数名丢失；带参装饰器少一层的经典错误；装饰器叠加执行顺序（自下而上）。

#### 第 3 天：上下文管理器

- 知识点：`with` 原理（`__enter__/__exit__`）；`contextlib.contextmanager`；`suppress`；文件、锁、数据库连接的 with 用法。
- 动手练习：
  1. 用 `contextmanager` 写"计时上下文" `with timer():`。
  2. 写"临时改目录"上下文：进入 with 时切目录，退出时切回。
  3. 用 `contextlib.suppress(FileNotFoundError)` 简化文件读取。
- 常见坑：`__exit__` 返回 True 会吞异常（一般返回 False 或 None）；contextmanager 里 `yield` 前后代码分别对应 enter/exit。

#### 第 4 天：正则表达式

- 知识点：`re` 模块：`match/search/findall/finditer/sub/split/compile`；元字符（`.` `^` `$` `*` `+` `?` `{}` `[]` `()` `|` `\d` `\w` `\s`）；贪婪 vs 非贪婪；分组提取。
- 动手练习：
  1. 从文本中提取所有邮箱、电话号码（中国手机号 1[3-9]\d{9}）、URL。
  2. 写"日志解析"：从日志行提取时间、级别、消息。
  3. 用 `re.sub` 清洗文本：去 HTML 标签、去多余空格。
- 常见坑：中文匹配用 `[\u4e00-\u9fa5]`；贪婪匹配用 `.*?` 改非贪婪；`re.match` 只从开头匹配。

#### 第 5 天：标准库深用（1）

- 知识点：`pathlib`（`Path` 全面用法）；`logging`（级别、配置、Formatter、RotatingFileHandler）；`datetime` 进阶（`strptime/strftime/timedelta`）；`argparse` 进阶（子命令）。
- 动手练习：
  1. 给记账本项目换用 `logging` 记录所有操作和错误，输出到 `app.log`，按天轮转。
  2. 用 `pathlib` 重写之前所有路径相关代码。
  3. 写"定时任务提醒"：输入 `2026-10-01 09:00 事件`，计算剩余时间。
- 常见坑：`logging` 默认不输出到文件；`logging` 的 `basicConfig` 只生效一次。

#### 周末项目：日志分析工具（接单级）

- 要求：
  1. 输入一个访问日志文件（nginx/apache 格式样例见附录），输出：请求总数、状态码分布、Top 10 IP、Top 10 路径、每分钟请求数。
  2. 用正则解析；用 `collections.Counter` 统计；支持 `--json` 输出。
  3. 大文件（100MB+）用生成器逐行读。
- 验收标准：能处理真实格式日志；输出清晰；含单元测试 3 个（pytest 初用）。

### 2.3 第 7 周：工程基础

#### 第 1 天：pytest 入门

- 知识点：测试的意义；`test_` 命名；`assert`；`pytest` 运行与报告；`fixture` 基础；`parametrize`；测试目录结构（`tests/`）。
- 动手练习：
  1. 给记账本的核心函数写 10 个测试（正常/边界/异常）。
  2. 用 `@pytest.mark.parametrize` 参数化"除法"函数的测试。
  3. 用 fixture 准备临时数据文件。
- 常见坑：测试相互依赖（禁止）；测试修改了真实数据（用临时目录）；`assert` 后不加括号。

#### 第 2 天：调试技巧

- 知识点：print 调试的局限；`pdb`（`breakpoint()`）基础命令（`n/s/c/p/q`）；异常堆栈阅读；`logging` 分级调试；常见 bug 模式清单。
- 动手练习：
  1. 给一段"故意有 bug"的代码（索引越界、变量名拼错、类型错误、逻辑错误）逐一调试修复。
  2. 练习读 5 个真实堆栈报错，说出问题位置和原因。
- 常见坑：修 bug 先复现 → 定位 → 最小化修复 → 回归测试，不要乱改。

#### 第 3 天：代码规范与类型注解进阶

- 知识点：`typing` 进阶（`Optional/Union/Any/Tuple/Set/Callable/Generator`）；`mypy` 静态检查；`ruff` 全规则；Code Review 自查清单（10 条）。
- 动手练习：
  1. 给 L1 记账本项目跑 `mypy`，修到 0 错误。
  2. 用自查清单 Review 自己上周写的项目代码，列出 5 个改进点。
- 英语任务：背 10 个测试词：test、assert、fixture、parameterized、pass、fail、coverage、mock、suite、report。

#### 第 4–5 天：requests 与 BeautifulSoup（爬虫入门）

- 知识点：HTTP 基础（GET/POST、状态码、headers）；`requests`：`get/post`、`params/headers/timeout`、`Session`、编码；`BeautifulSoup`：解析、`find/find_all`、CSS 选择器 `select`、属性提取；`robots.txt` 与合规意识（重要）；简单限速 `time.sleep`。
- 动手练习：
  1. 抓取一个新闻列表页，提取标题 + 链接 + 发布时间，打印前 10 条。
  2. 用 `Session` 保持请求头，伪装 User-Agent。
  3. 抓取商品价格页面，提取价格文本。
- 合规要点：只抓公开数据、尊重 robots.txt、限速、不抓个人信息、不绕过反爬验证（登录/验证码）、仅供学习。

#### 周末项目：爬虫 + 数据清洗 + Excel 导出（接单级）

- 要求：
  1. 目标站选择公开数据源（如政府公开目录、公开 API），或老师提供的样例站点。
  2. 流程：抓取列表页 → 翻页（≤ 5 页）→ 解析 → 清洗（去重、去空、类型转换）→ 保存 CSV + Excel（`openpyxl` 或 pandas）。
  3. 含限速、超时、失败重试（最多 3 次）、日志。
  4. 写英文 README 和 5 行英文使用说明。
- 验收标准：输出文件可被非技术用户打开使用；代码可复跑；日志清晰。

### 2.4 第 8 周：接单准备与项目收尾

#### 第 1–2 天：接单平台与作品集

- 内容：
  1. 注册 Upwork / Fiverr / 其他海外平台，完善 Profile（英文简介模板见附录 B）。
  2. 把前 8 周的项目整理成 3 个作品：记账本（数据工具）、日志分析（自动化）、爬虫+Excel（数据抓取）。
  3. 每个作品放 GitHub 公开仓库，写英文 README（项目背景、功能截图、技术栈、运行方式）。
- 动手任务：创建 GitHub 账号（如无），学习 `git init/add/commit/push` 完整流程。

#### 第 3–4 天：首单定位与报价练习

- 内容：分析 Upwork/Fiverr 上 Python 初级单（data scraping、Excel automation、data cleaning）的定价区间（常见 $20–100）；写 2 个针对具体 job post 的英文 Proposal（模板见附录 B）；学习平台规则（接单手续费、提现）。
- 动手任务：实际浏览平台，收藏 5 个适合自己的 job post，各写 100 词 Proposal。

#### 第 5 天：L2 测验准备

- 内容：复习 OOP、生成器、装饰器、正则、pytest 五个模块；完成附录 A 的 L2 样题。

#### 周末：L2 阶段测验 + 项目验收

- 测验：闭卷 60 分钟。
- 项目验收：爬虫+数据处理项目按"客户视角"验收：换一台电脑、用 3 分钟看 README 能否运行；数据准确率自查（抽样核对 10 条）。

**L2 完成标志**：测验 ≥ 80 分 + 爬虫项目验收通过 + GitHub 有 3 个公开项目 + 平台 Profile 已建好。

---

## 3. L3 数据与 Web 方向（第 9–14 周）

**等级目标**：能独立完成"取数 → 清洗 → 分析 → 可视化报告"完整闭环；能开发并部署一个可用的 Web API 服务；具备算法与数据结构基础。
**考核**：数据分析报告 + 部署的 API 服务通过验收；客单价目标提升到 $100–500。

### 3.1 第 9 周：NumPy 与 Pandas 入门

#### 第 1–2 天：NumPy 基础

- 知识点：`np.array`；shape/dtype；索引与切片；广播；向量化运算（比循环快 10–100 倍）；常用函数（`sum/mean/std/min/max/unique/where`）；`reshape/ravel`。
- 动手练习：
  1. 生成 10000 个随机数，对比"Python 循环求和"与"np.sum"的速度（用 time 计时）。
  2. 温度数组：华氏转摄氏（向量化）；找出超过 30 度的天数索引。
  3. 二维数组：模拟 30 天 × 4 城市气温，求每天平均、每城市平均。
- 常见坑：`np` 数组元素同类型；切片是视图（改切片会改原数组，用 `.copy()`）。

#### 第 3–4 天：Pandas 核心（Series/DataFrame/读写）

- 知识点：`pd.Series` / `pd.DataFrame`；从 dict/list/CSV 创建；`read_csv/read_excel/to_csv/to_excel`；`head/tail/info/describe`；列选择（`df["col"]`、`df[["a","b"]]`）；行筛选（布尔索引）；新增/删除列。
- 动手练习：
  1. 读取 `students.csv`，输出基本统计信息。
  2. 筛选：成绩 ≥ 80 且城市为广州的学生。
  3. 新增列：总分 = 数学 + 语文 + 英语；按总分排序取前 10。
  4. 把结果导出 Excel（`to_excel`）。
- 常见坑：`df[["a"]]` 返回 DataFrame，`df["a"]` 返回 Series；`read_csv` 中文编码 `encoding='utf-8'`；链式赋值（`df[df.a>1]["b"]=...` 会警告）。

#### 第 5 天 + 周末：Pandas 实战（数据清洗）

- 知识点：缺失值（`isna/dropna/fillna`）；重复值（`duplicated/drop_duplicates`）；类型转换（`astype/to_datetime`）；异常值处理；`apply` 自定义函数。
- 动手练习：清洗一份真实公开数据（如电商订单公开样例）：
  1. 统计缺失率，决定删除还是填充。
  2. 去重、统一日期格式、金额转数值。
  3. 输出清洗前/后的数据质量对比表。
- 验收：清洗流程写成函数，可复跑，附英文注释。

### 3.2 第 10 周：Pandas 进阶与数据分析

#### 第 1–2 天：分组与聚合

- 知识点：`groupby`（`sum/mean/count/agg`）；多列分组；`pivot_table`；`merge/join/concat`；`value_counts`。
- 动手练习：
  1. 订单数据：按城市统计销售额、订单数、客单价。
  2. 按"城市 × 月份"透视表。
  3. 两张表（订单、商品）用 `merge` 关联，分析商品类目销售占比。
- 常见坑：`groupby` 后是 DataFrameGroupBy 对象；`agg` 用字典指定多列多函数；`merge` 注意 `on` 与 `how`。

#### 第 3 天：时间序列

- 知识点：`to_datetime`；`set_index`；`resample`（日→周/月）；`shift/diff`；滚动窗口 `rolling`。
- 动手练习：
  1. 股票或销售日数据：转月度汇总、计算 7 日移动平均。
  2. 计算环比/同比变化。
- 常见坑：时间索引需排序；`resample` 的规则字符串（`W`/`M`/`D`/`h`）要记。

#### 第 4 天：数据可视化

- 知识点：`matplotlib` 基础（`plot/scatter/bar/hist`、标题、标签、图例、保存图片）；`seaborn` 常用（`histplot/boxplot/heatmap/pairplot`）；图表规范（标题、单位、来源）。
- 动手练习：
  1. 用数据做 4 张图：销售趋势折线、城市销量柱状、价格分布直方、两变量相关散点。
  2. 用 `heatmap` 展示城市 × 月份的销量热力图。
- 常见坑：中文显示（`plt.rcParams` 设置字体）；保存用 `bbox_inches='tight'`。

#### 第 5 天 + 周末：数据分析完整项目（L3 项目 A）

- 项目：**"XX 城市二手房/商品销售数据分析报告"**（数据用公开数据集）：
  1. 数据清洗 → 探索分析（10+ 统计量、8 张图）→ 3 个业务结论 → 输出 `report.md` + 图表目录。
  2. 要求：分析过程可复现（一个 `main.py` 跑完全流程）、有英文 README。
- 验收标准：业务结论有数据支撑；图表清晰；报告结构完整（背景/数据/分析/结论）。

### 3.3 第 11 周：SQL 与数据库

#### 第 1–2 天：SQL 基础（SQLite）

- 知识点：数据库概念；`CREATE TABLE`；`INSERT/UPDATE/DELETE`；`SELECT`（`WHERE/ORDER BY/LIMIT`）；聚合（`COUNT/SUM/AVG/GROUP BY/HAVING`）；`JOIN`（INNER/LEFT）；索引概念。
- 动手练习：用 `sqlite3` 或 DB Browser：
  1. 建订单库（用户表、订单表、商品表），插入样例数据。
  2. 完成 10 道查询题（含 JOIN、GROUP BY、HAVING）。
- 常见坑：`GROUP BY` 后 SELECT 的列要聚合或分组；字符串用单引号；`LIMIT` 语法与 MySQL 相同。

#### 第 3 天：Python 操作数据库

- 知识点：`sqlite3` 模块（`connect/execute/commit`、参数化查询防注入）；`pandas.read_sql`；事务概念。
- 动手练习：
  1. 用 Python 建表、批量插入 1 万条、查询统计。
  2. 参数化查询：写一个按城市查询的函数，演示 SQL 注入风险与防御（`?` 占位）。
- 常见坑：忘记 `commit()`；用 f-string 拼 SQL（严重安全问题，禁止）；连接用完要 `close`。

#### 第 4–5 天：PostgreSQL 与 ORM 入门

- 知识点：安装 PostgreSQL（本地或用云免费实例）；`psycopg2`/`SQLAlchemy` 连接；与 SQLite 差异（类型、并发）；`SQLAlchemy` ORM 基础（`declarative_base`、`session`、CRUD）。
- 动手练习：用 SQLAlchemy 定义 2 张表并完成 CRUD。
- 英语任务：背 10 个数据库词：table、column、row、primary key、foreign key、query、join、index、transaction、migration。

#### 周末：把数据分析项目升级为"数据库版"

- 要求：把订单数据导入 PostgreSQL；分析查询改用 SQL；写 5 个常用查询函数。

### 3.4 第 12 周：Web 后端（FastAPI）

#### 第 1 天：HTTP 与 Web 基础

- 知识点：HTTP 方法与状态码；URL 结构；请求/响应；REST 资源思维；JSON。
- 动手练习：用 `curl` 或浏览器访问公开 API（如天气/汇率公开接口），观察请求与响应结构。
- 英语任务：背 10 个 Web 词：endpoint、route、request、response、status code、JSON、API、client、server、middleware。

#### 第 2–3 天：FastAPI 入门

- 知识点：`FastAPI` + `uvicorn`；路径参数/查询参数；`GET/POST/PUT/DELETE`；`pydantic` 模型校验；`status_code`；文档 `/docs`（自动 Swagger）。
- 动手练习：
  1. 写"待办事项 API"：内存列表实现 CRUD，全部带类型校验。
  2. 写"计算器 API"：`/calc?op=add&a=1&b=2`，非法参数返回 422。
  3. 用 `requests` 写客户端测试自己的 API。
- 常见坑：路径参数类型要声明；POST 用 `pydantic` 模型接收 body；重启服务才生效（用 `--reload`）。

#### 第 4 天：数据库接入 API

- 知识点：SQLAlchemy + FastAPI 集成（`Session`、依赖注入 `Depends`）；创建/读取模式（schema）；简单分页。
- 动手练习：把待办事项 API 改为 SQLite 持久化。
- 常见坑：Session 用完要关闭（用 `Depends(get_db)` + `yield`）；模型与 schema 分离。

#### 第 5 天：认证与安全基础

- 知识点：`OAuth2` 密码模式 + JWT 签发/校验（`python-jose` + `passlib`）；密码哈希；`CORS`；输入校验与注入防护。
- 动手练习：给 API 加注册/登录/获取当前用户接口；保护 `/me` 路由。
- 安全底线：永远不存明文密码；永远用参数化 SQL；JWT 密钥不提交到 GitHub（用环境变量）。

#### 周末：部署到云服务器

- 内容：注册云服务器（AWS 免费层/轻量云）；安装 Python/uvicorn；`systemd` 守护进程；`nginx` 反向代理；域名 + HTTPS（Let's Encrypt）。
- 动手：把待办 API 部署上线，用手机访问验证。
- 验收：`https://你的域名/docs` 可访问；重启服务器后服务自动恢复。

### 3.5 第 13 周：算法与数据结构

- 内容（每天一个主题 + LeetCode 3 题）：
  1. 复杂度分析（Big-O 直觉）。
  2. 数组与字符串：双指针、滑动窗口。
  3. 哈希表与集合：两数之和、计数类问题。
  4. 栈与队列：括号匹配、单调栈入门。
  5. 链表：反转、合并、快慢指针。
  6. 递归与回溯入门：排列组合。
  7. 排序与二分：常用排序手写、二分查找模板。
- 要求：每主题手写 2–3 题；用英文写题解 1 题（发 dev.to 或存笔记）。
- 英语任务：背 10 个算法词：complexity、recursion、pointer、stack、queue、hash、sort、binary search、timeout、optimize。

### 3.6 第 14 周：并发入门 + L3 收尾

#### 第 1–2 天：并发编程基础

- 知识点：多线程 vs 多进程 vs asyncio；GIL 是什么、影响什么；`threading`（并发 IO 场景）；`multiprocessing`（CPU 密集）；`asyncio` 入门（`async/await`、`asyncio.run`、`gather`）；`concurrent.futures` 的 `ThreadPoolExecutor/ProcessPoolExecutor`。
- 动手练习：
  1. 用线程池并发下载 20 个网页（对比串行时间）。
  2. 用 `asyncio` 并发请求 10 个公开 API。
  3. 用多进程计算素数个数（对比 CPU 密集场景）。
- 常见坑：共享变量要加锁；线程池任务要处理异常；asyncio 里不能调阻塞函数。

#### 第 3–4 天：并发在爬虫中的应用

- 知识点：限速与并发平衡；`asyncio + aiohttp` 爬虫；断点续爬（记录已完成 URL）；失败重试队列。
- 动手：把 L2 爬虫升级为并发版（≤ 10 并发 + 限速），对比耗时。
- 合规：并发也要遵守 robots.txt 与站点限速，量级保持克制。

#### 第 5 天：L3 测验 + 项目收尾

- 内容：L3 测验（闭卷 60 分钟）；把数据分析项目和 API 服务整理进 GitHub 作品集；写英文 README。

#### 周末：L3 项目验收

- 验收项：
  1. 数据分析报告：结构完整、结论有数据支撑、可复现。
  2. API 服务：线上可访问、文档齐全、有测试。
- 升级条件：测验 ≥ 80 分 + 两项目验收通过 → 进入 L4。

**L3 完成标志**：测验通过 + 数据分析报告 + 线上 API 服务 + GitHub 5 个公开项目。

---

## 4. L4 工程化（第 15–22 周）

**等级目标**：具备生产级交付能力——测试、容器化、CI/CD、性能优化、项目架构都能独立完成；接近"高级程序员"门槛。
**考核**：一个生产级完整项目通过验收。

### 4.1 第 15 周：测试进阶

#### 第 1–2 天：pytest 完整能力

- 知识点：`fixture`（scope：function/module/session、`yield` fixture、`conftest.py`）；`parametrize`；`monkeypatch`；`tmp_path`；断言进阶（`pytest.raises`、近似比较）。
- 动手练习：为 FastAPI 项目写 API 测试（用 `TestClient`），覆盖正常/边界/异常路径。
- 常见坑：fixture 命名与测试参数一致；`TestClient` 需要 `with` 上下文。

#### 第 3–4 天：Mock 与覆盖率

- 知识点：`unittest.mock`（`patch/MagicMock`）；何时该 mock（外部服务、时间、随机）；覆盖率工具（`pytest-cov`）；覆盖率 ≠ 质量。
- 动手练习：给爬虫写测试：mock 网络请求，验证解析逻辑；把项目覆盖率跑到 80%+。
- 常见坑：过度 mock 导致测试失去意义；mock 路径写错（要 patch 使用处的路径）。

#### 第 5 天 + 周末：TDD 实战

- 知识点：TDD 流程（红-绿-重构）；测试先行开发一个功能模块。
- 动手：用 TDD 开发"购物车结算"模块（折扣、税费、满减），先写测试再实现。

### 4.2 第 16 周：Git 工作流与 GitHub

#### 第 1–2 天：Git 进阶

- 知识点：`branch/checkout/merge`；冲突解决；`rebase` vs `merge`；`stash`；`cherry-pick`（了解）；`reflog` 救援；`tag`。
- 动手练习：模拟两人协作（两个分支各改同一文件），完整走一遍冲突解决。
- 常见坑：`git pull` 前先 `commit/stash`；不要 `git push --force` 到共享分支。

#### 第 3–4 天：协作与 PR

- 知识点：Fork + PR 流程；Code Review 评论；`GitHub Issues`；`branch protection`。
- 动手：给一个开源项目（如喜欢的 Python 库）提交一个文档修正 PR 或提一个 issue（L5 再做代码贡献，这里先练习流程）。
- 英语任务：背 10 个 Git 词：branch、merge、conflict、commit、push、pull、fork、pull request、review、rebase。

#### 第 5 天 + 周末：Git 规范与团队模拟

- 要求：制定个人 commit 规范（如 conventional commits）；用 GitHub 组织/仓库模拟 3 人协作完成一个小功能。

### 4.3 第 17 周：Docker

#### 第 1–2 天：Docker 基础

- 知识点：镜像 vs 容器；`Dockerfile`（`FROM/COPY/RUN/CMD/EXPOSE/WORKDIR`）；`docker build/run/ps/exec/logs/rm`；数据卷；端口映射；`.dockerignore`。
- 动手练习：把一个 FastAPI 项目容器化，本地跑通。
- 常见坑：镜像尽量精简（用 slim）；`COPY` 顺序影响缓存；容器里文件权限。

#### 第 3–4 天：docker-compose 与多服务

- 知识点：`docker-compose.yml`（`services/networks/volumes/environment`）；app + db（PostgreSQL）+ redis 编排；健康检查。
- 动手练习：把"API + PostgreSQL"用 compose 一键启动。
- 常见坑：服务间连接用服务名；环境变量集中管理（`.env`）。

#### 第 5 天 + 周末：部署实战

- 要求：把生产级 API 用 Docker 部署到云服务器；配置 nginx + HTTPS；写 `deploy.md` 部署文档。

### 4.4 第 18 周：CI/CD

#### 第 1–3 天：GitHub Actions

- 知识点：`workflow`（`on/ jobs/ steps/ actions`）；`checkout`、`setup-python`；跑测试、跑 lint、构建镜像；`secrets` 管理。
- 动手练习：给项目配 3 条流水线：PR 触发跑测试 + lint；main 分支构建 Docker 镜像；定时任务（如每周依赖更新检查）。
- 常见坑：workflow 语法缩进；权限 `contents: read` 最小化；secrets 不打印。

#### 第 4–5 天：部署自动化

- 知识点：`docker/build-push-action` 推镜像到 GitHub Container Registry；`ssh-action` 或 `webhook` 触发服务器拉取部署；环境变量与配置分离。
- 动手：实现"push main → 自动测试 → 构建镜像 → 自动部署"完整链路。

#### 周末：为作品集项目全面接入 CI/CD

- 验收：每个公开项目 PR 自动跑测试；README 有 CI 徽章（build passing）。

### 4.5 第 19 周：设计模式与 SOLID

#### 第 1–2 天：SOLID 原则

- 知识点：单一职责、开闭、里氏替换、接口隔离、依赖反转；每原则 1 个"坏代码 → 重构"案例。
- 动手练习：用 SOLID 审查自己一个项目，重构 3 处。

#### 第 3–5 天：常用设计模式（Python 实现）

- 知识点（每个模式：场景、代码、优缺点）：单例；工厂方法/抽象工厂；策略模式；观察者模式；装饰器模式；适配器；模板方法；依赖注入容器思想。
- 动手练习：为每个模式写 1 个 20 行左右的示例 + 使用场景说明。
- 常见坑：不要为了模式而模式；优先简单方案，模式是重构的结果不是预设。

#### 周末：模式在真实项目的应用

- 要求：在待办 API 或数据分析项目中，识别并应用 2 个模式，写文档说明"为什么"。

### 4.6 第 20 周：代码质量与 Review

#### 第 1–2 天：静态检查与类型

- 知识点：`mypy` 严格模式；`ruff` 完整规则集；`pre-commit` 钩子（格式化+检查自动化）；`black` 格式化。
- 动手练习：给全部项目配置 `pre-commit`；mypy 0 错误。

#### 第 3 天：Code Review 实操

- 知识点：审查清单（逻辑、边界、安全、性能、可读、测试）；评论的艺术（建设性、具体）；接收 Review 的心态。
- 动手：找一个开源 PR 练习审查（写审查意见）；把自己项目发到社区求 Review（如 Reddit r/learnpython 或 GitHub）。

#### 第 4–5 天：重构与代码坏味道

- 知识点：坏味道清单（长函数、重复代码、魔法数字、上帝类）；重构手法（提取函数、引入常量、拆分类）。
- 动手：对一个 500 行项目做一次系统重构，前后对比指标（行数、圈复杂度）。

#### 周末：工程化周总结

- 输出：写一篇中文技术博客或英文 dev.to 文章《How I Review My Own Python Code》（500 词以上）。

### 4.7 第 21 周：性能优化

#### 第 1 天：性能分析

- 知识点：`timeit`；`cProfile` 分析热点；`memory_profiler` 内存分析；`line_profiler`。
- 动手：对一个数据处理程序做 profile，找出 Top 3 瓶颈。
- 常见坑：先分析再优化，不要凭感觉；优化要配基准测试。

#### 第 2 天：算法与数据结构优化

- 知识点：查找优化（list vs set vs dict）；避免 O(n²)；缓存 `lru_cache`；惰性求值。
- 动手：把 3 个慢程序用算法优化，记录加速比。

#### 第 3 天：IO 与并发优化

- 知识点：批量读写；连接池；异步 IO 改造；`pandas` 高效读取（`dtype`、分块）。
- 动手：优化一个文件处理程序（1GB 数据），从串行改并行，记录时间。

#### 第 4 天：数据库与缓存

- 知识点：索引设计与 `EXPLAIN`；查询优化；Redis 缓存入门（`redis-py`）；缓存策略（旁路缓存、过期）。
- 动手：给 API 加 Redis 缓存（热点数据），测 QPS 提升。
- 常见坑：缓存失效与一致性；不加索引的 LIKE 查询；连接不释放。

#### 第 5 天 + 周末：性能优化专题报告

- 要求：选一个项目做完整性能优化，输出报告：基准 → 瓶颈 → 优化 → 收益数据。

### 4.8 第 22 周：项目架构与综合项目

#### 第 1–2 天：架构设计基础

- 知识点：分层架构（接口层/业务层/数据层）；配置管理（环境变量、配置类）；日志体系（分级、链路追踪思路）；错误处理与监控（异常上报、健康检查）。
- 动手：设计一个"订单系统"的架构草图（数据流图 + 模块划分）。

#### 第 3–6 天：L4 综合项目（生产级交付）

- 项目：**"带认证的数据库 API 服务"**（如：个人知识库笔记 API / 订单管理 API）：
  1. 功能：用户注册登录（JWT）、资源 CRUD、分页、搜索、数据校验。
  2. 质量：pytest 覆盖率 ≥ 80%、mypy 0 错误、ruff 通过、pre-commit。
  3. 工程：Docker + docker-compose（app+db+redis）、GitHub Actions（测试+构建+部署）、nginx + HTTPS。
  4. 文档：英文 README（架构图、API 文档、部署步骤）+ 中文设计文档。
- 验收标准（按高级程序员评审标准）：在干净环境按 README 5 步内跑起来；全链路自动化；代码可维护。

#### 第 7 天：L4 测验 + 项目验收

- 测验：闭卷 90 分钟（架构设计题 + 代码题）。
- 验收：按评审清单逐项过（见附录 C）。

**L4 完成标志**：测验通过 + 生产级项目验收通过 + 能独立完成 Code Review + GitHub 有 6+ 公开项目。

---

## 5. L5 专家打磨（第 23–36 周）

**等级目标**：达到"高级 Python 程序员"门槛——能读并修改开源源码、能设计系统、能评审他人代码、能用英文技术沟通、有可展示的作品集与收入来源。
**考核**：完整系统项目 + 开源 PR + 3 篇英文技术文章 + 英文模拟面试通过。

### 5.1 第 23–26 周：源码阅读与理解

#### 第 23 周：requests 源码精读

- 内容：按"入口 → Session → 请求构造 → 连接池 → 重试 → 响应解析"主线读；重点：`requests.api`、`Session.request`、`HTTPAdapter`、重试机制；画一张 requests 架构图（自己画）。
- 产出：写一篇英文文章《How requests works under the hood》（发 dev.to）。

#### 第 24 周：Flask 或 FastAPI 源码精读

- 内容：路由注册与分发机制；请求上下文（`g/request`）；中间件；`pydantic` 校验如何集成；选一个真实请求跟踪调用链。
- 产出：给源码写注释笔记（GitHub 仓库或博客）。

#### 第 25 周：pandas 核心源码精读

- 内容：`DataFrame` 内部结构（BlockManager 概念）；`read_csv` 解析流程；`groupby` 实现思路；只看核心路径，不求全懂。
- 产出：笔记 + 一篇中文知乎长文或英文文章。

#### 第 26 周：源码阅读方法总结 + 复刻练习

- 内容：总结"读源码方法论"（定位入口、跟踪数据流、看测试、最小复现）；用标准库实现一个小型 `requests` 简化版（`http.client` 层面）或小型装饰器框架。
- 验收：能向别人讲清"一个 HTTP 请求从 urllib 到响应经过哪些环节"。

### 5.2 第 27–28 周：Python 底层与高级特性

#### 第 27 周：CPython 对象模型

- 内容：对象头（`PyObject`）；引用计数与垃圾回收（分代 GC）；不可变对象与内存管理（小整数缓存、字符串驻留）；`id()` 与内存地址。
- 动手：用 `sys.getrefcount`、`gc` 模块观察对象生命周期；写"小整数缓存"演示程序。

#### 第 28 周：描述符、元类与高级语言特性

- 内容：描述符协议（`__get__/__set__`，理解 `@property` 本质）；元类（`type` 创建类、`__new__`/`__init__`）；`__slots__` 内存优化；`contextvars`；`dataclasses` 深用（`field/frozen/PostInit`）；`enum`。
- 动手：用描述符实现一个"类型校验属性"；用元类实现"注册所有子类"的插件系统。
- 产出：英文文章《Descriptors and metaclasses in Python》。

### 5.3 第 29–30 周：异步与并发深入

#### 第 29 周：asyncio 深入

- 内容：事件循环机制；`Task/Future/coroutine` 关系；`async with` / `async for`；`asyncio.Lock/Semaphore`；`asyncio.run_in_executor` 桥接阻塞代码；与线程的协作模型。
- 动手：写一个并发限速的异步爬虫框架（可配置并发数、重试、断点续爬）；压测对比线程版。
- 常见坑：事件循环里阻塞；`asyncio.gather` 的异常传播（`return_exceptions`）。

#### 第 30 周：多进程与分布式思维

- 内容：进程池与共享内存（`multiprocessing` 高级用法）；`concurrent.futures` 实战；分布式任务队列概念（Celery/RQ 了解）；消息队列（Redis Stream / Kafka 概念）。
- 动手：把一个 CPU 密集任务改造为进程池并行，写基准报告。
- 产出：英文文章《Concurrency in Python: threads, asyncio, and processes》。

### 5.4 第 31–32 周：系统设计与工程深化

#### 第 31 周：系统设计基础

- 内容：设计方法论（需求 → 估算 → 架构 → 关键决策 → 演进）；经典组件：缓存、队列、数据库分片、限流、日志与监控；微服务 vs 单体权衡；API 设计规范（版本、错误码、幂等）。
- 动手：做 2 个设计题（如：设计一个短链接服务 / 设计一个爬虫调度系统），画架构图 + 写设计文档。
- 英语任务：背 10 个架构词：scalability、availability、latency、throughput、cache、queue、sharding、idempotency、monitoring、load balancer。

#### 第 32 周：项目架构实战

- 内容：把 L4 项目升级为多模块架构；引入任务队列处理慢任务；加监控（健康检查、指标、告警）；写完整的英文架构文档（README 升级为"architecture"章节）。
- 验收：架构文档能让他人 30 分钟内理解项目全貌。

### 5.5 第 33–34 周：开源贡献与算法冲刺

#### 第 33 周：开源贡献全流程

- 内容：选择目标项目（按兴趣：FastAPI/requests/pandas/自己用的库）；从文档/issue 起步（good first issue）；贡献代码 PR 全流程（fork → branch → commit → PR → 回应 review → merge）；贡献类型：文档、测试、bugfix、feature。
- 动手：完成 1 个真实 PR 被合并（或至少进入 review 阶段）。
- 注意：贡献前读 CONTRIBUTING.md；小步提交；尊重维护者时间。

#### 第 34 周：LeetCode 系统训练

- 内容：每天 2 题（重点题型：数组/字符串、哈希、双指针、滑动窗口、栈、树、DFS/BFS、动态规划、贪心、图入门）；每周一次限时模拟（45 分钟 2 题）。
- 要求：每 3 题写 1 篇英文题解（发 dev.to）；建立错题本（错误原因分类）。

### 5.6 第 35–36 周：作品集、英语与求职/接单冲刺

#### 第 35 周：作品集与个人品牌

- 内容：整理 GitHub 主页（README 个人介绍、置顶 6 个项目）；项目 README 全部升级（截图、架构图、演示链接、技术栈徽章）；写个人英文技术简历（1 页）；更新 Upwork/Fiverr Profile 为"高级"定位。
- 动手：完成全部线上资料；英文自我介绍视频（2 分钟，录制并复盘）。

#### 第 36 周：英文面试与市场冲刺

- 内容：英文技术面试模拟（自我介绍、项目深挖、系统设计、算法白板，各练 1 轮）；英文行为面试（STAR 法则）；投递策略：远程岗位（如 remote job boards）+ 高客单价接单（$500+）。
- 动手：完成 3 次模拟面试（可找 AI 或社区伙伴）；本周至少投出 5 个岗位/10 个 Proposal。

#### 最终验收（L5 毕业标准，对照"高级程序员"画像）：

1. 一个独立设计的完整系统项目（含架构文档、测试、CI、部署、英文文档）。
2. 至少 1 个被合并的开源 PR。
3. 3 篇以上英文技术文章（dev.to）发布。
4. LeetCode 累计 150+ 题，含 20 篇英文题解。
5. 英文模拟面试通过（能流利介绍项目、讨论技术选型）。
6. 有稳定的收入来源（接单/岗位）或明确的 offer 在手。

**L5 完成标志**：上述 6 项全部达成 → 达成"高级 Python 程序员"水平。

---

## 6. 贯穿全程：技术英语 + 接单变现 + 打卡

### 6.1 技术英语计划（每日 30–60 分钟，与编程同步）

| 阶段 | 内容 | 产出 |
|---|---|---|
| L1（第 1–4 周） | 背记核心词汇（每课 10 词，共 100+）；读 Python 官方 Tutorial 英文版对应章节 | 词汇本（可导入 Anki） |
| L2（第 5–8 周） | 写英文 README；读英文错误信息并翻译；看英文教程视频（开英文字幕） | 3 个项目的英文 README |
| L3（第 9–14 周） | 英文技术文档阅读（FastAPI/Pandas 官方文档）；代码注释改英文；看英文视频无字幕试听 | 注释全英文的代码库 |
| L4（第 15–22 周） | 用英文写 2 篇技术文章（dev.to）；英文 Code Review 评论；听英文技术播客 | 2 篇英文文章 |
| L5（第 23–36 周） | 英文面试模拟、英文演讲、活跃英文社区（GitHub issue、Stack Overflow 回答） | 3+ 篇英文文章 + 面试通过 |

- 词汇工具：Anki 每日 15 分钟；每周 50 新词。
- 听力：L3 起每天 15 分钟英文技术视频/播客。
- 口语：L4 起每天 10 分钟"用英文讲今天学的内容"（录音自听）。

### 6.2 接单变现指南（从 L2 第 8 周启动）

- **平台**：Upwork（长单/专业）、Fiverr（标准化小单）、Freelancer/PeoplePerHour 备选；国内：猪八戒、淘宝服务市场（起步可选）。
- **Profile 要点**：头像专业；标题含关键词（Python / Web Scraping / Data Processing / API）；简介 3 段（能力、流程、交付物）；放 3 个作品链接。
- **报价策略**：前 5 单以"低价 + 好评"为目标（低于市场价 20–30%）；之后按市场价；做出 5 个五星好评后提价 30%。
- **接单流程规范**：明确需求 → 书面确认范围 → 收定金（30–50%）→ 定期汇报 → 交付 + 演示 → 收尾款 → 要评价。
- **安全与合规**：不接违法/灰产单（爬取个人隐私数据、绕过付费墙、攻击类）；不泄露客户数据；签简单 NDA；提现走正规渠道。
- **Proposal 模板**（见附录 B）。

### 6.3 每日打卡与复盘模板

```markdown
## 日期：2026-__-__ 星期__
**今日任务完成度**：□ 上午学习 □ 下午练习 □ 英语 □ 复盘
**今天学会了**（用一句话讲给别人听）：
**卡住的问题**：
**解决方式**：
**明日 3 件事**：1. 2. 3.
```

- 建议用 `doubao-cron-scheduler` 建每日提醒（如每天 21:30 提醒复盘）。
- 每周日 30 分钟周复盘：本周产出（代码行数、项目、文章）、下周计划、进度与计划偏差。

---

## 7. 资源清单

### 7.1 免费资源（官方优先）

| 资源 | 用途 | 阶段 |
|---|---|---|
| Python 官方 Tutorial（英文） | 语法权威参考 | L1–L2 |
| Python 官方文档（中文版/英文版） | 查库 | 全程 |
| w3schools Python / Real Python（英文） | 补充阅读 | L1–L3 |
| CS50P（Harvard，英文课程） | 系统打基础（可选加速） | L1 |
| Corey Schafer / Tech With Tim（YouTube） | 视频教学 | L1–L2 |
| Exercism / HackerRank | 练习题 | L1–L3 |
| LeetCode | 算法 | L3–L5 |
| FastAPI / Pandas / requests 官方文档 | 库学习 | L3+ |
| roadmap.sh / Full Stack Python | 路线参考 | 全程 |

### 7.2 书籍（按需选购，不囤书）

| 书 | 定位 | 阶段 |
|---|---|---|
| 《Python Crash Course》（英文） | 入门强化练习 | L1 |
| 《Fluent Python》2nd（英文，精通 Python） | 进阶圣经 | L2–L3 |
| 《Python Cookbook》 | 查手册 | L2–L4 |
| 《Clean Code》（Robert Martin） | 代码质量 | L4 |
| 《Design Patterns: Elements of Reusable OOP》或 Python 版 | 设计模式 | L4 |
| 《A Byte of Python》（免费） | 补充 | L1 |

### 7.3 社区与提问

- Stack Overflow（英文提问）；Reddit r/learnpython、r/Python；GitHub Discussions；中文：Python 中文社区、知乎专栏。
- 提问规范：最小可复现代码 + 期望/实际输出 + 环境信息。

---

## 附录 A：测验样题（各等级抽 5 题示意）

### L1 样题
1. 写出 `[1,2,3,4,5]` 的反转（两种方法）。
2. `"hello world"` 每个单词首字母大写，结果是什么？
3. 读 `data.txt` 每行一个数字，求和（含异常处理）。
4. `d = {"a": 1, "b": 2}`：如何安全取 `"c"` 的值，默认 0？
5. 写一个函数 `is_palindrome(s)` 判断回文。

### L2 样题
1. 写一个装饰器，缓存函数结果（提示 `lru_cache` 或自写 dict 缓存）。
2. `yield` 和 `return` 在一个函数里能共存吗？为什么？
3. 用正则提取 `"Order #12345 on 2026-09-01 cost $99.9"` 中的订单号、日期、金额。
4. 类 `A` 继承 `B`，`super().__init__()` 的作用是什么？
5. 写一个 pytest 测试：函数 `divide(a, b)` 除零时抛 `ValueError`。

### L3 样题
1. Pandas：如何筛选"金额 > 1000 且城市为上海"的行？
2. SQL：`SELECT city, COUNT(*) FROM orders GROUP BY city HAVING COUNT(*) > 10;` 含义？
3. FastAPI：写一个 `GET /users/{id}`，返回用户或 404。
4. 列表 `[3,1,2]` 用 `sorted` 和 `.sort()` 的区别？
5. 什么时候用 `asyncio` 而不是多线程？

### L4 样题
1. pytest fixture 的 `scope="session"` 和 `"function"` 区别？
2. 写一个 `Dockerfile` 部署 FastAPI 应用（3 行核心）。
3. GitHub Actions：何时触发 `pull_request` 和 `push` 事件？
4. 什么情况下你会引入 Redis 缓存？如何保证一致性？
5. 简述 SOLID 中"开闭原则"并举例。

### L5 样题
1. 描述一个 HTTP 请求在 requests 库中的完整调用链。
2. GIL 是什么？它如何影响多线程？什么场景该用多进程？
3. 设计一个限流系统（令牌桶/漏桶），画图并说明。
4. 你如何向非技术客户解释一个复杂系统？（英文回答）
5. 评估一段你 review 的代码：安全、性能、可读性各指出一个问题。

---

## 附录 B：英文 Proposal 模板（接单用）

```
Hi [Client Name],

I read your job post about [summarize the task in one sentence, e.g. scraping
product data from a website into Excel].

What I'll deliver:
1. Clean, working Python script that [key output]
2. The final data in Excel/CSV with [columns/quality checks]
3. A short video walkthrough + documentation

Why me: I have [X months/years] of Python experience and have completed
similar projects like [link to portfolio]. I follow the site's terms and
robots.txt, and I handle edge cases (missing data, timeouts, pagination).

Timeline: [e.g. 3 days after we confirm details]
Budget: flexible — happy to discuss after you confirm the exact scope.

Looking forward to working with you,
[Your Name]
```

（发布前把方括号内容替换成真实信息；Proposal 前 2 行就要点明"我懂你的需求"。）

---

## 附录 C：生产级项目验收清单（L4 用）

- [ ] 干净环境按 README 5 步内能跑起来
- [ ] 测试覆盖率 ≥ 80%，`pytest` 全绿
- [ ] `mypy` 0 错误，`ruff` 通过，`pre-commit` 生效
- [ ] Docker 镜像可构建，compose 一键启动
- [ ] CI 流水线：PR 自动测试 + main 自动部署
- [ ] HTTPS 线上可访问，重启自恢复
- [ ] 英文 README：功能、架构、API、部署、截图
- [ ] 日志完整、错误友好、无明文密码/密钥
- [ ] 代码分层清晰，函数 < 50 行，无重复代码
- [ ] 有健康检查与基本监控

---

*本计划按每天 6–8 小时全职投入设计；时间紧张可压缩 L5 源码/算法内容，但 L1–L4 的项目验收不建议跳过。祝学有所成。*


