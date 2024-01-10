# Replaces character class with \w

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w.edu$", email):
    print("valid")
else:
    print("Invalid")