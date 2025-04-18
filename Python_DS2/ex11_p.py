income = eval(input("Enter your annual income: $"))
if income <= 10000:
    tax = income * 0/100
    print("Your income tax is: $", tax)
elif income <= 20000:
    tax_on = income - 10000
    tax = tax_on * 10/100
    print("Your income tax is: $", tax)
elif income <= 50000:
    tax_on = income - 20000
    tax = (tax_on * 20/100) + 1000
    print("Your income tax is: $", tax)
else:
    tax_on = income - 50000
    tax = (tax_on * 30/100) + 7000
    print("Your income tax is: $", tax)
