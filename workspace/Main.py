from consolemenu import *
from consolemenu.items import *
from workspace.Core.Database import Database
from workspace.Methods.UserMenuMethods import UserMenuMethods
from workspace.ETL.ETLManager import ETLManager
from workspace.Storage.DataConfigurator import DataConfigurator


def main():
    database = Database()
    database.create_db()
    user_methods = UserMenuMethods(database)
    # TODO don't use magic strings!!
    # TODO check if songs file exists, if so - don't add new songs to it
    etl_manager = ETLManager(DataConfigurator.songs_path, DataConfigurator.tracks_path, "tracks")
    etl_manager.run()

    menu = ConsoleMenu("Spotipy", "MAIN MENU")

    login = FunctionItem("Login", user_methods.user_login, args=[])
    signup = FunctionItem("Signup", user_methods.user_signup, args=[])



    menu.append_item(login)
    menu.append_item(signup)

    menu.start()
    menu.join()

if __name__ == '__main__':
    main()
