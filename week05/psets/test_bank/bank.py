# Back to the Bank


def main():
    greeting = input("Greeting: ").strip().lower()
    greeting = remove_punctuation(greeting).split(" ")
    print(f"${value(greeting[0])}")
    

def value(greeting):
    if greeting == "hello":
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


def remove_punctuation(s):
    return "".join(filter(lambda x: x.isalpha() or x.isdigit() or x.isspace(), s))


if __name__ == "__main__":
    main()
