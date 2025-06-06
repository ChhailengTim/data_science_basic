

def increment(n):
    n = n + 1
    print('\tn inside the function is', n)
    return n

x = 1
print('Before the call, x is ', x)
x = increment(x)
print('After the call, x is', x)