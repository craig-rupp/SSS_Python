def create_student():
    student_name = input("What's the student's name? : ")
    student_dictionary = {
        "name" : student_name,
        "marks" : []
    }
    return student_dictionary

def add_grades(student):
    grades = input("Please enter the grades for your student, separated by a comma : ")
    grades = grades.split(",")
    for grade in grades:
        student["marks"].append(float(grade))
    print(student)
    confirm(student)

def confirm(dict):
    print(dict)
    name = dict["name"]
    grades = dict["marks"]
    answer = ""
    while answer not in ["y", "n"]:
        answer = input("Confirm grades : " + str(grades) + ", for " + name + " : [Y/N]").lower()
    if answer == "y":
        print("You have confirmed grades : " + str(grades) + " for " + name)
        return dict
    elif answer != "y":
        dict["marks"] = []
        print(name + ", has had their grades removed")
        print(dict)
        return dict



add_grades(create_student())
