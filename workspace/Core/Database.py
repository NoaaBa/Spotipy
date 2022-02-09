import mysql.connector


class Database:
    def __init__(self):
        self.db_connector = mysql.connector.connect(host="localhost")
        self.my_cursor = self.db_connector.cursor()

    def create_db(self):
        self.my_cursor.execute("CREATE DATABASE users_data")
        self.my_cursor.execute("CREATE TABLE users (username VARCHAR(255) PRIMARY KEY, password VARCHAR(255))")

    def add_user_to_db(self, username, password):
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = (username, password)
        self.my_cursor.execute(sql, val)

    def check_if_user_exist(self, username, password):
        self.my_cursor.execute(f"SELECT {username} FROM users WHERE username=?")
        check_username = self.my_cursor.fetchone()
        if check_username != 0:
            print(f"Username {username} doesn't exist")
        else:
            print(f"{username} logged in!")
