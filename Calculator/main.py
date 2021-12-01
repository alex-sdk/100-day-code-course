from art import logo

def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def mulitiply(n1, n2):
    return n1 * n2


def exponent(n1, n2):
    return n1 ** n2

operations = {
    "+":add,
    "-":substract,
    "/":divide,
    "*":mulitiply,
    "^":exponent,
}


def calculator():
    print(logo)
    num1 = float(input("Please enter the first number: \n"))

    for symbol in operations:
        print(symbol)

    operator = input("Please selection which operation from above.\n")
    num2 = float(input("Please enter the second number: \n"))

    calcfunction  = operations[operator]
    answer = calcfunction(num1, num2)

    print(f"{num1} {operator} {num2} = {answer}")

    calculating = True 
    while calculating:
        continues = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. To exit enter any other input.\n")
        if continues == 'n':
            calculator()
            break
        elif continues == 'y':
            operator = input("Pick another operation: \n")
            num3 = float(input("Please enter the next number: \n"))
            calcfunction = operations[operator]
            prev_answer = answer
            answer = calcfunction(answer, num3)
            print(f"{prev_answer} {operator} {num3} = {answer}")
        else:
            quit()
calculator()