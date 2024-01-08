# Pizza Py

from sys import argv, exit
import csv
from tabulate import tabulate


def main():

    if len(argv) < 2:
        exit("Too few command-line arguments")
    elif len(argv) > 2:
        exit("Too many command-line arguments")
    else:
        if not argv[1].endswith(".csv"):
            exit("Not a CSV file")

        try:
            file = open(argv[1])
        except FileNotFoundError:
            exit("File does not exist")
        else:
            file.close()
    
    field_names = [f"{argv[1].removesuffix('.csv').title()} Pizza", "Small", "Large"]
    menu = create_menu(argv[1], field_names)
    print(tabulate(menu, headers="firstrow", tablefmt="grid"))


def create_menu(file, fn):
    m = []
    with open(argv[1]) as file:
        reader = csv.DictReader(file, fieldnames=fn)
        for row in reader:
            m.append(row)
    return m


if __name__ == "__main__":
    main()