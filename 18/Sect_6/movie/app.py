from user import User
import json
import os

user = User("Craig")
user.add_movie("Black Panther", "Sci-Fi", 2018)
user.add_movie("Jumanji", "Comedy", 2018)
user.add_movie("I, Tonya", "Dramedy", 2017)
print(user.trim_movie("Black  Panther "))
print(user.trim_movie(" Titanic"))
# with open('my_file.txt', 'w') as f:
#     json.dump(user.json(), f)
#
# with open('my_file.txt', 'r') as f:
#     json_data = json.load(f)
#     user = User.from_json(json_data)
#     print(user.json())
#
# foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
# foo_3 = list(filter(lambda x: x % 3 == 0, foo))
# #print(foo_3)
def menu():
    name = input("Please enter your name : ")
    filename = "{}.txt".format(name)
    if file_exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user = User(name)

    user_input = input("Enter 'a' to add a movie, 's' to see the list of movies, 'w' to set a movie as watched,"
          "'d' to delete a movie, 'l' to see list of watched movies,"
          "or 'f' to save, and 'q' to quit")
    while user_input != 'q':
        if user_input == 'a':
            movie_name = user.trim_movie(input("Please enter the name of the film : "))
            movie_genre = user.trim_movie(input("Please enter the genre of the film : "))
            movie_year = int(input("Please enter the year the film was made : "))
            user.add_movie(movie_name, movie_genre, movie_year)
        elif user_input == 's':
            for movie in user.movies:
                print("{}, a {} film made in {}, Watched : {}".format(movie.name, movie.genre, str(movie.year), str(movie.watched)))
        elif user_input == 'w':
            user_movie = input("Please enter the name of the film you would like to set as watched : ")
            user.set_watched(user.trim_movie(user_movie))
        elif user_input == 'd':
            movie_name = input("Enter the name of the movie to delete : ")
            user.delete_movie(user.trim_movie(movie_name))
        elif user_input == 'l':
            for movie in user.watched_movies():
                print("{}, a {} film made in {}, Watched : {}".format(movie.name, movie.genre, str(movie.year),
                str(movie.watched)))
        elif user_input == 'f':
            with open(filename, 'w') as f:
                json.dump(user.json(), f)
        user_input = input("Enter 'a' to add a movie, 's' to see the list of movies, 'w' to set a movie as watched,"
                           "'d' to delete a movie, 'l' to see list of watched movies,"
                           "or 'f' to save, and 'q' to quit")


def file_exists(filename):
    return os.path.isfile(filename)

menu()