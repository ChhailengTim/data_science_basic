num = eval(input("Enter a number : "))

if num / 5 == 0 and num / 6 == 0:
    print(True)
elif num / 5 == 0 or num / 6 == 0:  
    print(True)
else:
    print(False)