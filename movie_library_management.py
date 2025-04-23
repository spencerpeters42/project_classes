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
        #Open file
        import_movie = open(file_name)
        loaded_movies = 0
        #Create an empty list
        movie_catalog = list()
        #Go through text file line by line
        for each_line in import_movie:
            #Split by every ','
            each_line = each_line.split(',')
            #Add a Movie object with corresponding fields
            movie_catalog.append(Movie(each_line[0], each_line[1], each_line[2], int(each_line[3]), each_line[4], each_line[5], each_line[6]))
            #Increment total movies loaded
            loaded_movies += 1
        print('')
        #Return filled list of Movie objects
        return movie_catalog
    else:
        #Output that the file name was not found
        print('The catalog file \"', file_name, '\" is not found \n')
        #Prompt the user to continue without file
        user_input = input('Do you want to continue without loading a file (Yes/Y, No/N)? ').upper()
        
        if(user_input == 'Y' or user_input == 'YES'):
            print('The Movie Library System is opened without loading catalog \n')
            #Create an empty list to return
            movie_catalog = list()
            #Return empty catalog list
            return movie_catalog
        elif(user_input == 'N' or user_input == 'NO'):
            print('The Movie Library System will not continue...')
            #Return -1 to skip the menu and end program.
            return -1


def save_movies(file_name, movies):
    '''
    Parameters:
        -file_name: The name of the file to save the movie data.
        -movies: A list of Movie objects.
    Return Value:
        - # of movie lines written to file
    Description:
        -Saves the list of Movie objects to a CSV file.
    '''
    #Open file
    catalog = open(file_name, 'w')
    i = 0

    for movie in movies:
        #Write with specified format to file
        catalog.write(f'{movies[i].get_id()},{movies[i].get_title()},{movies[i].get_director()},{movies[i].get_genre()},{movies[i].get_availability()},{movies[i].get_price()},{movies[i].get_rental_count()}\n')
        i += 1
    #Close file
    catalog.close()
    #Return iteration variable
    return i

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
    #Output looking for movie
    print('Searching for \"', search_term, '\" in title, director, or genre...', sep='')
    i = 0
    #Create an empty list for matches
    matches = []
    #Look through all movies
    for movie in movies:
        #Check if search term matches any category of movie object
        if(search_term.upper() in movies[i].get_title().upper() or search_term.upper() in movies[i].get_genre_name().upper() or search_term.upper() in movies[i].get_director().upper()):
            #Add movie to matches
            matches.append(movies[i])
        i+=1
    #Return matching list of Movie objects
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
    #Look through all movies
    for movie in movies:
        #Check to see if input matches with every ID
        if(movie_id == movies[i].get_id()):
            #Return matching Movie object
            return movies[i]
        i += 1
    #Return -1 if no Movie object was found
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
        if(ui_id == movies[i].get_id()):
            fail_msg = 'Movie with ID ' + ui_id + ' already exists - cannot be added to library \n'
            #Case 1: Cannot Add Movie because of conflicting ID 
            return fail_msg
        i += 1
    #Query user for title
    ui_title = input('Enter title: ')
    #Query user for director name
    ui_director = input('Enter director: ')
    #Query user for genre
    ui_genre = get_genre()
    #Query user for price of movie
    ui_price = float(input('\nEnter price: '))
    #Add movie to catalog, making it available to rent and setting rental count to 0
    movies.append(Movie(ui_id, ui_title, ui_director, ui_genre, True, ui_price))
    #Case 2: Successfully Add Movie with no Conflicting ID
    return 'Movie ' + '\'' + ui_title + '\'' + ' added to library successfully .\n'

def remove_movie(movies):
    '''
    Parameters:
        -movies: A list of Movie objects.
    Return Value:
        -A string indicating the result of the remove attempt.
    Description:
        -Removes a movie from the library by its ID.
        Cannot remove a movie if a movie with ID does not exist in the library
    '''
    #Query user for ID
    user_input = int(input('Enter the movie ID to remove: '))
    i = 0
    #Look through all movies for ID
    for movie in movies:
        #Check to see if ID is in list
        if(user_input == int(movies[i].get_id())):
            #Store title for success message
            del_title = movies[i].get_title()
            #Delete Movie
            del movies[i]
            #Return success string
            return 'Movie \'' + del_title + '\' has been removed from library successfully.\n'  
        i += 1
    #Movie was not found, return error message
    return 'Movie with ID ' + str(user_input) + ' not found in library - cannot be removed.\n'

def update_movie_details(movies):
    '''
    Parameters:
        -movies: A list of Movie objects
    Return Value:
        -A string indicating the result of the update attempt.
    Description:
        -Updates all the details of a movie by its ID.
        Cannot edit a movie if a movie with ID does not exist in the list.
    '''
    #Prompt the user for ID
    ui_id = int(input('Enter the movie ID to update: '))
    i = 0
    #Check to see if ID is in list
    for movie in movies:
        if(ui_id == int(movies[i].get_id())):
            #Update Movie
            print('Leave fields blank to keep current values.')
            #Prompt user for title
            ui_title = input('Enter new title (current: ' + movies[i].get_title() + '): ')
            #Check to see if blank
            if(ui_title != ''):
                #Update title
                movies[i].set_title(ui_title)
            #Prompt user for director
            ui_director = input('Enter new director (current: ' + movies[i].get_director() + '): ')
            #Check to see if blank
            if(ui_director != ''):
                #Update director
                movies[i].set_director(ui_director)
            #Prompt user to change genre
            ui_genre = input('Enter new genre (current: ' + movies[i].get_genre_name() + ') (Yes/Y, No/N)? ')
            #Check if user wants to change genre
            if(ui_genre.upper() == 'Y' or ui_genre.upper() == 'YES'):
                #Update genre
                update_genre = get_genre()
                movies[i].set_genre(update_genre)
            #Prompt user to change price
            ui_price = input('Enter new price (current: ' + str(movies[i].get_price()) + '): ')
            #Check to see if blank
            if(ui_price != ''):
                #Update price
                movies[i].set_price(float(ui_price))
            #Return Success Message
            return 'Movie with ID ' + movies[i].get_id() + ' is updated successfully. \n'
        i += 1
    #Movie with ID not found, return failure message
    return 'Movie with ID ' + str(ui_id) + ' is not found in library. \n'

def get_genre():
    '''
    Parameters: None.
    Return Value:
        -The user's valid menu choice as a string.
    Description:
        -Displays the genre codes and descriptions and prompts the user for a valid choice.
    '''
    #Retrieve Genre Names and Keys
    movies = Movie(0, '', '', 0, True, 0.00)
    genre_list = movies.list_genre()
    genre_keys = movies.get_genre_keys()
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
    return ui_genre

def list_movies_by_genre(movies):
    '''
    Parameters:
        -movies: A list of Movie objects.
    Return Value: None
    Description:
        -Lists all movies of a specified genre. Displays a list of movies in the specified genre, or no movies found.
    '''
    user_input = get_genre()
    i = 0
    matched = False
    matching_movies = []

    for movie in movies:
        if(user_input == movies[i].get_genre()): 
            matched = True
            matching_movies.append(movies[i])
        i += 1
    
    if(matched == True):
        print_movies(matching_movies)
        print()
    else:
        print('No movies found.')

    print()

def print_movies(movies):
    '''
    Parameters:
        -movies: A list of Movie objects.
    Return Value: None.
    Description:
        -Prints a list of movies in a formatted table.
    '''
    i = 0
    #Print Header
    print('\n', MENU_HEADER, sep='')
    print(DASHES)
    #Format each element and output.
    for movie in movies:
        rental_cnt = str(movies[i].get_rental_count())
        rental_cnt = rental_cnt.strip('\n')
        print(f'{movies[i].get_id():<10}{movies[i].get_title():<30}{movies[i].get_director():<25}{movies[i].get_genre_name():<12}{movies[i].get_availability():<19}{movies[i].get_price():<8}{rental_cnt:>9}')
        i += 1
    pass

def popular_movies(movies):
    '''
    Parameters:
        -movies: A list of Movie objects.
    Return Value: None.
    Description:
        -Displays all the movies that have a rental_count >= to the entered value.
    '''
    #Query the user for input
    user_input = input('Enter the minimum number of rentals for the movies you want to view: ')
    #Matching list of movies
    matches = []
    i = 0
    #Check every movies rental count
    for movie in range(len(movies)):
        #Check if rental_count is higher than user_input
        if(int(movies[i].get_rental_count()) >= int(user_input)):
            #Add movie to matching list
            matches.append(movies[i])
        i += 1
    #Outputs
    print('\nMovies Rented', user_input, 'times or more', end='')
    #Format matching list and outputted
    print_movies(matches)
    print()
    pass

def check_availability_by_genre(movies):
    '''
    Parameters:
        -movies: A list of Movie objects.
    Return Value: None.
    Description:
        -Checks and displays the availability of movies in a specified genre.
        -Displays a list of movies that are available in the specified genre or no available movies.
    '''
    #Get genre from user
    user_input = get_genre()
    #Create matching list
    matches = []
    i = 0
    #Check all movies for specified genre and if they are available
    for movie in movies:
        if((movies[i].get_genre() == user_input) and (movies[i].get_availability() == 'Available')):
            matches.append(movies[i])
        i += 1
    #If no matches found
    if(len(matches) == 0):
        print('No movies available in that genre')
    else:
        #Output matching movies
        print_movies(matches)
        print()
    pass

def display_library_summary(movies):
    '''
    Parameters:
        -movies: A list of Movie objects.
    Return Value: None.
    Description:
        -Displays a summary of the library, including the total number of movies, number of available movies, and number of rented movies.
    '''
    total_movies = len(movies)
    available_movies = 0
    rented_movies = 0
    i = 0
    for movie in movies:
        if(movies[i].get_availability() == 'Available'):
            available_movies += 1
        else:
            rented_movies += 1
        i += 1
    print()
    print(f'{'Total movies':16}{':':4}{total_movies:4}')
    print(f'{'Available movies':16}{':':4}{available_movies:4}')
    print(f'{'Rented movies':16}{':':4}{rented_movies:4}')
    print()
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
            #Search for movies menu option
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
                    print_movies(matched_movies)
                    print()
            #Rent a movie menu option
            elif(user_input == '2'):
                #Prompt the user for ID to rent
                rent_id = input('Enter the movie ID to rent: ')
                #Print result of rental attempt
                print(rent_movie(catalog, rent_id))
            #Return a movie menu option
            elif(user_input == '3'):
                #Prompt the user for ID to return
                return_id = input('Enter the movie ID to return: ')
                #Print result of return attempt
                print(return_movie(catalog, return_id))
            #Add a movie menu option
            elif(user_input == '4'):
                #Call add_movie function and print resulting message
                print(add_movie(catalog))
            #Remove a movie menu option
            elif(user_input == '5'):
                #Call remove_movie function and print resulting message
                print(remove_movie(catalog))
            #Update movie details menu option
            elif(user_input == '6'):
                #Call update_movie_details function and print resulting message
                print(update_movie_details(catalog))
            #List movies by genre menu option
            elif(user_input == '7'):
                #Call list_movies_by_genre function
                list_movies_by_genre(catalog)
            #Find popular movies menu option
            elif(user_input == '8'):
                #Call popular_movies function
                popular_movies(catalog)
            #Check availability by genre menu option
            elif(user_input == '9'):
                #Call check_availability_by_genre function
                check_availability_by_genre(catalog)
            #Display library summary menu option
            elif(user_input == '10'):
                #Call display_library_summary function
                display_library_summary(catalog)
            user_input = print_menu()
        #Prompt the user to update file or discard changes
        update = input('Would you like to update the catalog (Yes/Y, No/N)? ').upper()
        #Write changes to file
        if(update == 'Y' or update == 'YES'):
            movies_written = save_movies(file_name, catalog)
            print(movies_written, 'movies have been written to Movie catalog.')
        else:
            print('Movie catalog has not been updated.')
        #End program
        print('Movie Library System Closed Successfully')


if __name__ == '__main__':
    main()