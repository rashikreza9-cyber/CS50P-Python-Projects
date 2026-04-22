import inflect
import sys

def main():
    p = inflect.engine()
    names = []

    # Continuously prompt for names until Ctrl-D
    while True:
        try:
            # Important: Use an empty input() or no prompt text 
            # to avoid check50 errors related to extra output
            name = input("Name: ")
            names.append(name)
        except EOFError:
            # Print a newline to move past the EOF signal
            print()
            break

    # Join names into a grammatically correct string
    if names:
        farewell = p.join(names)
        print(f"Adieu, adieu, to {farewell}")

if __name__ == "__main__":
    main()
