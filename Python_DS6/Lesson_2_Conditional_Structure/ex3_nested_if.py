


age = eval(input('Enter your age: '))
has_id = False

if age >= 18:
    if has_id:
        print('You are eligible to enter.')
    else:
        print('You need an ID to enter.')
else:
    print('You are not old enough to enter.')