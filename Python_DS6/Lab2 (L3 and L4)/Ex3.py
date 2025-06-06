

num_students = eval(input('Enter the number of students: '))

name = input('Enter a student name: ')
score = eval(input('Enter a student score: '))

for i in range(1, num_students):
    name1 = input('Enter a student name: ')
    score1 = eval(input('Enter a student score: '))

    if score1 > score : 
        name = name1
        score = score1

print('Top student', name, '\'s score is', score)
    
