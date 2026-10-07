# 写一个 safe_divide(a, b)：返回 a/b
# - b == 0 → 打印"除数不能为零"，返回 None
# - 非数字输入 → 打印"请输入数字"，返回 None
# - 成功 → 打印结果并返回
# 要求：try / except（两种）/ else / finally 全用上

def safe_divide(a, b):
    try:
        result = a / b
    except TypeError:
        print("请输入数字")
        return None
    except ZeroDivisionError:
        print("除数不能为零")
        return None
    else:
        print(f"结果是: {result}")
        return result
    finally:
        print("计算结束")