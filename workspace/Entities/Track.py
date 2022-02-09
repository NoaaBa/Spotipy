import json


class Track:
    def __init__(self, album, artists, song_id, song_name, song_popularity):
        self._album = album
        self._artists = artists
        self._song_id = song_id
        self._song_name = song_name
        self._song_popularity = song_popularity

    def __str__(self):
        return str({"Album": f"{self._album}",
                    "Artists": f"{self._artists}",
                    "Song ID": f"{self._song_id}",
                    "Song name": f"{self._song_name}",
                    "Song popularity": f"{self._song_popularity}"})

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)
