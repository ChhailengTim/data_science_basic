def series_sum(start, end):
    sum = 0
    for i in range(start, end, 2):
        sum = i/(i+2) + sum
    return sum


res1 = series_sum(1, 98)
print(res1)
