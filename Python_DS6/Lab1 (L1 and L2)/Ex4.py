# 0.00417

balance = eval(input('Enter your balance: '))

month1 = balance * (1 + 0.00417)
month2 = (balance + month1) * (1 + 0.00417)
month3 = (balance + month2) * (1 + 0.00417)
month4 = (balance + month3) * (1 + 0.00417)
month5 = (balance + month4) * (1 + 0.00417)
month6 = (balance + month5) * (1 + 0.00417)

print('After sixth month, the account value is', format(month6, '.2f'))