# Seasons of Love

import re
from sys import exit
from datetime import date
import inflect


def main():
    date = validate(input("Date of Birth: "))
    print(convert_to_words(calculate(date)))


def validate(d):
    if m := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", d):
        try:
            str_d = [int(m.group(i)) for i in range(1, 4)]
        except ValueError: exit(1)
    else: exit(1)
    return date(year=str_d[0], month=str_d[1], day=str_d[2])


def calculate(d):
    diff = date.today() - d
    return ((diff.days * 24) * 60)


def convert_to_words(minutes):
    p = inflect.engine()
    return (p.number_to_words(minutes, andword="") + " minutes").capitalize()


if __name__ == "__main__":
    main()