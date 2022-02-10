import json
import logging
from workspace.Storage.DataConfigurator import DataConfigurator


class SearchMethods:
    def __init__(self):
        logging.basicConfig(filename="search_log_file.log", format='%(asctime)s %(message)s', filemode='w')
        self.logger = logging.getLogger()

    def get_all_artists(self):
        file = open(DataConfigurator.tracks_path + "tracks.json")
        data_list = json.load(file)
        artists_list = []
        for data in data_list:
            for key in data:
                if (key == 'artists'):
                    for artist in data[key]:
                        artists_list.append(artist['name'])
        if not artists_list:
            self.logger.error("Error getting the artists from the file.")
        else:
            print(*artists_list, sep=", ")

        file.close()

    def get_albums_by_artist_name(self, artist_name):
        file = open(DataConfigurator.tracks_path + "tracks.json")
        data_list = json.load(file)
        albums_list = []
        for data in data_list:
            if artist_name in data:
                for key in data:
                    if (key == 'album'):
                        for album in data[key]:
                            albums_list.append(album['name'])
        if not albums_list:
            self.logger.error("Artist name was not found.")
        else:
            print(*albums_list, sep=", ")

        file.close()

    def get_most_popular_songs_by_artist_name(self, artist_name):
        file = open(DataConfigurator.tracks_path + "tracks.json")
        data_list = json.load(file)
        popular_songs = [0] * 10
        for data in data_list:
            if artist_name in data:
                for i in range(0, 10):
                    max = (data['song_popularity'])
                    for j in range(len(popular_songs)):
                        if popular_songs[j] > max:
                            max = popular_songs[j]
                        popular_songs.append(max)

        if not popular_songs:
            self.logger.error("Error reading the songs.")
        else:
            print(*popular_songs, sep=", ")

        file.close()

    def get_all_songs_in_album(self, album_name):
        file = open(DataConfigurator.tracks_path + "tracks.json")
        data_list = json.load(file)
        songs_list = []
        for data in data_list:
            if album_name in data:
                songs_list.append(data['song_name'])

        if not songs_list:
            self.logger.error("Couldn't read the songs from the album.")
        else:
            print(*songs_list, sep=", ")

        file.close()
