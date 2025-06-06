

investment_amount = eval(input('Enter investment amount: '))
annual_interest_rate = eval(input('Enter annual interest rate: '))
years = eval(input('Enter number of years: '))

#Convert user's input interest rate to percentage
rate_percentage = annual_interest_rate/100 

#Convert annual interest rate to monthly interest rate
monthly_interest_rate = rate_percentage / 12

#Convert years to months
months = years * 12

#Calculate the total amount (Investment amount + interest)
futureInvestmentAmount = investment_amount * (1+ monthly_interest_rate) ** months

#Print the result message
print('Accumulated value is', format(futureInvestmentAmount,'.2f'))