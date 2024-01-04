# Home Federal Savings Bank


def main():
    greeting = remove_punctuation(input("Greeting: ").strip().lower())
    greeting = greeting.split(" ")

    if greeting[0] == "hello":
        output = 0
    elif greeting[0].startswith("h"):
        output = 20
    else:
        output = 100
    
    print(f"${output}")
    

def remove_punctuation(s):
    return "".join(filter(lambda x: x.isalpha() or x.isdigit() or x.isspace(), s))


if __name__ == "__main__":
    main()
