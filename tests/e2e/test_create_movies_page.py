# TODO: Feature 2

def test_get_create_movie_page(test_app):
    response = test_app.get('/movies/new')
    
    data = response.data.decode('utf-8')
    
    assert response.status_code == 200
    assert '<h1 class="mb-5">Create Movie Rating</h1>' in data
    assert '<p class="mb-3">Create a movie rating below</p>' in data

def test_create_movie_rating(test_app):
    response = test_app.post("/movies", data={
        "movie-title": "Jurassic Park",
        "movie-director": "Steven Spielberg",
        "movie-rating": "5"
    }, follow_redirects=True)
    
    data = response.data.decode("utf-8")
    
    assert response.status_code == 200
    # assert '<p>Jurassic Park</p>' in data
    # assert '<p>Steven Spielberg</p>' in data
    # assert '<p>5</p>' in data
    
def test_create_movie_rating_validation_error(test_app):
    response = test_app.post('/movies', follow_redirects=True)
    
    assert response.status_code == 400