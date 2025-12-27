def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    still_wanna_proceed = True
    num1 = float(input("Enter the first number?:\n"))
    while still_wanna_proceed:
        num2 = float(input("Enter the next number?:\n"))
        for symbol in operations:
            print(symbol)
        operator = input("Pick an operation you want to perform!\n")
        calculation = operations[operator]
        result = calculation(num1, num2)
        print(f"Result of {num1} {operator} {num2} is {result}")
        if input(f"Press y to proceed calculating with {result} or 'n' to exit\n") == 'y':
            num1 = result
        else:
            still_wanna_proceed = False
            calculator()


calculator()