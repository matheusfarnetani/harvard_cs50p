# Bitcoin Price Index

import requests
import sys

URL = "https://api.coindesk.com/v1/bpi/currentprice.json"


def main():
    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")

    try:
        response = requests.get(URL)
    except requests.RequestException:
        sys.exit("Failed to get response from URL")
    o = response.json()

    amount = o["bpi"]["USD"]["rate_float"] * n
    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()