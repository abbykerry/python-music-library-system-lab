#!/usr/bin/env python3

class Song:
    """Represents a song with name, artist, and genre."""

    # Class attributes (shared by all Song objects)
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        """Initialize a new Song object with name, artist, and genre."""
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the total number of songs
        Song.count += 1

        # Add genre to the list of unique genres
        if genre not in Song.genres:
            Song.genres.append(genre)

        # Add artist to the list of unique artists
        if artist not in Song.artists:
            Song.artists.append(artist)

        # Update the count of songs per genre
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Update the count of songs per artist
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1