# Lines of Code

from sys import argv, exit


def main():

    if len(argv) < 1:
        exit("Too few command-line arguments")
    elif len(argv) > 2:
        exit("Too many command-line arguments")
    else:
        if not argv[1].endswith(".py"):
            exit("Not a Python file")

        try:
            file = open(argv[1])
        except FileNotFoundError:
            exit("File does not exist")
        else:
            file.close()

    lines_of_code = count_lines_of_code(argv[1])
    print(lines_of_code)
    return lines_of_code


def count_lines_of_code(f):
    n = 0
    with open(f) as file:
        for line in file:
            if line.startswith("#") or line[0] == "\n" or line.lstrip() == "":
                continue
            elif line.lstrip("    ").startswith("#"):
                continue
            else:
                n += 1
        return n


if __name__ == "__main__":
    main()
