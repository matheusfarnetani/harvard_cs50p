import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    return len(m) if (m := re.findall(r"\b[uU]m\b", s)) else 0


if __name__ == "__main__":
    main()