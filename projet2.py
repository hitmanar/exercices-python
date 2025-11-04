top_student_name = ""
highest_average = 0

students = [
    {"name":"Alice", "grades":[85,90,92]},
    {"name":"Bryan", "grades":[30,20,10]},
    {"name": "Arush", "grades": [50, 80, 30]}

]
for student in students:
 average = sum(student["grades"])/ len(student["grades"])

 student["average_grade"] = average
 print(students)

 if student["average_grade"] > highest_average:
     highest_average = student["average_grade"]
     top_student_name = student["name"]

print(f"le meilleir etudiant est {top_student_name} avec une moyenne de {highest_average}")