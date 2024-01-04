# Deep Thought
import sys


def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    match answer:
        case "42" | "forty-two" | "forty two":
            print("yes")
            sys.exit(0)
        case _:
            print("no")
            sys.exit(1)

if __name__ == "__main__":
    main()
