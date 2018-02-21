class Movie:
    def __init__(self, name, genre, year, watched):
        self.name = name
        self.genre = genre
        self.year = year
        self.watched = watched
        #print("You have created, {}, a {} - type film, made in {}".format(name, genre, year))
    def __repr__(self):
        return f"Movie(s) : {self.name}"
    def json(self):
        return {
            'name' : self.name,
            'genre' : self.genre,
            'year' : self.year,
            'watched' : self.watched
        }

    @classmethod
    def to_json(cls, json_data):
        return cls(json_data['name'], json_data['genre'], json_data['year'], json_data['watched'])
        #return cls(**json_data) dictionary passed to init class as a set of named paramaters (not ordered)