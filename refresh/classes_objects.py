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

#Exercise #26
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item_dictionary = {
            'name' : name,
            'price' : price
        }
        self.items.append(item_dictionary)

    def add_items(self, items):
        self.items.extend(items)
        print(self.items)

    def stock_price(self):
    # Add together all item prices in self.items and return the total.
        print(sum([item['price'] for item in self.items]))

test_store = Store('Albertsons')
#test_store.add_item('Face-Wash', 5)
items = [
    {
        'name' : 'Cerveza',
        'price' : 25
    },
    {
        'name' : 'Tecate',
        'price' : 18
    }
]
test_store.add_items(items)
test_store.stock_price()
