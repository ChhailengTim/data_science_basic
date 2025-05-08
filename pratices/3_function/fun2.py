def func1(*args):
    for i in args:
        print(i)


value1 = func1(20, 40, 60)
print(value1)  # (20, 40, 60)
value1 = func1(80, 100)
print(value1)  # (80, 100, None)