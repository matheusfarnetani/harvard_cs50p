# Scourgify

from sys import argv, exit
import csv


def main():

    if len(argv) < 3:
        exit("Too few command-line arguments")
    elif len(argv) > 3:
        exit("Too many command-line arguments")
    else:
        for i in range(2):
            if not argv[i + 1].endswith(".csv"):
                exit("Not a CSV file")

        try:
            file = open(argv[1])
        except FileNotFoundError:
            exit("File does not exist")
        else:
            file.close()
    
    students = read_students(argv[1])
    save_students(argv[2], students)


def save_students(file, students):
    with open(file, "w") as f:
        writer = csv.DictWriter(f, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)


def read_students(file):
    students = []
    with open(file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            last, first = row["name"].split(",")
            students.append({"first": first.strip(), "last": last, "house": row["house"]})
    return students


if __name__ == "__main__":
    main()