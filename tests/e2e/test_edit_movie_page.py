# TODO: Feature 5
from app import movie_repository

def test_get_edit_movie_page(test_app):
    movie_repository.create_movie("The Dark Knight", "Christopher Nolan", 5)
    movie_id = movie_repository.get_movie_by_title("The Dark Knight").movie_id

    response = test_app.get(f'/movies/{movie_id}/edit')
    data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert '<h1 class="mb-5">Edit Movie Rating</h1>' in data
    assert '<p class="mb-3">Edit the movie rating below</p>' in data

def test_update_movie_rating(test_app):
    movie_repository.create_movie("The Dark Knight", "Christopher Nolan", 5)
    movie_id = movie_repository.get_movie_by_title("The Dark Knight").movie_id

    response = test_app.post(f"/movies/{movie_id}", data={
        "movie-title": "Updated Title",
        "movie-director": "Updated Director",
        "movie-rating": "4"
    }, follow_redirects=True)
    data = response.data.decode("utf-8")

    assert response.status_code == 200
    assert 'Updated Title' in data
    assert 'Updated Director' in data
    assert '4' in data

