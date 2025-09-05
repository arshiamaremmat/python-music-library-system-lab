class Song:
    # ---- Class attributes (global insights) ----
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    # Optional alias to match alternate naming in some specs
    artists_count = artist_count

    def __init__(self, name: str, artist: str, genre: str):
        # ---- Instance attributes ----
        self.name = name
        self.artist = artist
        self.genre = genre

        # ---- Update class-level insights ----
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    # ---- Class methods for maintaining global state ----
    @classmethod
    def add_song_to_count(cls):
        """Increment total number of Song objects."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre: str):
        """Track unique genres."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist: str):
        """Track unique artists."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre: str):
        """Count songs per genre."""
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist: str):
        """Count songs per artist."""
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
