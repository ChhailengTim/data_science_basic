num = eval(input("Enter an integer: "))

if num % 5 == 0 and num % 6 == 0:
    print("Is 10 divisible by 5 and 6?", True)
    print("Is 10 divisible by 5 or 6?", True)
    print("Is 10 divisible by 5 or 6, but not both?", False)
elif num % 5 == 0 or num % 6 == 0:
    print("Is 10 divisible by 5 and 6?", False)
    print("Is 10 divisible by 5 or 6?", True)
    print("Is 10 divisible by 5 or 6, but not both?", True)
else:
    print("Is 10 divisible by 5 and 6?", False)
    print("Is 10 divisible by 5 or 6?", False)
    print("Is 10 divisible by 5 or 6, but not both?", False)
    
