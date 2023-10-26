# TODO: Feature 1
from app import app 


def test_get_all_movie_page(test_app):
    test_app = app.test_client()
    response = test_app.get('/movies')

    data = response.data.decode('utf-8')
    
    assert response.status_code == 200
    assert "There Are No Movies To Display!" in data
    # assert "All Movies" in data
    # assert "See Our List of Movie Ratings Below" in data