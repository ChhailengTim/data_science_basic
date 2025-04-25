num1, num2, num3 = eval(input("Enter three integer: "))

# small to large
if num1 > num2:
    num1, num2 = num2, num1
if num1 > num3:
    num1, num3 = num3, num1
if num2 > num3:
    num2, num3 = num3, num2

# large to small
# if num1 < num2:
#     num1, num2 = num2, num1
# if num1 < num3:
#     num1, num3 = num3, num1
# if num2 < num3:
#     num2, num3 = num3, num2

print(f"The numbers in ascending order are: {num1}, {num2}, {num3}")
# The numbers are now sorted in ascending order
# sorted_numbers = sorted([num1, num2, num3])
# print("The sorted number are:", sorted_numbers)
