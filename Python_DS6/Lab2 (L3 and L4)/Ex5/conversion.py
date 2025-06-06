

def temperature_conversion(val, type):
    if type == '1':
        res = (9.0 / 5.0) * val + 32
    elif type == '2':
        res = (5.0 / 9) * (val - 32) 
    else:
        res = None
        print('Invalid conversion type. Expected type value is 1 or 2')
    
    return res