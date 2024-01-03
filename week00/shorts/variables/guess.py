# Short - Variables

def main():
    guess = get_guess()
    if guess == 50:
        print("Correct!")
    else:
        print("Incorrect!")


def get_guess():
    while True:
        try:
            guess = int(input("Enter a guess: "))
        except ValueError:
            print("Invalid number.")
            continue
        return guess


main()
