investment_amount = eval(input("Enter the amount to be invested: "))
annual_interest_rate = eval(input("Enter the annual interest rate: "))
number_of_years = eval(input("Enter the number of years: "))

if investment_amount > 0 and annual_interest_rate > 0 and number_of_years > 0:
    monthly_interest_rate = annual_interest_rate / 1200
    number_of_months = number_of_years * 12
    future_value = investment_amount * \
        (1 + monthly_interest_rate) ** number_of_months
    print(f"Accumulated value is: {future_value:.2f}")
else:
    print("Please enter valid values for investment amount, annual interest rate, and number of years.")
