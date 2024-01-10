# Working 9 to 5

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if m := re.search(r"(\d{1,2}):?(\d+)?\s(AM|PM) to (\d{1,2}):?(\d+)?\s(AM|PM)", s):
        time = [m.group(i) for i in range (1, 7)]
    else:
        raise ValueError

    for i in range(len(time)):
        if not time[i]:
            continue
        elif time[i].isdigit():
            time[i] = int(time[i])
        
        if i in [0,3]:
            if not 0 <= time[i] <= 12:
                raise ValueError
            if time[i + 2].lower() == "pm" and time[i] != 12:
                time[i] = time[i] + 12
            elif time[i + 2].lower() == "am" and time[i] == 12:
                time[i] = 0
        elif i in [1,4]:
            if not 0 <= time[i] < 60:
                raise ValueError

    t0 = f"{time[0]:02}:{time[1] if time[1] else 0:02}"
    t1 = f"{time[3]:02}:{time[4] if time[4] else 0:02}"

    return t0 + " to " + t1


if __name__ == "__main__":
    main()