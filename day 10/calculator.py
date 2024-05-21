def add(n1,n2):
    return n1 + n2

def substrat(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    if n2 == 0 or n1 == 0:
        return "not a number"
    else:
        return n1 / n2

operations = {
    "+": add,
    "-": substrat,
    "*": multiply,
    "/": divide
}

num1 = int(input("insert the first number"))
for symbol in operations:
    print(symbol)
first_operation_symbol = input("what operation do you want to make? ")
num2 = int(input("insert the second number"))
calculation_function = operations[first_operation_symbol]
first_answer = calculation_function(num1,num2)
print(f"{num1} {first_operation_symbol} {num2} = {first_answer}")

continue_calc = True
while continue_calc:
    second_operation_symbol = input("do you want to make another operation ? type the operation sign or type 'no' \n")
    if second_operation_symbol == 'no':
        continue_calc = False
        print("Goodbye")
    else:
        num3 = int(input("insert the number"))
        calculation_function = operations[second_operation_symbol]
        second_answer = calculation_function(first_answer, num3)
        print(f"{first_answer} {second_operation_symbol} {num3} = {second_answer}")

