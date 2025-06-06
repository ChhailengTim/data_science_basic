

from conversion import *

val = eval(input('Enter the temperature value: '))
type = input('Enter the conversion type (1: Celsius to Fahrenheit and 2: Vice versa): ')

res = temperature_conversion(val, type)

print('The result is', res)