try:
    numberator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    if denominator == 0:
        print("Error: Division by zero is not allowed.")
    else:
        percentage = (numberator / denominator) * 100
        print(f"The percentage is: {percentage:.2f}%")
except ValueError:
    print("Invalid input. Please enter a number.")