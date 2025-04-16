import os
from movie import Movie
#Define Constants
MENU_HEADER = f'{'ID':<10}{'Title':<30}{'Director':<25}{'Genre':<12}{'Availability':<19}{'Price':<8}{'# Rentals':>9}'
DASHES = '-' * 113

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
        print('')
        return movie_catalog
    else:
        print('The catalog file \"', file_name, '\" is not found \n')
        
        user_input = input('Do you want to continue without loading a file (Yes/Y, No/N)? ').upper()
        
        if(user_input == 'Y' or user_input == 'YES'):
            print('The Movie Library System is opened without loading catalog \n')
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
    print('Searching for \"', search_term, '\" in title, director, or genre...', sep='')
    i = 0
    matches = []
    for movie in movies:
        if(search_term.upper() in movies[i].get_title().upper() or search_term.upper() in movies[i].get_genre_name().upper() or search_term.upper() in movies[i].get_director().upper()):
            matches.append(movies[i])
        i+=1
    return matches

def find_movie_by_id(movies, movie_id):
    '''
    Parameters:
        -movies: A list of Movie objects.
        -movie_id: The movie_id to locate in the list of Movie objects.
    Return Value:
        -The matches Movie object or -1 if not found.
    Description:
        -Searches for movies that match that search term.
    '''
    i = 0
    for movie in movies:
        if(movie_id == movies[i].get_movie_id()):
            return movies[i]
        i += 1
    
    return -1


def rent_movie(movies, movie_id):
    '''
    Parameters:
        -movies: A list of Movie objects.
        -movie_id: The ID of the movie to rent.
    Return Value:
        -A string indicating the result of the rental attempt.
    Description:
        -Rents a movie by its ID if it is available.
    '''
    #Check to find the movie with user inputted ID
    rental = find_movie_by_id(movies, movie_id)
    #Case 3: Movie is not found.
    if(rental == -1):
        return 'Movie with ID', movie_id, 'not found in library.\n'
    else:
        #Case 1: Movie available to rent and successfully rented
        if(rental.get_available()):
            rental.set_available(False)
            success_msg = '\'' + rental.get_title() + '\' rented successfully.\n'
            return success_msg
        else:
            #Case 2: Movie is unavailable to rent and not rented.
            fail_msg = '\'' + rental.get_title() + '\' is already rented - cannot be rented again.\n'
            return fail_msg

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
    #Reads in file name
    file_name = input('Enter the movie catalog filename: ')
    #Stores Movie objects in a list
    catalog = load_movies(file_name)
    if(catalog == -1):
        print('Movie Library System Closed Successfully\n')
    else:
        #Display menu and get valid user selection
        user_input = print_menu()
        #Continue displaying menu until user selects Exit the system.
        while user_input != '0':
            #Search for movies call
            if(user_input == '1'):
                #Prompt the user for search term
                search_term = input('Enter search term: ')
                #Call and store list of Movie objects that match search term
                matched_movies = search_movies(catalog, search_term)
                #Check if matched movies is empty
                if(len(matched_movies) == 0):
                    print('No matching movies found.\n')
                else:
                    #Display all matched movies
                    print()
                    print(MENU_HEADER)
                    print(DASHES)
                    i = 0
                    #Outputting each matching movie formatted properly
                    for movie in matched_movies:
                        print(f'{matched_movies[i].get_movie_id():<10}{matched_movies[i].get_title():<30}{matched_movies[i].get_director():<25}{matched_movies[i].get_genre_name():<12}{matched_movies[i].get_availability():<19} {matched_movies[i].get_price():<8}{matched_movies[i].get_rental_count():>9}', end='')
                        i += 1
                    print()
            #Rent a movie call
            elif(user_input == '2'):
                #Prompt the user for ID to rent
                rent_id = input('Enter the movie ID to rent: ')
                #Print result of rental attempt
                print(rent_movie(catalog, rent_id))
            user_input = print_menu()
    #search_movies(catalog, 'the')
    pass


if __name__ == '__main__':
    main()