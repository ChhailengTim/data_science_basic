def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 :
        return 1
    else:
        return n * factorial_recursive(n - 1)
    
nubmer = 5
result = factorial_recursive(nubmer)
print(f"The factorial of {nubmer} is {result}.")