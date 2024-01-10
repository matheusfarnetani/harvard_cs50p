# Response Validation

from validator_collection import validators, checkers, errors

def main():
    print(validate(input("What's your email address? ")))


def validate(e):
    return "Valid" if checkers.is_email(e) else "Invalid"
    # try:
    #     validators.email(e)
    # except errors.EmptyValueError:
    #     return "Invalid"
    # except errors.InvalidEmailError:
    #     return "Invalid"
    # else:
    #     return "Valid"


if __name__ == "__main__":
    main()