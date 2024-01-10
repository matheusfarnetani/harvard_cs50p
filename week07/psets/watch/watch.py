# Watch on YouTube

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if m := re.search(r'.+src="https?://(?:www\.)?youtube\.com/embed/(.+?)"', s):
        embed_url =  m.group(1)
    else:
        return None
    return f"https://youtu.be/{embed_url}"


if __name__ == "__main__":
    main()