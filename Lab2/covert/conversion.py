def temperateure_conversion(val, type):
    if type == "1":
        result = (9.0 / 5.0) * val + 32
    elif type == "2":
        result = (5.0 / 9.0) * (val - 32)
    else:
        result = None
        print("Invalid conversion type. Expected type value is 1 or 2")

    return result
