# Testing my twttr

import re


def main():
    inpt = input("Input: ").strip()
    print(f"Output: {shorten(inpt)}")


def shorten(word:str):
    return re.sub('[aeiouAEIOU]', "", word)


if __name__ == "__main__":
    main()