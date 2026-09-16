# CLI calculator - L1 Weekend Project
# Final fixed version; see lessons/009 for the "break exits one loop only" bug.
# Features: + - * / %, chained calculation, 'exit' to quit, division-by-zero guard.

def main():
    user_input1 = get_number()
    if user_input1 is None:
        return  # exit if the user chose to quit
    while True:
        user_input2 = get_number()
        if user_input2 is None:
            return  # exit if the user chose to quit
        operation = input("Enter an operation (+, -, *, /, %): ")
        result = calculate(user_input1, user_input2, operation)
        if result is not None:
            print(f"The result of {user_input1} {operation} {user_input2} is: {result}")
            user_input1 = result  # chain: result becomes the first number of the next round


def get_number():
    while True:
        try:
            user_input = input("Enter a number (or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting the program.")
                return None
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate(number1, number2, operation):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    elif operation == '/':
        if number2 != 0:
            return number1 / number2
        else:
            print("Error: Division by zero.")
            return None
    elif operation == '%':
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
