# Grocery List

# format = {"item": "quantity"}


def main():
    glist = get_groceries_list()
    gdict = make_groceries_dict(glist)
    print()
    for key, value in gdict.items():
        print(f"{value} {key.upper()}")


def make_groceries_dict(l:list):
    groceries = {}
    l.sort()
    for i in range(len(l)):
        if not l[i] in groceries.keys():
            groceries[l[i]] = 1
        else:
            groceries[l[i]] += 1
    return groceries


def get_groceries_list():
    groceries = []
    while True:
        try:
            g = input()
        except EOFError:
            return groceries
        else:
            groceries.append(g)


if __name__ == "__main__":
    main()
