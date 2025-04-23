balance, annual_interest_rate = eval(input("Enter the balance and annual interest rate: "))

if balance > 0 and annual_interest_rate > 0:
    monthly_interest = balance * annual_interest_rate / 1200
    print(f"The interest is: {monthly_interest:}")
else:  
    print("Please enter valid values for balance and annual interest rate.")