num = eval(input("Enter a number: "))
sum = 0
for i in range(1, num+1, 1):
    sum += i
print("The sum of the first", num, "numbers is:", sum)
