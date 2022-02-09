class Track:
    def __init__(self, album, artists, song_id, song_name, song_popularity):
        self._album = album
        self._artists = artists
        self._song_id = song_id
        self._song_name = song_name
        self._song_popularity = song_popularity

    def __str__(self):
        return (f"Album: {self._album}\nArtists: {self._artists}\nSong ID: {self._song_id}\n"
              f"Song name: {self._song_name}\nSong popularity: {self._song_popularity}")
