# Coke Machine

COINS = [25, 10, 5]


def main():
    price = 50
    while True:
        if price <= 0:
            print(f"Change Owed: {price if not price < 0 else price * -1}")
            break
        print(f"Amount Due: {price}")
        coin = get_int("Insert Coin: ")
        if not coin:
            continue
        price -= coin


def get_int(message):
    while True:
        try:
            i = int(input(message))
        except ValueError:
            print("Invalid number.")
            continue

        if i not in COINS:
            return False

        return i


if __name__ == "__main__":
    main()