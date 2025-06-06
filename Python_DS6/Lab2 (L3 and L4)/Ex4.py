'''

6 % 2 = 0
3 % 2 = 1
1 % 2 = 1
0

Binary of 6 is 110

'''

num = eval(input("Enter an integer: "))

binary_num = ""
value = num

while value != 0:
    res = str(value % 2)
    value = value // 2

    binary_num = res + binary_num

print(num, '\'s binary representation is', binary_num)
    
    
