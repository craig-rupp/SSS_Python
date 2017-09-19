class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

    # def friend(self, friend_name):
    #     ##return a new student called 'friend_name' in same school as self
    #     return Student(friend_name, self.school)
    @classmethod
    def friend(cls, origin, friend_name, *args):
        return cls(friend_name, origin.school, *args) #multiple args being passed


class WorkingStudent(Student):
    def __init__(self, name, school, salary, profession):
        super().__init__(name, school)
        self.salary = salary
        self.profession = profession

teddy = WorkingStudent('Teddy', 'Oxford', 800, 'Gardener')
print(teddy.school)
teddy_friend = WorkingStudent.friend(teddy, 'Eric', 750, 'Potter')
print(teddy_friend.name)
print(teddy_friend.salary)
print(teddy.profession)
