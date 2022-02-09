import json
from pprint import pprint
from workspace.ETL.Load import Load
from workspace.Storage.DataConfigurator import DataConfigurator

file.close()


class SearchMethods:
    def get_all_artists(self):
        file = open(DataConfigurator.tracks_path + "tracks.json")
        data_list = json.load(file)
        artists_list = []
        for list in data_list:
            for data in data_list:
                # print(f"OOPP {data}")
                for key in data:
                    # print(key)
                    # print(data[key])
                    if (key == 'artists'):
                        for artist in data[key]:
                            artists_list.append(artist['name'])
        print(*artists_list, sep=", ")

        file.close()


def get_albums_by_artist_name(self, artist_name):
    file = open(DataConfigurator.tracks_path + "tracks.json")
    data_list = json.load(file)
    albums_list = []
    for list in data_list:
        for data in data_list:
            if artist_name in data:
                for key in data:
                    if (key == 'album'):
                        for album in data[key]:
                            albums_list.append(album['name'])
    print(*albums_list, sep=", ")
    file.close()


def get_most_popular_songs_by_artist_name(self, artist_name):
    file = open(DataConfigurator.tracks_path + "tracks.json")
    data_list = json.load(file)
    albums_list = []
    popular_songs = [0]*10
    for list in data_list:
        for data in data_list:
            if artist_name in data:
                for i in range(0, 10):
                    max = (data['song_popularity'])
                    for j in range(len(popular_songs)):
                        if popular_songs[j] > max:
                            max = popular_songs[j]
                        popular_songs.append(max)
    print(*popular_songs, sep=", ")
    file.close()


def get_all_songs_in_album(self, album):
    pass
