saving_amount = eval(input("Enter the amount to be saved: "))
annual_interest_rate = 0.00417

if saving_amount > 0:
    interest = (1+annual_interest_rate)
    amount_1 = (saving_amount * interest)
    amount_2 = amount_1 * interest
    amount_3 = amount_2 * interest          
    amount_4 = amount_3 * interest
    amount_5 = amount_4 * interest
    amount_6 = amount_5 * interest
    amout = amount_1 + amount_2 + amount_3 + amount_4 + amount_5 + amount_6
    print(f'The amount of money in the account after 6 months is: {amout:.2f}')
