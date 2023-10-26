# TODO: Feature 4
from app import movie_repository
from src.repositories.movie_repository import get_movie_repository

def test_no_movie_id_exists():
    repo = get_movie_repository()
    repo.create_movie("The Matrix", "The Wachowski Brothers", 5)
    movie_id = repo.get_movie_by_title("The Matrix").movie_id
    repo.clear_db()
    assert repo.get_all_movies() == {}
    assert repo.get_movie_by_id(movie_id) == None
    
def test_movie_id_exists():
    movie_repository.create_movie("The Matrix", "The Wachowski Brothers", 5)
    movie_id = movie_repository.get_movie_by_title("The Matrix").movie_id
    assert movie_repository.get_movie_by_id(movie_id).movie_id == movie_id
    assert movie_repository.get_movie_by_id(movie_id).title == "The Matrix"
    assert movie_repository.get_movie_by_id(movie_id).director == "The Wachowski Brothers"
    assert movie_repository.get_movie_by_id(movie_id).rating == 5
    assert type(movie_repository.get_movie_by_id(movie_id).movie_id) == type(1)
    assert type(movie_repository.get_movie_by_id(movie_id).title) == type("")
    assert type(movie_repository.get_movie_by_id(movie_id).director) == type("")
    assert type(movie_repository.get_movie_by_id(movie_id).rating) == type(1)