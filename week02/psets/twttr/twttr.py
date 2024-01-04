# Just setting up my twttr

VOWELS = ["a", "e", "i", "o", "u"]


def main():
    inpt = input("Input: ").strip()
    outpt = twttr(inpt)
    print(f"Output: {outpt}")


def twttr(s):
    tmp = []
    for char in s:
        if char.lower() in VOWELS:
            continue
        else:
            tmp.append(char)
    
    return "".join(tmp)


if __name__ == "__main__":
    main()