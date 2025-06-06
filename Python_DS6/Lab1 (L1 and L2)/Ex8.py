
exchange_rate = eval(input('Enter the exchange rate from dollars to RMB: '))
exchange_type = input('Enter 0 to convert from dollar to RMB and 1 vice versa: ')

if exchange_type == '0':
    balance = eval(input('Enter the dollar amount: '))
    res = balance * exchange_rate

    print('$', balance, 'is', res, 'yuan.')

elif exchange_type == '1':
    balance = eval(input('Enter the yuan amount: '))
    res = balance / exchange_rate

    print(balance, 'yuan is $', format(res,'.2f'))

else:
    print('Invalid input.')    

