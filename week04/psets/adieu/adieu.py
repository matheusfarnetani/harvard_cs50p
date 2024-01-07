# Adieu, Adieu

import inflect


def main():
    p = inflect.engine()
    words = get_input("Name: ")
    print(f"Adieu, adieu, to " + p.join(words))


def get_input(prompt):
    l = list()
    while True:
        try:
            l.append(input(prompt))
        except EOFError:
            print()
            return l


if __name__ == "__main__":
    main()