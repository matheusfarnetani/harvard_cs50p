# Catches a ValueError

try:
    x = int(input("What's x? "))
    print(f"x s {x}")
except ValueError:
    print("x is not an integer")