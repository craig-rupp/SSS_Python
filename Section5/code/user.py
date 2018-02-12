import sqlite3

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * from Users WHERE username=?" #username has to match a parameter ?
        result = cursor.execute(query, (username,))  #, needed to tell python it's a tuple (for username)
        row = result.fetchone()
        if row:
            print("First Row returned")
            print(row)
            #user = cls(row[0], row[1], row[2])
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user