from arithmetic import arithmetic_operation


def main():
    # Example usage of the arithmetic_operation function
    val1 = 4
    val2 = 2

    print("Addition:", arithmetic_operation(val1, val2, 'add'))
    print("Subtraction:", arithmetic_operation(val1, val2, 'subtract'))
    print("Multiplication:", arithmetic_operation(val1, val2, 'multiply'))
    print("Division:", arithmetic_operation(val1, val2, 'divide'))


print(main())
