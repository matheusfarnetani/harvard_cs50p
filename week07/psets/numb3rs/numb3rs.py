# NUMB3RS

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(inpt):

    if m := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", inpt):
        ip = [int(m.group(i)) for i in range(1,5)]
    else:
        return False
    
    for i in ip:
        if not 0 <= i <= 255:
            return False

    return True


if __name__ == "__main__":
    main()