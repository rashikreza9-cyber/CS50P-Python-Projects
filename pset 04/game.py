while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
        
        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
