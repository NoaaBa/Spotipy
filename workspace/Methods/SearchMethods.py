import json
from pprint import pprint
from workspace.ETL.Load import Load
from workspace.Storage.DataConfigurator import DataConfigurator


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


def get_albums_by_artist_name(self, artist):
    pass


def get_most_popular_songs_by_artist_name(self, artist):
    pass


def get_all_songs_in_album(self, album):
    pass
