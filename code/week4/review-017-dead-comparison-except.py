def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero")   # ← 坑 2a：除零语义应该是 ZeroDivisionError
    return a / b

def evaluate(a, b, operation):
    if operation == '+':
        return add(a, b)
    elif operation == '/':
        return divide(a, b)
    else:                          # ← 坑 1：死代码！比较表达式不算执行
        raise ValueError("Invalid operation")  #       else 变"管你输什么一律除"
