# camelCase


def main():
    camel = input("camelCase: ").strip()
    snake = snake_case(camel)
    print(snake)

def snake_case(s:str):
    new_s = []
    for char in s:
        if char.isupper():
            new_s.append("_")
        new_s.append(f"{char.lower()}")
    
    return "".join(new_s)


if __name__ == "__main__":
    main()