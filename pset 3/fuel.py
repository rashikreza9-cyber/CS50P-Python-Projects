while True:
    try:
        fuel = (input("Fraction(x/y): "))
        x,y = map(int, fuel.split('/'))
        if x>y or x<0:
            continue
        percentage = round((x/y)*100)
        if percentage>=99: print("F")
        elif percentage<=1: print("E")
        else:
         print(f"{percentage}%")
        break
    except(ValueError, ZeroDivisionError):
         pass
