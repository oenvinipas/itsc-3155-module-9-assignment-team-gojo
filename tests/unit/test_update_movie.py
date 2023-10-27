# TODO: Feature 5

from app import movie_repository

def test_update_movie():
    movie_repository.create_movie("The Dark Knight", "Christopher Nolan", 5)
    movie = movie_repository.get_movie_by_title("The Dark Knight")
    movie_id = movie.movie_id

    movie_repository.update_movie(movie_id, "The Dark Knight Rises", "Christopher Nolan", 4)

    updated_movie = movie_repository.get_movie_by_id(movie_id)
    assert updated_movie.title == "The Dark Knight Rises"
    assert updated_movie.director == "Christopher Nolan"
    assert updated_movie.rating == 4
