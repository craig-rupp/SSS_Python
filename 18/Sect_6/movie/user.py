from movie import Movie
class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def trim_movie(self, film_name):
        if ' ' in film_name:
            film_name.strip()
            if ' ' in film_name:
               return " ".join(film_name.split())
            else:
                return film_name
        else:
            return film_name

    def add_movie(self, name, genre, year):
        self.movies.append(Movie(name, genre, year, False))

    def delete_movie(self, name):
        self.movies = list(filter(lambda x : x.name != name, self.movies))
        #self.movies.remove(filter(lambda x: x == name, self.movies))

    def watched_movies(self):
        watched_movies = list(filter(lambda x: x.watched, self.movies))
        return watched_movies

    def set_watched(self, name):
        for movie in self.movies:
            if movie.name == name:
                movie.watched == True

    def json(self):
        return {
            'name' : self.name,
            'movies' : [
                movie.json() for movie in self.movies
            ]
        }

    @classmethod
    def from_json(cls, json_data):
        #use arg to create user & movies, put movies in user object and return user
        movies = []
        for movie_data in json_data["movies"]:
            movies.append(Movie.to_json(movie_data))
            #movies.append(Movie(movie["name"], movie["genre"], movie["year"], movie["watched"]))
        user = cls(json_data["name"])
        user.movies = movies
        return user