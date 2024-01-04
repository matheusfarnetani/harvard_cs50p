# File Extensions

suffixes = (".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip")

def main():
    fileName = input("File name: ").strip().lower()
    if check_extension(fileName):
        fileName = fileName.split(".")
        match fileName[-1]:
            case "gif" | "png":
                print(f"image/{fileName[-1]}")
            case "jpg" | "jpeg":
                print("image/jpeg")
            case "txt":
                print("text/plain")
            case _:
                print(f"application/{fileName[-1]}")
    else:
        print("application/octet-stream")


def check_extension(f):
    return f.endswith(suffixes)


if __name__ == "__main__":
    main()
