print("Find factorial of a number")
n = 5
factorial = 1

if n < 0:
    print("Factorial does not exist for negative numbers")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, n + 1):
        factorial *= i
    print("The factorial of", n, "is", factorial)