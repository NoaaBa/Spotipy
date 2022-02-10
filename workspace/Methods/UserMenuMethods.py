import logging


class UserMenuMethods:
    def __init__(self, database):
        self._database = database
        logging.basicConfig(filename="user_log_file.log", format='%(asctime)s %(message)s', filemode='w')
        self.logger = logging.getLogger()

    def get_input(self):
        self._username = input("Enter username: ")
        self._password = input("Enter password: ")

    def user_signup(self):
        self.get_input()
        if self._database.check_if_user_exist(self._username):
            self.logger.info(f"User {self._username} already exists in Spotipy.")
        else:
            self._database.add_user_to_db(self._username, self._password)

    def user_login(self):
        self.get_input()
        if self._database.check_if_user_exist(self._username):
            if self._database.check_password_validation(self._username, self._password):
                self.logger.info("Logged in successfully.")
            else:
                self.logger.info("Password is incorrent.")
        else:
            self.logger.info(f"User {self._username} doesn't exist in Spotipy.")
