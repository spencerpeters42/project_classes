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

    if(rental == -1):
        #Case 1: Movie is not found.
        not_found = 'Movie with ID ' + movie_id + ' not found in library. \n'
        return not_found
    else:
        #Check to see if rental is available
        if(rental.get_available()):
            #Grab current rental count
            rent_cnt = int(rental.get_rental_count())
            #Increment the rental count
            rental.set_rental_count(rent_cnt + 1)
            #Set movie to unavailable
            rental.set_available(False)
            #Case 2: Movie available to rent and successfully rented
            success_msg = '\'' + rental.get_title() + '\' rented successfully.\n'
            return success_msg
        else:
            #Case 3: Movie is unavailable to rent and not rented.
            fail_msg = '\'' + rental.get_title() + '\' is already rented - cannot be rented again.\n'
            return fail_msg

def return_movie(movies, movie_id):
    '''
    Parameters:
        -movies: A list of Movie objects.
        -movie_id: The ID of the movie to return.
    Return Value:
        -A string indicating the result of the return attempt.
    Description:
        -Returns a rented movie by its ID. Cannot return a movie that has not been rented.
    '''
    movie_return = find_movie_by_id(movies, movie_id)

    if(movie_return == -1):
        not_found = 'Movie with ID ' + movie_id + ' not found in library. \n'
        return not_found
    else:
        if(movie_return.get_available()):
            fail_msg = '\'' + movie_return.get_title() + '\' was not rented - cannot be returned. \n'
            return fail_msg
        else:
            movie_return.set_available(True)
            success_msg = '\'' + movie_return.get_title() + '\' was returned successfully. \n'
            return success_msg

def add_movie(movies):
    '''
    Parameters:
        -movies: A list of Movie objects.
    Return Value:
        -A string indicating the result of the add attempt.
    Description:
        -Adds a new movie to the library after prompting the user for details.
        Cannot add a movie fi the movie with that ID already exists in the list.
    '''
    
    #Query user for ID
    ui_id = input('Enter movie ID: ')

    i = 0
    #Check to see if ID already exists
    for movie in movies:
        if(ui_id == movies[i].get_movie_id()):
            fail_msg = 'Movie with ID ' + ui_id + ' already exists - cannot be added to library \n'
            #Case 1: Cannot Add Movie because of conflicting ID 
            return fail_msg
        i += 1
    #Query user for title
    ui_title = input('Enter title: ')
    #Query user for director name
    ui_director = input('Enter director: ')

    #Retrieve Genre Names and Keys
    genre_list = movies[0].list_genre()
    genre_keys = movies[0].get_genre_keys()
    i = 0
    #Output possible genres
    print('\n\tGenres')
    for item in range(len(genre_list)):
        #Format output
        current_index = str(i) + ')'
        print(f'{'\t'}{current_index}{genre_list[i]}')
        i += 1
    #Query user for genre selection
    ui_genre = int(input('\tChoose genre(0-9): '))
    
    #Validate Genre selection
    while ui_genre not in genre_keys:
        print('Invalid Genre: Enter a valid genre (0-9)')
        ui_genre = int(input('\tChoose genre(0-9): '))
    #Query user for price of movie
    ui_price = float(input('\nEnter price: '))
    #Add movie to catalog, making it available to rent and setting rental count to 0
    movies.append(Movie(ui_id, ui_title, ui_director, ui_genre, True, ui_price, 0))
    #Case 2: Successfully Add Movie with no Conflicting ID
    return 'Movie ' + '\'' + ui_title + '\'' + ' added to library successfully .\n'

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
            #Search for movies function call
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
            #Rent a movie function call
            elif(user_input == '2'):
                #Prompt the user for ID to rent
                rent_id = input('Enter the movie ID to rent: ')
                #Print result of rental attempt
                print(rent_movie(catalog, rent_id))
            #Return a movie function call
            elif(user_input == '3'):
                #Prompt the user for ID to return
                return_id = input('Enter the movie ID to return: ')
                #Print result of return attempt
                print(return_movie(catalog, return_id))
            #Add a movie function call
            elif(user_input == '4'):
                #Call add_movie function and print resulting message
                print(add_movie(catalog))
                pass
            user_input = print_menu()
    pass


if __name__ == '__main__':
    main()