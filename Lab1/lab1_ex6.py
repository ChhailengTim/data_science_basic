digits = eval(input("Enter a number between 0 and 1000: "))
if digits >= 0 and digits <= 1000:
    num1 = digits % 10
    num2 = digits // 10 % 10
    num3 = digits // 100
    sum_of_digits = num1 + num2 + num3
    print(f"The sum of the digits is: {sum_of_digits}")
else: 
    print("Please enter a valid number between 0 and 1000.")
