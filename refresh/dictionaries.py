my_set = {1, 2, 3}
print(my_set)
example = {'name' : 'Oscar', 'age': 27, 'grades' : [85, 74, 91]}
lottery_player = {
    'name' : 'Rolf',
    'numbers' : (13, 26, 18, 19)
}
universities = [
    {
        'name' : 'University of Texas at Austin',
        'location' : 'Austin, TX'
    },
    {
        'name' : 'Kingsman Academy',
        'location' : 'Stratford Upon England'
    }
]
for university in universities:
    print(university)

two_levels = {
    'defense' : {
        'CentreBack' : 'Koscielny',
        'WingBack' : 'Bellerin',
        'LWB' : 'Kolasinac'
    },
    'midfield' : {
        'HoldingMF': 'Xhaka',
        'BoxToBox' : 'Ramsey',
        'AttackingMf' : 'Ozil'
    },
    'attack' : {
        'RF' : 'Welbeck',
        'CF' : 'Lacazette',
        'LF' : 'Sanchez'
    }
}
print(two_levels['defense']['WingBack'])
print(sum(lottery_player['numbers'])/ len(lottery_player['numbers']))

#Coding Ex (Lessong #23)
# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {
    'name' : 'Jose',
    'school' : 'Computing',
    'grades' : (66, 77, 88)
}

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades =   data['grades']# Change this!
    return sum(grades) / len(grades)


# Implement the function below
# Given a list of students (dictionaries), calculate the average grade of the class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        # Implement here
        total += sum(student['grades'])
        count += len(student['grades'])
    return total / count
