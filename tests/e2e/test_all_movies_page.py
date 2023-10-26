# TODO: Feature 1
from app import app, movie_repository


def test_get_all_movie_page(test_app):
    response = test_app.get('/movies')

    data = response.data.decode('utf-8')
    
    assert response.status_code == 200
    assert "There Are No Movies To Display!" in data

def test_get_movies(test_app):
    movie_repository.create_movie('Jurassic Park', "Steven Spielberg", "5")
    
    response = test_app.get('/movies')
    data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert "All Movies" in data
    assert "See Our List of Movie Ratings Below" in data
    assert "Jurassic Park" in data
    assert "Steven Spielberg" in data
    assert "5" in data
    