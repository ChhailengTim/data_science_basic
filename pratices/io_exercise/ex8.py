totalMoney = 1000
quantity = 3
price = 450

statement = f"I have {totalMoney} dollars, I bought {quantity} items for {price} dollars each." 
print(statement.format(quantity, totalMoney, price))