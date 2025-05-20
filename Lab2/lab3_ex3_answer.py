stu_numbers = int(input("Enter the number of students: "))
name = input("Enter the name of students: ")
score = eval(input("Enter the score of students: "))

for i in range(1, stu_numbers):
    name1 = input("Enter the name of students: ")
    score1 = eval(input("Enter the score of students: "))

    if score1 > score:
        name = name1
        score = score1

print("Top stuedent is", name, "with score", score)
