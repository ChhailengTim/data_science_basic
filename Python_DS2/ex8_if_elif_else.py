weight = eval(input("Enter your weight in kg: "))
height = eval(input("Enter your height in meters (m): "))
bmi = weight / (height * height)

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:  
    print("You are obese.")