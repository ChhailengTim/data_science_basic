def print_alternate_pattern(rows):
    num = 1
    for i in range(1, rows +1):
        if i % 2 != 0:
            for x in range(num, num + i):
                print(x, end=" ")
            print()
        else:
            for y in range(num + i - 1, num - 1, -1):
                print(y, end=" ")
            print()
        num += i

print_alternate_pattern(5)