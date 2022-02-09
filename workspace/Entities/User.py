import json


class User:
    def __init__(self, username, password, playlists=None, premium=None):
        self._username = username
        self._password = password
        self._songs_playlists = playlists
        self._is_premium = premium

    def create_playlist(self):
        if self._is_premium is False:
            # TODO LOGS
            if len(self._songs_playlists) > 5:
                print("You've reached the limit of playlists you can create.\n"
                      "Consider buying Premium in order to be able to create more playlists.")
                return
        playlist_name = input("Enter playlist name: ")
        if playlist_name in self._songs_playlists:
            print("Name already exists!")
        else:
            self._songs_playlists.append(playlist_name)

    def add_songs_to_playlist(self):
        playlist_name = input("Enter playlist name: ")
        # TODO LOGS
        if playlist_name not in self._songs_playlists:
            print("Playlist doesn't exist.")
        else:
            if self._is_premium is False:
                if len(self._songs_playlists[playlist_name]) > 20:
                    print("You've reached the limit of songs you can put in a playlist.\n"
                          "Consider buying Premium in order to be able to add more songs.")
                return
            song_name = input("Enter song name: ")
            self._songs_playlists[playlist_name].append(song_name)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)
