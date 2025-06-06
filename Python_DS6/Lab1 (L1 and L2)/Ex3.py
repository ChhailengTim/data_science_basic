#interest = balance * (annualInterestRate / 1200) 

balance, interest_rate = eval(input('Enter your balance and interest rate: ')) 

interest = balance * (interest_rate/1200)

print('The interest is', format(interest, '.4f'))