def load_movies(file_name):
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
    print_menu()

    pass


if __name__ == '__main__':
    main()