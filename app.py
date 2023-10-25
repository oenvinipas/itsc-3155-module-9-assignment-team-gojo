from flask import Flask, abort, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True, movie_repository=movie_repository)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html')


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    movie_title = request.form.get("movie-title")
    movie_director = request.form.get("movie-director")
    movie_rating = request.form.get("movie-rating")
    
    if movie_title is None or movie_director is None or movie_rating is None:
        abort(400)
    
    movie_repository.create_movie(movie_title, movie_director, movie_rating)
    
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3 
    movie_repository.create_movie("The Shawshank Redemption", "Frank Darabont", 1)
    movie_repository.create_movie("The Godfather", "Francis Ford Coppola", 3)
    movie_repository.create_movie("Pulp Fiction", "Quentin Tarantino", 5)

    movie_title = request.args.get('movie-title')
    
    if movie_title is None:
        return render_template('search_movies.html', search_active=True)

    movie = movie_repository.get_movie_by_title(movie_title)

    return render_template('search_movies.html', search_active=True, movie=movie)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    return render_template('get_single_movie.html')


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    return render_template('edit_movies_form.html')


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass

#test3