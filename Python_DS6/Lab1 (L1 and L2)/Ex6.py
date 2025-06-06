num = eval(input('Enter an integer between 0 and 999: '))
#932

#2 = 932 % 10
#93 = 932 // 10
#3 = 93 % 10
#9 = 93 // 10

num1 = num % 10
print('num1 = ', num1)
remaining_digit = num // 10
num2 = remaining_digit % 10
print('num2 = ', num2)
num3 = remaining_digit // 10
print('num3 = ', num3)

res = num1 + num2 + num3
print('The sum of the digits is', res)
