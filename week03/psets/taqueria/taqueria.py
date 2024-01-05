# Felipe's Taqueria

from sys import exit


MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total = 0
    while True:
        item = get_item("Item: ").strip().title()
        if not item in MENU.keys():
            continue
        
        total += MENU[item]
        print(f"Total: ${total:.2f}")


def get_item(prompt):
    try:
        return input(prompt)
    except EOFError:
        print()
        exit(0)


if __name__ == "__main__":
    main()
    