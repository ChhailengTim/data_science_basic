weight1, price1 = eval(input('Enter the weight and price of Package 1: '))
weight2, price2 = eval(input('Enter the weight and price of Package 2: '))

unit_price1 = price1 / weight1
unitprice2 = price2 / weight2

if unit_price1 > unitprice2:
    print('Package 2 has better price.') 
elif unit_price2 > unitprice1:
    print('Package 1 has better price.')
else:
    print('Both package has the same price.')