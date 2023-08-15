class Movie:
    def __init__(self, title, director, release_year, minutes, genre, rating):
        self.title = title
        self.director = director
        self.release_year = release_year
        self.minutes = minutes
        self.genre = genre
        self.rating = rating

    def __str__(self):
        return self.title

    def __lt__(self, other):
        return self.rating < other.rating

    def __le__(self, other):
        return self.rating <= other.rating

    def __eq__(self, other):
        return self.rating == other.rating

    def __ne__(self, other):
        return self.rating != other.rating

    def __gt__(self, other):
        return self.rating > other.rating

    def __ge__(self, other):
        return self.rating >= other.rating

    def __hash__(self):
        return hash((self.title, self.release_year))

