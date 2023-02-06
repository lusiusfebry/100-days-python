from logo import logo


def addition(a, b):
    return a + b


def multiply(a, b):
    return a * b


def substraction(a, b):
    return a - b


def division(a, b):
    return a / b


def calculator():
    print(logo)
    operation = {
        "+": addition,
        "-": substraction,
        "*": multiply,
        "/": division
    }

    num1 = float(input("What\'s the first number: "))
    for operator in operation:
        print(operator)
    shouldContinue = True
    while shouldContinue:

        operationChoice = input("pick up an operation: ")
        num2 = float(input("What\'s the next number: "))

        calculation = operation[operationChoice]
        answer = calculation(num1, num2)
        print(f"{num1} {operationChoice} {num2} = {answer}")

        again = input(f"Type \'y\' to continue with {answer}, or type \'n\' to start a new calculation: ")
        if again == "n":
            shouldContinue = False
            calculator()
        else:
            num1 = answer


def main():
    calculator()


main()
