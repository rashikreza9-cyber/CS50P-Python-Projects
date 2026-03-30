months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
while True:
    date = input("Date: ").strip()
    if "/" in date :
        try:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
            if month<=12 and day<=31:
                print(f"{year}-{month:02}-{day:02}")
                break
            else:
                continue
        except ValueError:
            pass
    elif "," in date:
        try:
            month_day, year2 = date.split(",")
            month2, day2 = month_day.split(" ")
            month2 = months.index(month2) + 1
            day2 = int(day2)
            year2 = int(year2)
            if month2 <= 12 and day2 <=31:
                print(f"{year}-{month:02}-{day:02}")
                break
            else:
                continue
        except ValueError:
            pass
    else:
        continue
