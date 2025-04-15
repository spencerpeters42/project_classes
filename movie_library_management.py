import os
from movie import Movie

def load_movies(file_name):
    #Validating file path
    if os.path.exists(file_name):
        import_movie = open(file_name)
        loaded_movies = 0
        movie_catalog = list()

        for each_line in import_movie:
            each_line = each_line.split(',')
            movie_catalog.append(Movie(each_line[0], each_line[1], each_line[2], each_line[3], each_line[4], each_line[5], each_line[6]))
            loaded_movies += 1
            return loaded_movies
    else:
        print('The catalog file \"', file_name, '\" is not found \n')
        
        user_input = input('Do you want to continue without loading a file (Yes/Y, No/N)? ').upper()
        
        pass    


def save_movies(file_name, movies):
    pass

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
    load_catalog = load_movies(file_name)
    print(load_catalog)
    #print_menu()
    pass


if __name__ == '__main__':
    main()