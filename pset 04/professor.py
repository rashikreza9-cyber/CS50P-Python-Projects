def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass
import random

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    # For level 2: 10 to 99; for level 3: 100 to 999
    lower = 10**(level - 1)
    upper = (10**level) - 1
    return random.randint(lower, upper)
def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        trials = 0

        while trials < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == (x + y):
                    score += 1
                    break
                else:
                    print("EEE")
                    trials += 1
            except ValueError:
                print("EEE")
                    trials += 1
            except ValueError:
                print("EEE")
                trials += 1

            if trials == 3:
                print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")

if __name__ == "__main__":
    main()
