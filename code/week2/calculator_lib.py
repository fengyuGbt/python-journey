def add(a: float, b: float) -> float:
    """返回 a 加 b 的和。

    参数：
        a (int/float): 第一个数
        b (int/float): 第二个数

    返回：
        a + b 的结果
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """返回 a 减 b 的差。

    参数：
        a (int/float): 第一个数
        b (int/float): 第二个数

    返回：
        a - b 的结果
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """返回 a 乘 b 的积。

    参数：
        a (int/float): 第一个数
        b (int/float): 第二个数

    返回：
        a * b 的结果
    """
    return a * b


def divide(a: float, b: float) -> float | None:
    """返回 a 除以 b 的商。

    参数：
        a (int/float): 被除数
        b (int/float): 除数

    返回：
        a / b 的结果
    """
    if b == 0:
        print("除数不能为零。")
        return None
    return a / b


def calculate(op: str, a: float, b: float) -> float | None:
    """根据操作符执行相应的计算。

    参数：
        op (str): 操作符，可以是 '+', '-', '*', '/'
        a (int/float): 第一个数
        b (int/float): 第二个数

    返回：
        计算结果，如果操作符无效则返回 None
    """
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        print("无效的操作符。")
        return None
