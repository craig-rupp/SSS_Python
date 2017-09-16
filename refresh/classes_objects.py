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
    def go_to_school(self):
        print("I'm going to {}".format(self.school))
    @classmethod
    def am_a_student(cls):
        print("I am a student")
    @staticmethod
    def human():
        print("I'm of this world")

craig = Student('Craig', 'UT')
print(craig.name + ', went to ' + craig.school)
craig.grades.extend((75, 89, 91))
print(craig.grade_average())
craig.go_to_school()
Student.am_a_student()
Student.human()

#Exercise #26
# class Store:
#     def __init__(self, name):
#         self.name = name
#         self.items = []
#
#     def add_item(self, name, price):
#         # Create a dictionary with keys name and price, and append that to self.items.
#         item_dictionary = {
#             'name' : name,
#             'price' : price
#         }
#         self.items.append(item_dictionary)
#
#     def add_items(self, items):
#         self.items.extend(items)
#         print(self.items)
#
#     def stock_price(self):
#     # Add together all item prices in self.items and return the total.
#         print(sum([item['price'] for item in self.items]))
#
# test_store = Store('Albertsons')
# #test_store.add_item('Face-Wash', 5)
# items = [
#     {
#         'name' : 'Cerveza',
#         'price' : 25
#     },
#     {
#         'name' : 'Tecate',
#         'price' : 18
#     }
# ]
# test_store.add_items(items)
# test_store.stock_price()

#Exercise #27
#Class / Static Method
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        #return cls(store.name + " -- franchise")
        new_store = cls(store.name)
        print(new_store)
        #using class instead of Store (object Name)
    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        print('{}, total stock price: {}'.format(store.name.upper(), int(store.stock_price())))


store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

Store.franchise(store)  # returns a Store with name "Test - franchise"
Store.franchise(store2)  # returns a Store with name "Amazon - franchise"

Store.store_details(store)  # returns "Test, total stock price: 0"
Store.store_details(store2)  # returns "Amazon, total stock price: 160"