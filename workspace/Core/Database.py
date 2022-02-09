from workspace.ETL.Load import Load
from workspace.Entities.User import User


class Database:
    def __init__(self):
        self._database_name = "users_data.txt"
        self._file_path = r"C:\BasicCourse\Tasks\Spotipy\users"
        self._file_loader = Load()

    def create_db(self):
        self._file_loader.create_file("hello", self._file_path, self._database_name)

    def add_user_to_db(self, username, password):
        user = User(username, password)
        self._file_loader.load_data_to_file(user, self._file_path, self._database_name)

    def check_if_user_exist(self, username):
        file = self._file_loader.get_data_from_file(self._file_path, self._database_name)
        for line in file.readlines():
            if username in line:
                return True
        return False

    def check_password_validation(self, username, password):
        file = self._file_loader.get_data_from_file(self._file_path, self._database_name)
        lines = file.readlines()
        for line in lines:
            if username in line:
                if password in line:
                    return True
        return False
