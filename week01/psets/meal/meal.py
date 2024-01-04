# Meal Time
from sys import exit


def main():
    time = input("What time is it? ")

    time = convert(time)
    
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        pass

    exit(0)


def convert(time):
    t = time.strip().split(":")

    if len(t) != 2:
        print("Please insert a time value formatted as < hour:minutes >")
        exit(1)
    if not t[0].isdigit() or not t[1].isdigit():
        print("Please insert a time value formatted as < hour:minutes >")
        exit(1)

    t0 = float(t[0])
    t1 = float(t[1])

    return t0 + ((t1 * 100 / 60) / 100)


if __name__ == "__main__":
    main()
