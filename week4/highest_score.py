
number_of_students = int(input("\nEnter the number of students:"))

current_student = ("Nobody", 0)

first_highest = [current_student]
second_highest = [current_student]

while number_of_students > 0:
    name = input("\nEnter student's name: ")
    score = input("\nEnter student's score: ")

    if not name:
        break

    current_student = (name, int(score))
    score = current_student[1]

    first_score = first_highest[0][1]
    second_score = second_highest[0][1]

    if score > first_score:
        second_highest = first_highest
        first_highest = [current_student]

    elif score == first_score:
        first_highest.append(current_student)

    elif score == second_score:
        second_highest.append(current_student)

    number_of_students-=1


print("\n")
print("Top scores:")
for students in first_highest:
    print(students[0], students[1], end=" ")
print("\n")
for students in second_highest:
    print(students[0], students[1], end=" ")
print("\n")



