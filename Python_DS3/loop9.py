sum = 0
number = 0
while number < 10:
    number += 1
    if number == 5 or number == 6:
        continue
    sum += number
print("The sum is: ", sum)