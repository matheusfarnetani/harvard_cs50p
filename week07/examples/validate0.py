# Validates email addres by checking for @

email = input("What's your email? ").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")