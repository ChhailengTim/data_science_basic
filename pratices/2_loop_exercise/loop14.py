num = 76542
reversed = 0

while num > 0:
    digit = num % 10
    print("The digit is:", digit)
    reversed = reversed * 10 + digit
    num = num // 10
print("The reversed number is:", reversed)
