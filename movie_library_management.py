import os
from movie import Movie

def load_movies(file_name):
    '''
    Parameters:
        -file_name: The name of the file containing movie data.
    Return Value:
        -A list of Movie objects.
    Description:
        -Loads movies from a CSV file and returns them as a list of Movie Objects.
    '''
    #Validating file path
    if os.path.exists(file_name):
        import_movie = open(file_name)
        loaded_movies = 0
        movie_catalog = list()
        for each_line in import_movie:
            each_line = each_line.split(',')
            movie_catalog.append(Movie(each_line[0], each_line[1], each_line[2], int(each_line[3]), each_line[4], each_line[5], each_line[6]))
            loaded_movies += 1
        return movie_catalog
    else:
        print('The catalog file \"', file_name, '\" is not found \n')
        
        user_input = input('Do you want to continue without loading a file (Yes/Y, No/N)? ').upper()
        
        if(user_input == 'Y' or user_input == 'YES'):
            print('The Movie Library System is opened without loading catalog')
            movie_catalog = list()
            return movie_catalog
        elif(user_input == 'N' or user_input == 'NO'):
            print('The Movie Library System will not continue...')
            return -1


def save_movies(file_name, movies):
    pass

def search_movies(movies, search_term):
    '''
    Parameters:
        -movies: A list of Movie Objects.
        -search_term: The term to search for in movie titles, directors, or genres.
    Return Value:
        -A list of matched Movie objects.
    Description:
        -Searches for movies that match that search term.
    '''
    i = 0
    matches = []
    for movie in movies:
        if(search_term.upper() in movies[i].get_title().upper() or search_term.upper() in movies[i].get_genre_name().upper() or search_term.upper() in movies[i].get_director().upper()):
            matches.append(movies[i])
        i+=1
    return matches


def print_menu():
    '''
    Parameters: None
    Return Value: The user's valid menu choice as a string.
    Description: Displays the menu and prompts the user for a valid choice.
    '''
    #Declares available menu options
    menu_options = {'1': 'Search for movies', '2': 'Rent a movie', '3': 'Return a movie', '4':'Add a movie','5':'Remove a movie',
                    '6':'Update movie details','7':'List movies by genre','8': 'Find popular movies','9': 'Check availability by genre',
                    '10':'Display library summary', '0':'Exit the system'}
    menu_key = list(menu_options.keys())
    valid_input = set(menu_options.keys())
    DIVIDER = '=' * 25
    i = 0

    #Print header of menu
    print('Movie Library - Main Menu')
    print(DIVIDER)
    #Prints the menu options
    for option in menu_options:
        key_output = menu_key[i] + ')'
        print(f'{key_output} {menu_options[option]}')
        i += 1 
    #Prompts the user for input
    user_input = input('Enter your selection: ')
    #Validates user input
    while user_input not in valid_input:
        print('Invalid option. Please try again.')
        user_input = input('Enter your selection: ')
    #Return user input
    return user_input



def main():
    file_name = input('Enter the movie catalog filename: ')
    catalog = load_movies(file_name)
    #print_menu()
    search_movies(catalog, 'the')
    pass


if __name__ == '__main__':
    main()