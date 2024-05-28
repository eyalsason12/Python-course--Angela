def add(n1, n2):
    return n1 + n2


def substrat(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0 or n1 == 0:
        return "not a number"
    else:
        return n1 / n2


operations = {"+": add, "-": substrat, "*": multiply, "/": divide}


def calculator():
    num1 = float(input("what's the first number"))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("what operation do you want to make? ")
        num2 = float(input("what's the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(
            f"type 'y' to continue calculating with {answer}, or type 'n' to exit"
        ) == ("y"):
            num1 = answer
        else:
            should_continue = False


calculator()
