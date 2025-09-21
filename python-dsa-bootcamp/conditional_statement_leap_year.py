year = int(input("Enter the Year"))

if year > 0:
    if year % 4 == 0:
        print(year, "The number is a Leap Year")
    else:
        print(year, "The number is not a Leap Year")
else:
    print(year, "Year can't be Negative or Zero")