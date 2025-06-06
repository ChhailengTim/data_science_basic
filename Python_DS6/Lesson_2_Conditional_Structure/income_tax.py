


annual_income = eval(input('Enter your annual income: $'))

if annual_income <= 10000:
    tax = 0
elif annual_income <= 20000:
    tax = (annual_income - 10000)* 0.1
elif annual_income <= 50000:
    tax = ((annual_income - 20000) * 0.2) + 1000
else:
    tax = ((annual_income - 50000) * 0.3) + 7000

print('Your income tax is: $', tax)