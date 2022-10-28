from art import logo


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
    "/": divide
}


def calc():
    print(logo)
    flag = False
    num1 = float(input("Enter first number:"))
    while not flag:
        num2 = float(input("Enter next number:"))
        symbol = input("What operation do you want to do? +, -, *, /: ")
        function = operations[symbol]
        answer = (function(num1, num2))
        print(f'{num1} {symbol} {num2} = {answer}')
        if input(f"Type 'y' to continue with {answer} or type 'n' to start again:") == "y":
            num1 = answer
        else:
            flag = True
            calc()


calc()
