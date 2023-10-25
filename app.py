from flask import Flask, redirect, render_template, abort, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)
app.debug = True

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    movie = movie_repository.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=True, movie_repository=movie_repository, movie=movie)
    movie = movie_repository.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=True, movie_repository=movie_repository, movie=movie)


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
    print(type(movie_title))
    print(type(movie_director))
    print(type(movie_rating))
    
    if movie_title is None or movie_director is None or movie_rating is None:
        abort(403)
    
    movie_rating = int(movie_rating)
    
    movie_repository.create_movie(movie_title, movie_director, movie_rating)
    
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3 
    movie_title = request.args.get('movie-title')
    
    if movie_title is None:
        return render_template('search_movies.html', search_active=True)

    movie = movie_repository.get_movie_by_title(movie_title)
    return render_template('search_movies.html', search_active=True, movie=movie, error='There is no movie by that name')


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    movie = movie_repository.get_movie_by_id(int(movie_id)) #unit test this
    if movie:
        title = movie.title
        director = movie.director
        rating = movie.rating
    else: 
        abort (404)
    return render_template('get_single_movie.html', title=title, director=director, rating=rating, movie_id=movie_id)

@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
   # Retrieve the current movie's details
   movie = movie_repository.get_movie_by_id(int(movie_id))
   if movie:
       current_title = movie.title
       current_director = movie.director
       current_rating = movie.rating
   else:
       abort(404)
  
   return render_template('edit_movies_form.html', current_title=current_title, current_director=current_director, current_rating=current_rating, movie_id=movie_id)


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
   # TODO: Feature 5
   movie_title = request.form['movie-title']
   movie_director = request.form['movie-director']
   movie_rating = request.form['movie-rating']
  
   if movie_title is None or movie_director is None or movie_rating is None:
       abort(400)

   movie_rating = int(movie_rating)
  
   movie_repository.update_movie(movie_id, movie_title, movie_director, movie_rating)

   # After updating the movie in the database, we redirect back to that single movie page
   return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass

# test 