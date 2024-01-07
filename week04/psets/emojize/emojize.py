# Emojize

import emoji

def main():
    inpt = input("Input: ")
    print(f"Output: {emoji.emojize(inpt, language='alias')}")


if __name__ == "__main__":
    main()
