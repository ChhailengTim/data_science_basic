num = eval(input("Enter a number : "))

divide_by_5 = (num % 5 == 0)
divide_by_6 = (num % 6 == 0)

both = divide_by_5 and divide_by_6
either = divide_by_5 or divide_by_6
only_one = divide_by_5 != divide_by_6

# Print the results
print(f"Is {num} divisible by 5 and 6? {both}")
print(f"Is {num} divisible by 5 or 6? {either}")
print(f"Is {num} divisible by 5 or 6, but not both? {only_one}")
