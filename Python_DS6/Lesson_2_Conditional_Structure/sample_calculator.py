




x1 = eval(input('Enter the first number: '))
x2 = eval(input('Enter the second number: '))
operator = input('Enter an operation (+, -, *, /): ')

if operator == '+':
    res = x1 + x2
    print('The result is', res)
elif operator == '-':
    res = x1 - x2
    print('The result is', res)
elif operator == '*':
    res = x1 * x2
    print('The result is', res)
elif operator == '/':
    res = x1 / x2
    print('The result is', res)
else:
    print('Error: Invalid operation entered')


