# QA · pip 报 "from versions: none" 怎么办？/ pip says "from versions: none" — what now?

## 中文

**问题**：`pip install ruff` 报错：

```
ERROR: Could not find a version that satisfies the requirement ruff (from versions: none)
ERROR: No matching distribution found for ruff
```

**排查顺序**（按优先级）：

1. **看 Python 版本**：`python --version`。太旧（如 < 3.7）会过滤掉所有新版本 → `from versions: none`。但 Python 3.12 完全没问题。
2. **看 pip 版本**：`pip --version`。太旧（< 20）解析新包元数据可能失败 → `pip install --upgrade pip`。
3. **换镜像源**（最常见原因——当前镜像对该包同步异常）：

```bash
# 阿里云（国内快）
pip install ruff -i https://mirrors.aliyun.com/pypi/simple/

# 腾讯云
pip install ruff -i https://mirrors.cloud.tencent.com/pypi/simple/

# 官方源（网络允许时最准）
pip install ruff -i https://pypi.org/simple
```

**本案例**：Python 3.12.3 + pip 24.0 都没问题，清华镜像（tuna）对 ruff 同步异常 → 换阿里云一次成功。

**提示**：换源只对**当前命令**生效。想持久改默认源：

```bash
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
```

---

## English

**Problem**: `pip install ruff` fails with:

```
ERROR: Could not find a version that satisfies the requirement ruff (from versions: none)
```

**Troubleshoot in this order**:

1. **Check Python version**: `python --version`. Too old (e.g. < 3.7) filters out all new versions → `from versions: none`.
2. **Check pip version**: `pip --version`. Very old pip may fail parsing new metadata → `pip install --upgrade pip`.
3. **Switch the mirror** (most common cause — the current index has a sync problem for that package):

```bash
pip install ruff -i https://mirrors.aliyun.com/pypi/simple/
pip install ruff -i https://pypi.org/simple
```

**This case**: Python 3.12.3 + pip 24.0 were both fine; the Tsinghua mirror had a sync issue for ruff → Aliyun mirror worked immediately.

To change the default index permanently:

```bash
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
```

---

## 原对话摘录 / Original conversation excerpt

> 摘自学习者与 AI 助教的真实对话（2026-09-21）。

**学习者贴出的报错**：

> "pip install ruff → Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple → ERROR: Could not find a version that satisfies the requirement ruff (from versions: none)"

**助教排查与解决**：

> "`from versions: none` 通常是 Python 版本太旧或镜像同步问题。查了你的环境：Python 3.12.3 + pip 24.0 都没问题——确认是清华镜像对 ruff 的同步异常。换阿里云源：`pip install ruff -i https://mirrors.aliyun.com/pypi/simple/` → 成功安装 ruff 0.16.8。"
