import os

from movie_test.user import User
import json
#user = User("Colleen")


#user.add_movie("West Side Story", "Drama")

#user.save_to_file()

# newUser = User.load_from_file('Craig.txt')
#
# print(newUser.name)
# print(newUser.movies)

# user = User('Craig')
# user.add_movie("The Witch", "Horror")
# user.add_movie("The Iron Giant", "Kids")
# #print(user)
# print(user.json())
# with open('Craig.txt', 'w') as f:
#         json.dump(user.json(), f)

# with open('Craig.txt', 'r') as f:
#     json_data = json.load(f)
#     user = User.from_json(json_data)
#     print(user.json())
def menu():
    #ask for user name
    user_name = str(input("Please enter your name: "))
    #check if file exists for user
    filename = "{}.txt".format(user_name)
    if file_exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user = User(user_name)

    user_input = input("Enter an 'a' to add a movie, 's' to see a list of movies, "
                       "'w' to set a movie as watched, 'd' to delete a movie, 'l' to see a list of watched movies,"
                       " or 'v' to save and 'q' to quit : ")
    while user_input != 'q':
        if user_input == 'a':
            movie_name = input("Enter your movie name : ")
            movie_genre = input("Enter your movie's genre: ")
            user.add_movie(movie_name, movie_genre)
        elif user_input == 's':
            if len(user.movies) < 1:
                print("There are curretly no films to display, please type 'a' if you would like to add to your list!")
            elif len(user.movies) >= 1:
                for movie in user.movies:
                    print("Name : {} , Genre : {} , Watched : {} ". format(movie.name, movie.genre, movie.watched))
        elif user_input == 'w':
            for movie in user.movies:
                print("Name : {} , Genre : {} , Watched : {} ". format(movie.name, movie.genre, movie.watched))
            movie_name = str(input("Enter the movie name you would like to set as watched : "))
            user.set_watched(movie_name)
        elif user_input == 'd':
            if len(user.movies) < 1:
                print("You must have one movie in your list in order to delete, please select 'a' to add to your list")
            elif len(user.movies) >= 1:
                print("See list below of your movies")
                for movie in user.movies:
                    print("Name : {} , Genre : {} , Watched : {} ". format(movie.name, movie.genre, movie.watched))
                movie_name = input("Enter the name of the movie you would like to delete: ")
                user.delete_movie(movie_name)
        elif user_input == 'l':
            for movie in user.watched_movies():
                print("Name : {} , Genre : {} , Watched : {} ". format(movie.name, movie.genre, movie.watched))
        elif user_input == 'v':
            with open(filename, 'w') as f:
                json.dump(user.json(), f)

        user_input = input("Enter an 'a' to add a movie, 's' to see a list of movies, "
                           "'w' to set a movie as watched, 'd' to delete a movie, 'l' to see a list of watched movies,"
                           " or 'v' to save and 'q' to quit : ")

def file_exists(filename):
    return os.path.isfile(filename)

menu()
