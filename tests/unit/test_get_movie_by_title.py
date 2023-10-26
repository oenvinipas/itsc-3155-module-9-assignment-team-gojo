# TODO: Feature 3
from app import movie_repository
from src.repositories.movie_repository import get_movie_repository

def test_no_movie_seacrched():
    repo = get_movie_repository()
    repo.clear_db()
    assert len(repo.get_all_movies()) == 0

def test_search_movie_returns_results():
    movie_repository.create_movie('Jurassic Park', "Steven Spielberg", "5")
    assert movie_repository.get_movie_by_title('Jurrasic') == None
    assert movie_repository.get_movie_by_title('Jurassic Park').title == 'Jurassic Park'
    assert movie_repository.get_movie_by_title('Jurassic Park').director == 'Steven Spielberg'
    assert movie_repository.get_movie_by_title('Jurassic Park').rating == '5'
    assert type(movie_repository.get_movie_by_title('Jurassic Park').title) == type("")
    assert type(movie_repository.get_movie_by_title('Jurassic Park').director) == type("")
    assert type(movie_repository.get_movie_by_title('Jurassic Park').rating) == type("")