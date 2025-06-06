


num = [5, -3, 8, -1, 10]

sum_num = 0
for i in num:
    if i < 0:
        continue
    sum_num = sum_num + i

print('The sum of positive numbers is', sum_num)