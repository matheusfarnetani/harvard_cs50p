# Outdated
# ISO 8601

from sys import exit

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
SPLIT_OPTIONS = [None, "/", "-", "_", "\\"]


def main():
    date = get_date("Date: ")
    if not date:
        exit(1)
    
    formated_date = format_date(date)
    print(formated_date)
    exit(0)


def format_date(date):
    return f"{date[2]}-{date[0]:02}-{date[1]:02}"


def check_date(date, split_option):
    for i, x in enumerate(date):

        # Calculate once
        x_int = isinstance(x, int)
        x_str = isinstance(x, str)

        if not x_int and not x_str:
            return False

        if i == 0:
            if x_int and x > 12:
                return False
            elif x_str and split_option:
                return False
            elif x_str and not x in MONTHS:
                return False
            elif x_str and x in MONTHS:
                date = [(MONTHS.index(x)) + 1, date[1], date[2]]
        elif i == 1:
            if x_int and x > 31:
                return False
            elif x_str:
                return False
        elif i == 2:
            if x_int and not len(str(x)) == 4:
                return False
            if x_str:
                return False
    return date


def convert_date(date:list):
    for i in range(len(date)):
        try:
            date[i] = int(date[i])
        except ValueError:
            pass
    return date


def split_date(inpt:str):
    for i in range(len(SPLIT_OPTIONS)):
        date = inpt.split(sep=SPLIT_OPTIONS[i])
        if len(date) == 3:
            return date, i
    return False


def get_inpt(prompt):
    try:
        return input(prompt).strip().title()
    except EOFError:
        print()
        return False


def get_date(prompt):
    while True:
        # Get user's input
        inpt = get_inpt(prompt)
        if not inpt:
            return False

        # Split input into list of 3 instances
        date, split_option = split_date(inpt)
        if not date:
            continue

        # print(date)
        if date[0].isalpha() and not date[1].endswith(","):
            continue
        elif date[0].isalpha() and date[1].endswith(","):
            date[1] = date[1][:-1]
        
        # Convert 
        date = convert_date(date)
        
        # Check
        date = check_date(date, split_option)
        if not date:
            continue

        return date


def remove_punctuation(s):
    return "".join(filter(lambda x: x.isalpha() or x.isdigit(), s))


if __name__ == "__main__":
    main()
