from ascii_art import calculator_logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What is the first number?: "))

    for operator in operators:
        print(operator)

    another_sum = True
    while another_sum:
        sum_type = input("Pick an operater: ")
        num2 = float(input("What is the second number?: "))

        answer = operators[sum_type](num1, num2)

        print(f"{num1} {sum_type} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to exit.: "):
            num1 = answer
        else:
            another_sum = False

print(calculator_logo)
calculator()