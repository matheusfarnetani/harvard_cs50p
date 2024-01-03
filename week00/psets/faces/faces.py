# Making Faces

def main():
    string = input().strip()
    print(convert(string))


def convert(string:str):
    splitString = string.split(" ")
    for i in range(len(splitString)):
        if splitString[i] == ":)":
            splitString[i] = "🙂"
        elif splitString[i] == ":(":
            splitString[i] = "🙁"
        else:
            continue
    return " ".join(splitString)




main()