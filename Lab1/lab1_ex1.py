day = int(input("Enter the days : "))

if day > 0:
    year = day // 365
    month = (day % 365) // 30
    day = (day % 365) % 30
    print(f"Year : {int(year)}")
    print(f"Month : {int(month)}")
    print(f"Day : {int(day)}")
else:
    print("Please enter a valid number of days.")
