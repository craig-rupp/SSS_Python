import sqlite3

#initial connections
connection = sqlite3.connect('data.db')

cursor = connection.cursor()
create_table = "CREATE TABLE Users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'Craig_TR', 'Thomas')
insert_user1 = "INSERT INTO Users VALUES(?, ?, ?)"
cursor.execute(insert_user1, user)

users = [
    (2, 'Rolf', 'flor'),
    (3, 'Anne', 'Grur')
]

cursor.executemany(insert_user1, users)

select_query = "SELECT * from Users"

for row in cursor.execute(select_query):
    print(row)


connection.commit()

connection.close()
