
def arithmetic_operation(val1, val2, operation_name):
    if operation_name == 'Addition':
        return val1 + val2
    elif operation_name == 'Subtraction':
        return val1 - val2
    elif operation_name == 'Multiplication':
        return val1 * val2
    elif operation_name == 'Division':
        return val1 / val2
    else:
        print('Invalid conversion type. Expected type value is \
            "Addition", "Subtraction", "Multiplication", or "Division"')
         