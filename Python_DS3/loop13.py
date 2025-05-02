num = [11, 21, 27, 32, 35, 42, 46, 49, 56, 70, 777]

for i in num:
    if i > 500:
        break
    if i % 7 == 0:
        if i > 50:
            continue
        print(i)