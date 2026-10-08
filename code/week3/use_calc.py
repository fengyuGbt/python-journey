import calc

def main():
    print("Welcome to the calculator!")
    while True:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ")
            if operation.lower() == 'exit':
                print("Exiting the calculator. Goodbye!")
                break
            if operation not in ['+', '-', '*', '/']:
                print("Invalid operation. Please choose from +, -, *, or /.")
                continue
            result = calc.evaluate(a, b, operation)
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        except ZeroDivisionError as e:
            print(e)
            continue

if __name__ == "__main__":
    main()