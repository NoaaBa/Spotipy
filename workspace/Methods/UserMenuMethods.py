from workspace.Core.Database import Database
from workspace.Entities.User import User

class UserMenuMethods:
    def __init__(self, database):
        self._database = database

    def get_input(self):
        self._username = input("Enter username: ")
        self._password = input("Enter password: ")

    def user_signup(self):
        self.get_input()
        if self._database.check_if_user_exist(self._username):
            print(f"User {self._username} already exists in Spotipy.")
        else:
            self._database.add_user_to_db(self._username, self._password)

    def user_login(self):
        self.get_input()
        if self._database.check_if_user_exist(self._username):
            if self._database.check_password_validation(self._username, self._password):
                print("Logged in successfully.")
            else:
                print("Password is incorrect.")
        else:
            print(f"User {self._username} doesn't exist in Spotipy.")
