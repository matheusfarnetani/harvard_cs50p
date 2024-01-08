# CS50 P-Shirt

from sys import argv, exit
from os.path import splitext
from PIL import Image, ImageOps

EXTENSIONS = [".jpeg", ".jpg", ".png"]


def main():

    if len(argv) < 3:
        exit("Too few command-line arguments")
    elif len(argv) > 3:
        exit("Too many command-line arguments")
    else:
        for i in range(2):
            if not splitext(argv[i + 1])[-1] in EXTENSIONS:
                exit("Invalid output")
        
        if splitext(argv[1])[-1] != splitext(argv[2])[-1]:
            exit("Input and output have different extensions")

        try:
            file = open(argv[1])
        except FileNotFoundError:
            exit("Input does not exist")
        else:
            file.close()
    
    base = Image.open(argv[1])
    shirt = Image.open("shirt.png")

    base = ImageOps.fit(base, shirt.size)
    base.paste(shirt, shirt)
    
    base.save(argv[2])


if __name__ == "__main__":
    main()