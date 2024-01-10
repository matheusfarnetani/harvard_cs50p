# Extracts Twitter uername from URL using str.replace

url = ("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")
