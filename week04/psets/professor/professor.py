# Little Professor

from sys import exit
import random

OPERATIONS = ["+", "-", "*", "/"]
QUESTIONS = 10
CHANCES = 3


def main():
    level = get_level()
    score = 0

    for _ in range(QUESTIONS):
        x, y, z = generate_math_problem(level)

        result = calculate_result(x, y, z)
        if not result:
            exit(1)
        
        for i in range(CHANCES):
            inpt = get_int(f"{x} {y} {z} = ")
            if inpt == result:
                score += 1
                break
            else:
                print("EEE")
                if i == 2:
                    print(f"{x} {y} {z} = {result}")
            
    print(f"Score: {score}")
    exit(0)


def calculate_result(x, operation, z):
    match operation:
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            return x / z
        case _:
            return False


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            continue


def generate_math_problem(level):
    x = generate_integer(level)
    y = "+" # random.choice(OPERATIONS)
    z = generate_integer(level)
    return x, y, z


def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue

        if 1 <= n <= 3:
            return n


def generate_integer(level):
    if not 0 < level <= 3:
        raise ValueError

    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)


if __name__ == "__main__":
    main()