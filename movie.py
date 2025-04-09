class Movie:
    '''A class that stores information about movies.'''
    #Constructor
    def __init__(self, movie_id, title, director, genre, available, price, rental_count):
        self.__movie_id = movie_id
        self.__title = title
        self.__director = director
        self.__genre = genre
        self.__available = available
        self.__price = price
        self.__rental_count = rental_count
    
    #Getters
    def get_movie_id(self):
        return self.__movie_id
    
    def get_title(self):
        return self.__title
    
    def get_director(self):
        return self.__director
    
    def get_genre(self):
        return self.__genre
    
    def get_available(self):
        return self.__available
    
    def get_price(self):
        return self.__price
    
    def get_rental_count(self):
        return self.__rental_count
    
    def get_genre_name(self):
        GENRE_NAME = {0: 'Action', 1: 'Comedy', 2: 'Drama', 3: 'Horror', 4: 'Sci-Fi',
        5: 'Romance', 6: 'Thriller', 7: 'Animation', 8: 'Documentary', 9: 'Fantasy'}
        return GENRE_NAME[self.get_genre()]
    
    def get_availability(self):
        if(self.get_availability()):
            return 'Available'
        else:
            return 'Rented'
    #Setters
    def set_movie_id(self, movie_id):
        self.__movie_id = movie_id

    def set_title(self, title):
        self.__title = title

    def set_director(self, director):
        self.__director = director

    def set_genre(self, genre):
        self.__genre = genre

    def set_price(self, price):
        self.__price = price
    
    def __str__():
        return "{:10s}{:30s}{:25s}{:12s}{:12s}{:>12s}{:>12s}".format("ID", "Title",
        "Director", "Genre", "Availability", "Price", "# Rentals")