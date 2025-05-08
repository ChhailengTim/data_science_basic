def outer_func(a,b):
    square = a ** 2

    def addition(a,b):
        return a + b
    
    add = addition(a,b)
    return add + 5


res = outer_func(5, 10)
print(res)
