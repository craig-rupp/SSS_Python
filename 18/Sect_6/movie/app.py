from user import User

# user = User("Craig")
# user.add_movie("Black Panther", "Sci-Fi", 2018)
# user.add_movie("Jumanji", "Comedy", 2018)
# user.save_user_to_file()
user = User.load_from_file("Craig.txt")
print(user.name)
print(user.movies)
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
foo_3 = list(filter(lambda x: x % 3 == 0, foo))
print(foo_3)