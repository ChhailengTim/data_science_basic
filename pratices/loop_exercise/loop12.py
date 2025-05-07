num1 = 0
num2 = 1

for i in range(0, 10):
    print(num1, end=" ")
    result = num1 + num2
    num1 = num2
    num2 = result
