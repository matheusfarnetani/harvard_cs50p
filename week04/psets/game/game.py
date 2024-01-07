# Guessing Game

import random
from sys import exit


def main():
    level = get_int("Level: ")
    number = random.randint(1, level)

    while True:
        guess = get_int("Guess: ")
        if not(compare_numbers(guess, number)):
            continue
        break


def compare_numbers(x, y):
    if x < y:
        print("Too small!")
        return False
    elif x > y:
        print("Too large!")
        return False
    
    print("Just right!")
    return True


def get_int(prompt):
    while True:
        try:
            n = int(input(prompt))
        except ValueError:
            continue
        except EOFError:
            print()
            exit(1)
    
        if n > 0:
            return n


if __name__ == "__main__":
    main()
