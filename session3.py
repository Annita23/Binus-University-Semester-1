students_list = [("John", 17, 88)]

classroom = {
    "students" : students_list
}


s2 = ("Coco", 21, 90)
s3 = ("Toto", 18, 78)
s4 = ("Tata", 18, 55)
s5 = ("Titi", 25, 85)
s6 = ("Mark", 20, 70)


classroom["students"].append(s2)
classroom["students"].append(s3)
classroom["students"].append(s4)
classroom["students"].append(s5)
classroom["students"].append(s6)

print("Adding student")
print("Classroom:", classroom)



print("Removing Tata")
classroom["students"].remove(s4)
print("Classroom:", classroom)

highest_grade = classroom["students"][0]
for i in classroom["students"]:
    for j in classroom["students"][i]:
        if j[2] > highest_grade[2]:
            highest_grade = classroom["students"][i]

print("Highest student grad is:", highest_grade)

print("Sort by grade")
classroom["students"].sort(key=lambda tup: tup[2])
print("Classroom: ", classroom)