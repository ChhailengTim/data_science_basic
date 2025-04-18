purchase = eval(input("Enter the total amount of purchase amount: $"))

if purchase > 100:
    discount = purchase * 10 / 100
    print(f"Customer is eligible for 10% discount")
    print("The discount is: $", discount)
    final_discount = purchase - discount
    print("The final amount after discount is: $", final_discount)
elif purchase <= 100:
    discount = purchase * 5 / 100
    print(f"Customer is eligible for 5% discount")
    print("The discount is: $", discount)
    final_discount = purchase - discount
    print("The final amount after discount is: $", final_discount)

