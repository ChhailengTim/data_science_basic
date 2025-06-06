

price = eval(input('Enter the total amount of purchase: $'))

if price > 100:
    discount_price = price * 0.90
else:
    discount_price = price * 0.95
print('Final amount after discount: $', discount_price)
