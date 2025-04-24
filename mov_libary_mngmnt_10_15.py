import os
from movie import Movie

MENU_HEADER = f'{'ID':<10}{'Title':<30}{'Director':<25}{'Genre':<12}{'Availability':<19}{'Price':<8}{'# Rentals':>9}'
DASHES = '-' * 113


class MovieManagement:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie_id, title, director, year):
        new_movie = Movie(movie_id, title, director, year)
        self.movies.append(new_movie)

    def __str__(self):
        return "\n".join(str(movie) for movie in self.movies)

    def update_mov(movies):
        '''
        Parameters:
            -movies: A list of Movie objects.
        Return Value:
            -A string indicating the result of the remove attempt.
        Description:
            -Removes a movie from the library by its ID.
            Cannot remove a movie if a movie with ID does not exist in the library
        '''
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

def get_genre():
    movies = Movie(0, '', '', 0, True, 0.00)
    genre_list = movies.list_genre()
    genre_keys = movies.get_genre_keys()
    i = 0
    print('\n\tGenres')
    for item in range(len(genre_list)):
        current_index = str(i) + ')'
        print(f'{'\t'}{current_index}{genre_list[i]}')
        i += 1
    ui_genre = int(input('\tChoose genre(0-9): '))

    while ui_genre not in genre_keys:
        print('Invalid Genre: Enter a valid genre (0-9)')
        ui_genre = int(input('\tChoose genre(0-9): '))
    return ui_genre

def list_movies_by_genre(movies):
    user_genre = get_genre()
    i = 0
    matched = False
    mov_match = []

    for movie in movies:
        if(user_genre == movies[i].get_genre()): 
            matched = True
            mov_match.append(movies[i])
        i += 1
    
    if(matched == True):
        print_movies(mov_match)
        print()
    else:
        print('No movies found.')

    print()

def print_movies(movies):
    i = 0
    print('\n', MENU_HEADER, sep='')
    print(DASHES)

    for movie in movies:
        rented = str(movies[i].get_rental_count())
        rented = rented.strip('\n')
        print(f'{movies[i].get_id():<10}{movies[i].get_title():<30}{movies[i].get_director():<25}{movies[i].get_genre_name():<12}{movies[i].get_availability():<19}{movies[i].get_price():<8}{rental_cnt:>9}')
        i += 1
    pass

