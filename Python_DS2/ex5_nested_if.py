age = eval(input("Enter your age: "))
has_id = True

if age >= 18:
    if has_id:
        print("You can enter the club.")
    else:
        print("You need to show your ID.")
else:
    print("You are too young to enter the club.")