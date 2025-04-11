a = eval(input("Enter a number: "))

if a % 2 == 0:
    print("a is even number")
    if a > 10:
        print("The number is even and greater than 10")
    else:
        print("The number is even and 10 or less")
else:
    print("a is odd number")
