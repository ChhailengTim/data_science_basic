numbers = [5, -3, 8, -1, 10]
sum = 0

for i in numbers:
    if i < 0:
        continue
    sum += i
print("The sum of positive numbers: ", sum)
