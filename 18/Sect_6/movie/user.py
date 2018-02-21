from movie import Movie
class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def add_movie(self, name, genre, year):
        self.movies.append(Movie(name, genre, year, False))

    def delete_movie(self, name):
        self.movies = list(filter(lambda x : x.name != name, self.movies))
        #self.movies.remove(filter(lambda x: x == name, self.movies))

    def watched_movies(self):
        watched_movies = list(filter(lambda x: x.watched, self.movies))
        return watched_movies

    def save_user_to_file(self):
        with open("{}.txt".format(self.name), 'w') as f:
            f.write(self.name + "\n")
            for movie in self.movies:
                f.write("{}, {}, {}, {} \n".format(movie.name, movie.genre, str(movie.year), str(movie.watched)))

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as f:
            content = f.readlines()
            #f.readlines() returns a list
            username = content[0]
            movies = []
            for line in content[1:]:
                movie_data = line.split(", ")
                movies.append(Movie(movie_data[0], movie_data[1], movie_data[2], movie_data[3] == "True"))

            user = cls(username)
            user.movies = movies
            return user

