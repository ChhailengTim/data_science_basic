def arithmetic_operation(val1, val2, operation_name):
    """
    Perform arithmetic operations based on the operation name.

    :param val1: First value
    :param val2: Second value
    :param operation_name: Name of the operation ('add', 'subtract', 'multiply', 'divide')
    :return: Result of the arithmetic operation
    """
    if operation_name == 'add':
        return val1 + val2
    elif operation_name == 'subtract':
        return val1 - val2
    elif operation_name == 'multiply':
        return val1 * val2
    elif operation_name == 'divide':
        if val2 != 0:
            return val1 / val2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation name.")
