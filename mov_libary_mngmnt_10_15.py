import os
from movie import Movie

class MovieManagement:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie_id, title, director, year):
        new_movie = Movie(movie_id, title, director, year)
        self.movies.append(new_movie)

    def __str__(self):
        return "\n".join(str(movie) for movie in self.movies)
    
def update_mov(movies):
    movie_id= input('Enter the movie id you want to update.')

    mov_update = None
    for movie in movies:
        if movie.movie_id==movie_id:
            mov_update=movie
            break
    
    new_title = input('Enter new title (blank if non):')
    new_director = input('Enter the name of the director (blank if none):')
    new_year = input('Enter the year (blank if none):')

    if new_title:
        mov_update.title= new_title
    if new_director:
        mov_update.director  = new_director
    if new_year:
        mov_update.year = new_year
    
    return 'Movie details updated successfully'
