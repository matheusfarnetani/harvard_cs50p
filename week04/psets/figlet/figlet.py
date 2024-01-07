# Frank, Ian and Glen's Letters

from sys import argv, exit
from pyfiglet import Figlet


def main():
    f = Figlet()

    if len(argv) == 3 and (argv[1] == "-f" or argv[1] == "--font"):
        if argv[2] in f.getFonts():
            f.setFont(font=argv[2])
        else:
            exit(2)
    else:
        exit(2)

    inpt = input("Input: ").strip()
    print(f"Output: {f.renderText(inpt)}")
    
    exit(0)


if __name__ == "__main__":
    main()
