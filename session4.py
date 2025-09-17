def average_score(scores):
    i = 0
    val = 0
    for score in scores:
        val += score
        i += 1

    return val / i

def make_student(name, scores):
    av = average_score(scores)
    dic = { "student_name" : name, "student_scores" : scores, "average_score" : av }
    return dic


def class_summary(students):
    top_student = students[0]
    for student in students:
        if student["average_score"] > top_student["average_score"]:
            top_student = student

    return top_student


s1 = make_student("Holla", [98, 50, 88, 55, 73])
s2 = make_student("Toto", [8, 90, 57, 55, 98, 30])
s3 = make_student("Mark", [99, 100, 45, 70, 79])
s4 = make_student("Lala", [99, 99, 45, 50, 38])

students_list = [s1, s2, s3]

class_summary(students_list)