class Movie:
    def __init__(self, name, genre, year, watched):
        self.name = name
        self.genre = genre
        self.year = year
        self.watched = watched
        print("You have created, {}, a {} - type film, made in {}".format(name, genre, year))
    def __repr__(self):
        return f"Movie(s) : {self.name}"