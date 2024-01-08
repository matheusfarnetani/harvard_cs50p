# Refueling

from sys import exit

def main():
    fraction = input("Fraction: ").strip()
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction:str):
    f = fraction.split("/")
    if len(f) != 2: exit(1)

    try:
        r = (int(f[0]) / int(f[1])) * 100 
        return r if r <= 100 else exit("Fraction value is more than 100%")
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError


def gauge(percentage:int):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{round(percentage)}%"


if __name__ == "__main__":
    main()
