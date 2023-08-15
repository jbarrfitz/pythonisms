# test_movies.py
import pytest
from pythonisms.dunder import Movie  # Import the Movie class from your module

xanadu = Movie("Xanadu", "Robert Greenwald", 1980, 96, "Musical", 9.0)
airplane = Movie("Airplane!", "Jim Abrahams, David Zucker, Jerry Zucker", 1980, 88, "Comedy", 10.0)
silence_of_the_lambs = Movie("The Silence of the Lambs", "Jonathan Demme", 1991, 118, "Thriller", 9.6)
manhunter = Movie("Manhunter", "Michael Mann", 1986, 120, "Thriller", 7.3)
amelie = Movie("Amelie", "Jean-Pierre Jeunet", 2001, 122, "Romantic Comedy", 8.3)
remains_of_the_day = Movie("The Remains of the Day", "James Ivory", 1993, 134, "Drama", 7.8)
network = Movie("Network", "Sidney Lumet", 1976, 121, "Drama", 9.1)
orient_express = Movie("Murder on the Orient Express", "Sidney Lumet", 1974, 128, "Mystery", 7.3)


# Test cases
def test_movie_initialization():
    assert xanadu.title == "Xanadu"
    assert airplane.director == "Jim Abrahams, David Zucker, Jerry Zucker"


def test_movie_less_than():
    assert network > manhunter


def test_movie_less_than_equal():
    assert orient_express <= manhunter


def test_movie_equal():
    assert orient_express == manhunter


def test_movie_greater_than():
    assert xanadu > remains_of_the_day


def test_movie_greater_than_equal():
    assert silence_of_the_lambs > amelie


def test_movie_not_equal():
    assert amelie != network


def test_movie_hashable():
    assert isinstance(hash(silence_of_the_lambs), int)


def test_movie_to_string():
    assert str(silence_of_the_lambs) == "The Silence of the Lambs"
