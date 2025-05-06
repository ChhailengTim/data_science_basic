num_students = int(input("Enter the number of students: "))
students = []
scores = []

for i in range(num_students):
    name = input(f"Enter the name of student {i + 1}: ")
    score = float(input(f"Enter the score of student {i + 1}: "))
    students.append(name)
    scores.append(score)

max_score = max(scores)
top_students = []

for i in range(len(scores)):
    if scores[i] == max_score:
        top_students.append(students[i])

print(f"Top score is {max_score}")
print("Top students:")
for s in top_students:
    print(s)
