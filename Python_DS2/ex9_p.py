num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == "+":
    result = num1 + num2
    print("The result is:", result)
elif operation == "-":
    result = num1 - num2
    print("The result is:", result)
elif operation == "*":
    result = num1 * num2
    print("The result is:", result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("The result is:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation entered.")
