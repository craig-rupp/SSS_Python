student_list = []
def create_student():
    student_name = input("What's the student's name? : ")
    student_dictionary = {
        "name" : student_name,
        "marks" : []
    }
    student_list.append(student_dictionary)
    another = input("Would you like to add another student? : [Y/N]?").lower()
    if another == 'y':
        create_student()
    return student_list

def add_grades(students):
    for student in students:
        print(student['name'])
        grades = input("Please enter the grades for : {}, separated by a comma : ".format(student["name"]))
        grades = grades.split(",")
        for grade in grades:
            student["marks"].append(float(grade))
    student_list = students
    return student_list

def confirm(dict):
    for individual_student in dict:
        name = individual_student["name"]
        grades = individual_student["marks"]
        answer = ""
        while answer not in ["y", "n"]:
            answer = input("Confirm grades : " + str(grades) + ", for " + name + " : [Y/N]").lower()
        if answer == "y":
            print("You have confirmed grades : " + str(grades) + " for " + name)
            average = input("Would you like to have an average of the student's grades? : [Y/N]").lower()
        if average == "y":
            print(individual_student)
            calculate_student_average(individual_student)
        elif answer != "y":
            individual_student["marks"] = []
            print(name + ", has had their grades removed")

def calculate_student_average(student):
    # calculate average, set new key in dictionary for average, print out student
    student_average = sum(student["marks"])/len(student["marks"])
    student['average'] = student_average
    print(student)

def menu():
    #student list for all students, grades per student, print list, exit
    print(create_student())
    print(add_grades(student_list))
    confirm(student_list)


menu()

#add_grades(create_student())
