# number of terms
num = 2
terms = 5

sum_sequence = 0

for i in range(0, terms):
    print(num, end=' + ')
    sum_sequence += num
    num = num * 10 + 2
print(" = ", sum_sequence)