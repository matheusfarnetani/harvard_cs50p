# Math Interpreter

from sys import exit

def main():
    x, y, z = input("Expression: ").strip().split(" ")

    if not x.isdigit() or not z.isdigit():
        print("Usage: x + y or x - y or x * y or x / y")
        print("x and y must be nummeric.")
        exit(1)

    x = float(x)
    z = float(z)

    match y:
        case "+":
            print(addition(x, z))
        case "-":
            print(substraction(x, z))
        case "*":
            print(multiplication(x, z))
        case "/":
            print(division(x, z))
        case _:
            print("Usage: x + y or x - y or x * y or x / y")
            print("Only \"+ - * /\" operations are available.")
            exit(1)

    exit(0)


def addition(x, y):
    return x + y


def substraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


if __name__ == "__main__":
    main()
