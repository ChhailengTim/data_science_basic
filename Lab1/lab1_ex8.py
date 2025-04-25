exchange_rate = eval(input("Enter the exchange rate: "))

convert_type = int(input("Enter 0 convert from U.S to RMB, 1 convert from RMB to U.S: "))

if convert_type == 0:
    amount = eval(input("Enter the amount in U.S: "))
    converted_amount = amount * exchange_rate
    print(f"{amount} U.S. dollars is {converted_amount} RMB.") 
elif convert_type == 1:
    amount = eval(input("Enter the amount in RMB: "))
    converted_amount = amount / exchange_rate
    print(f"{amount} RMB is {converted_amount:.2f} U.S. dollars.")
else:
    print("Incorrect input.")