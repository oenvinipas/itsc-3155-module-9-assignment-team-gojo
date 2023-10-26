# TODO: Feature 1
from app import movie_repository
from src.repositories.movie_repository import get_movie_repository

# check if get_all_movies() returns a dictionary that is empty/no movies are in the 
# repository.
def test_get_all_movies():
    movie_repo = get_movie_repository()
    movie_repo.clear_db()
    assert len(movie_repo.get_all_movies()) == 0
    
def test_get_movies():
    movie_repo = get_movie_repository()
    movie_repo.clear_db()

    movie_repository.create_movie('Jurassic Park', "Steven Spielberg", "5")
    movie_repository.create_movie('Whiplash', 'Damien Chazelle', '4')
    assert len(movie_repo.get_all_movies()) == 2 