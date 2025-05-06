def find_largest(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest


res1 = find_largest(5, 10, 3)
print(res1)
res2 = find_largest(-4, -1, -7)
print(res2)
res3 = find_largest(8, 8, 2)
print(res3)
