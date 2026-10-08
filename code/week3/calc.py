print("module loaded")
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    return a / b

def evaluate(a, b, operation):
    """Evaluate the expression based on user input."""
    if operation == '+':
        return add(a, b)
    elif operation == '-':
        return subtract(a, b)
    elif operation == '*':
        return multiply(a, b)
    elif operation == '/':
        return divide(a, b)
    else:
        raise ValueError("Invalid operation. Please choose from +, -, *, or /.")
  