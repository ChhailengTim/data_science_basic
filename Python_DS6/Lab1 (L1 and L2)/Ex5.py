num1, num2, num3 = eval(input('Enter three integers: '))

if num1 > num2:
    num1, num2 = num2, num1

if num1 > num3:
    num1, num3 = num3, num1

if num2 > num3:
    num2, num3 = num3, num2

print('The numbers are:', num1, num2, num3) 