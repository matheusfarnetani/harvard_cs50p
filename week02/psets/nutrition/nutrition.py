# Nutrition Facts

# weight is in grams (g)
FRUITS = {
    "apple": {"serving": "1", "size": "large", "weight": 242, "calories": 130},
    "avocado": {"serving": "1/5", "size": "medium", "weight": 30, "calories": 50},
    "banana": {"serving": "1", "size": " medium", "weight": 126, "calories": 110},
    "cantaloupe": {"serving": "1", "size": "medium", "weight": 134, "calories": 50},
    "grapefruit": {"serving": "1/2", "size": "medium", "weight": 154, "calories": 60},
    "grapes": {"serving": "3/4", "size": "cup", "weight": 126, "calories": 90},
    "melon": {"serving": "1/10", "size": "medium", "weight": 134, "calories": 50},
    "kiwifruit": {"serving": "2", "size": "medium", "weight": 148, "calories": 90},
    "lemon": {"serving": "1", "size": "medium", "weight": 58, "calories": 15},
    "lime": {"serving": "1", "size": "medium", "weight": 67, "calories": 20},
    "nectarine": {"serving": "1", "size": "medium", "weight": 140, "calories": 60},
    "orange": {"serving": "1", "size": "medium", "weight": 154, "calories": 80},
    "peach": {"serving": "1", "size": "medium", "weight": 147, "calories": 60},
    "pear": {"serving": "1", "size": "medium", "weight": 166, "calories": 100},
    "pineapple": {"serving": "2", "size": "slices, 3\" diameter, 3/4\" thick", "weight": 112, "calories": 50},
    "plums": {"serving": "2", "size": "medium", "weight": 151, "calories": 70},
    "strawberries": {"serving": "8", "size": "medium", "weight": 147, "calories": 50},
    "sweet cherries": {"serving": "21", "size": "cherries; 1 cup", "weight": 140, "calories": 100},
    "tangerine": {"serving": "1", "size": "medium", "weight": 109, "calories": 50},
    "watermelon": {"serving": "1/18", "size": "medium; 2 cups diced pieces", "weight": 280, "calories": 80},
}


def main():
    fruit = input("Item: ").strip().lower()
    if fruit in FRUITS:
        print(f"Calories: {FRUITS[fruit]['calories']}")


if __name__ == "__main__":
    main()