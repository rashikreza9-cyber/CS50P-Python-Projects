def main():
 fruits = {

}
 item = input("Item: ").lowerca
def main():
    # 1. Create the dictionary with lowercase keys
    fruits = {"apple" : 130,
    "avocado": 50,
    "banana":110,
    "cantaloupe":50,
    "grapefruit":60,
    "grapes":60,
    "honeydew Melon": 50,
    "lemon":15,
    "kiwifruit":90,
    "lime":20,
    "nectarine":60,
    "orange": 80,
    "peach":60,
    "pear":100,
    "pineapple":50,
    "plums":70,
    "strawberries":50,
    "Sweet cherries":100,
    "tangerine":50,
    "watermelon":80
    }

    # 2. Get user input
    item = input("Item: ").lower()

    # 3. Check and Print
    if item in fruits:
        print("Calories:", fruits[item])

main()
