# TODO: Feature 3
from app import movie_repository
from src.repositories.movie_repository import get_movie_repository

def test_get_search_movie_page(test_app):
    response = test_app.get('/movies/search')
    
    data = response.data.decode('utf-8')
    
    assert response.status_code == 200
    assert '<h1 class="mb-5">Search Movie Ratings</h1>' in data
    assert '<p class="mb-3">Search for a movie rating below</p>' in data

def test_search_movie_rating_page(test_app):
    response = test_app.get('/movies/search', query_string={
        'movie-title': "Jurassic Park",
        "movie-director": "Steven Spielberg",
        "movie-rating": "4"
    }, follow_redirects=True)
    
    data = response.data.decode("utf-8")

    assert '<h3 class="pt-2"> Jurassic Park </h3>' in data
    assert '<p> Author: Steven Spielberg </p>' in data
    assert '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="gold" class="bi bi-star-fill" viewBox="0 0 16 16">' in data
    assert '<path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>' in data
    if movie_repository.get_movie_by_title("Jurassic Park").rating < 5:
        assert '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-star" viewBox="0 0 16 16">' in data 
        assert '<path d="M2.866 14.85c-.078.444.36.791.746.593l4.39-2.256 4.389 2.256c.386.198.824-.149.746-.592l-.83-4.73 3.522-3.356c.33-.314.16-.888-.282-.95l-4.898-.696L8.465.792a.513.513 0 0 0-.927 0L5.354 5.12l-4.898.696c-.441.062-.612.636-.283.95l3.523 3.356-.83 4.73zm4.905-2.767-3.686 1.894.694-3.957a.565.565 0 0 0-.163-.505L1.71 6.745l4.052-.576a.525.525 0 0 0 .393-.288L8 2.223l1.847 3.658a.525.525 0 0 0 .393.288l4.052.575-2.906 2.77a.565.565 0 0 0-.163.506l.694 3.957-3.686-1.894a.503.503 0 0 0-.461 0z"/>' in data
    assert '</svg>' in data

def test_opposite_search_movie_rating_page(test_app):
    response = test_app.get('/movies/search', query_string={
        'movie-title': "Aquaman",
        "movie-director": "Steven Spielberg",
        "movie-rating": "2"
    }, follow_redirects=True)
    
    data = response.data.decode("utf-8")

    assert not '<h3 class="pt-2"> Aquaman </h3>' in data

def test_error_message(test_app):
    response = test_app.get('/movies/search', query_string={
        'movie-title': "",
    },follow_redirects=True)
    
    data = response.data.decode("utf-8")

    assert '<h3 class = "text-center text-danger strong">There is no movie by that name</h3>' in data