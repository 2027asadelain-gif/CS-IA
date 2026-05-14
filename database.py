import sqlite3


with sqlite3.connect("messages.db")as conn:
    cursor=conn.cursor()
    # cursor.execute("SELECT * FROM users")

# create a table 
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS msgs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    msg TEXT)
""")

# username = input("what is your username")

def insert_user(username):
    with sqlite3.connect("messages.db")as conn:
        cursor=conn.cursor()


        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        conn.commit()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        print(result)

        # conn.close()

def insert_message(msg):
    with sqlite3.connect("messages.db")as conn:
        cursor=conn.cursor()


        cursor.execute("INSERT INTO msgs (msg) VALUES (?)", (msg,))
        conn.commit()
        cursor.execute("SELECT * FROM msgs")
        result = cursor.fetchall()
        print(result)

        # conn.close()

# insert_message("hello world")