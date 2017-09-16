loterry_player_dict = {
    'name' : 'Rolf',
    'scores' : (17, 13, 21, 17, 18)
}
class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.scores = (17, 13, 21, 17, 18)
    def total(self):
        return(sum(self.scores))

player = LotteryPlayer('Craig')
print(player.name)
print(player.total())

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grades = []
    def grade_average(self):
        return(sum(self.grades) / len(self.grades))

craig = Student('Craig', 'UT')
print(craig.name + ', went to ' + craig.school)
craig.grades.extend((75, 89, 91))
print(craig.grade_average())