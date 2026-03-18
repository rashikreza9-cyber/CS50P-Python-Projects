def main():
    # Dictionary to store grocery items and their counts
    groceries = {}

    while True:
        try:
            # Get user input and convert to uppercase for case-insensitivity
            item = input().upper()

            # Check if item is already in the dictionary
            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1

        except EOFError:
            # Break the loop when Ctrl+D is pressed
            break
        except ValueError:
            # Handle potential ValueErrors, though not strictly required by problem spec
            pass

    # Sort the dictionary keys alphabetically
    # The sorted() function returns a list of sorted keys
    for item in sorted(groceries.keys()):
        # Print the count and the item name
        print(groceries[item], item)

if __name__ == "__main__":
    main()
