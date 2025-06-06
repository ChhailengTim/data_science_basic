
from arithmetic import *

while True:
    val1 = eval(input('Enter the first number: '))
    val2 = eval(input('Enter the second number: '))
    operation_name = input('Enter the operation name (Addition, Subtraction, Multiplication, Division): ')

    res = arithmetic_operation(val1, val2, operation_name)

    print('The result is:', res)