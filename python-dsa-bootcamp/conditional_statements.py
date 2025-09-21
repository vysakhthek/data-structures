num = int(input("Enter the Number"))

if num > 0:
    print("Number is Positive")
    if num % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")
else:
    print("Number is Zero or Negative")