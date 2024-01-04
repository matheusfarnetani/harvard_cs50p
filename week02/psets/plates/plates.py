# Vanity Plates


def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)

    if not 2 <= length <= 6:
        return False
    
    numbers = False
    last_char_is_num = False
    
    length -= 1
    for i, char  in enumerate(s):
        if i < length:
            if not char.isalpha() and not char.isnumeric():
                break
            elif i < 2 and not char.isalpha():
                break
            elif numbers == False and char == "0":
                break
            elif last_char_is_num == True and not char.isnumeric():
                break
            elif char.isnumeric():
                numbers = True
                last_char_is_num = True
            else:
                continue
        else:
            return True
    return False


if __name__ == "__main__":
    main()