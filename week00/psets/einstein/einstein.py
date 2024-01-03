# Einstein

c = 300000000

def main():
    while True:
        try:
            mass = int(input("m: "))
        except ValueError:
            print("Invalid number.")
            continue
        else:
            break

    print(f"e: {equivalence(mass)}")


def equivalence(m):
    return m * square(c)


def square(n):
    return n * n


main()