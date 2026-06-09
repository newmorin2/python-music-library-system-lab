class Song():
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1

        if artist not in Song.artists:
            Song.artists.append(artist)

        if genre not in Song.genres:
            Song.genres.append(genre)

        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        if artist in Song.artists_count:
            Song.artists_count[artist] += 1
        else:
            Song.artists_count[artist] = 1