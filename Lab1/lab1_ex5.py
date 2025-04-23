num1, num2, num3 = eval(input("Enter three integer: "))
# if num1 <= num2 <= num3:
#     print("The sorted number are:", [num1, num2, num3])
# elif num1 <= num3 <= num2:
#     print("The sorted number are:", [num1, num3, num2])
# elif num2 <= num1 <= num3:
#     print("The sorted number are:", [num2, num1, num3])
# elif num2 <= num3 <= num1:
#     print("The sorted number are:", [num2, num3, num1])
# elif num3 <= num1 <= num2:
#     print("The sorted number are:", [num3, num1, num2])
# else:
#     print("The sorted number are:", [num3, num2, num1])
sorted_numbers = sorted([num1, num2, num3])
print("The sorted number are:", sorted_numbers)

    