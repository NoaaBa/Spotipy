import json

class User:
    def __init__(self, username, password, playlists=None, premium=None):
        self.username = username
        self.password = password
        self.songs_playlists = playlists
        self.is_premium = premium

         # The number of playlists a non-premium user can have.
        self.max_non_premium_playlists = 5
         # The number of songs in playlists a non-premium user can have.
        self.max_non_premium_songs = 20


    def create_playlist(self):
        if self.is_premium is False:
            # TODO LOGS
            if len(self.songs_playlists) > self.max_non_premium_playlists:
                print("You've reached the limit of playlists you can create.\n"
                      "Consider buying Premium in order to be able to create more playlists.")
                return
        playlist_name = input("Enter playlist name: ")
        if playlist_name in self.songs_playlists:
            print("Name already exists!")
        else:
            self.songs_playlists.append(playlist_name)

    def add_songs_to_playlist(self):
        playlist_name = input("Enter playlist name: ")
        # TODO LOGS
        if playlist_name not in self.songs_playlists:
            print("Playlist doesn't exist.")
        else:
            if self.is_premium is False:
                if len(self.songs_playlists[playlist_name]) > self.max_non_premium_songs:
                    print("You've reached the limit of songs you can put in a playlist.\n"
                          "Consider buying Premium in order to be able to add more songs.")
                return
            song_name = input("Enter song name: ")
            self.songs_playlists[playlist_name].append(song_name)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
