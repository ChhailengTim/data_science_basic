from conversion import *

val = eval(input("Enter the temperature value: "))
type = input("Enter the conversion type (1 for C to F, 2 for F to C): ")
result = temperateure_conversion(val, type)
print("The result is:", result)