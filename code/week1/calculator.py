def main():
    """
    这是一个简单的计算器程序，允许用户输入两个数字和一个操作符，然后输出计算结果。

    用户可以选择退出程序。

    """
    user_input1 = get_number()
    if user_input1 is None:
        return  # Exit if the user chose to quit
    while True:
        user_input2 = get_number()
        if user_input2 is None:
            return  # Exit if the user chose to quit
        operation = input("Enter an operation (+, -, *, /, %): ")
        result = calculate(user_input1, user_input2, operation)
        if result is not None:
            print(f"The result of {user_input1} {operation} {user_input2} is: {result}")
            user_input1 = result  # Update the first number for the next calculation


def get_number() -> float | None:
    """
    获取用户输入的数字。如果用户输入 'exit'，则返回 None 以退出程序。

    返回：
        float: 用户输入的数字
        None: 如果用户选择退出
    """
    while True:
        try:
            user_input = input("Enter a number (or 'exit' to quit): ")
            if user_input.lower() == "exit":
                print("Exiting the program.")
                return None
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate(number1: float, number2: float, operation: str) -> float | None:
    """
    根据用户输入的操作符执行相应的计算。

    参数：
        number1 (float): 第一个数字
        number2 (float): 第二个数字
        operation (str): 操作符，可以是 '+', '-', '*', '/', '%'

    返回：
        float: 计算结果，如果操作符无效或除数为零，则返回 None
    例外：
        如果除数为零，打印错误信息并返回 None。
    例外：
        如果操作符无效，打印错误信息并返回 None。
    """
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        if number2 != 0:
            return number1 / number2
        else:
            print("Error: Division by zero.")
            return None
    elif operation == "%":
        if number2 != 0:
            return number1 % number2
        else:
            print("Error: Division by zero.")
            return None
    else:
        print("Invalid operation. Please choose from +, -, *, /, or %.")
        return None


if __name__ == "__main__":
    main()
