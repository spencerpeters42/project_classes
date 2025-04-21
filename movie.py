class Movie:
    '''A class that stores information about movies.'''

    #Constructor
    def __init__(self, movie_id, title, director, genre, available, price, rental_count = 0):
        self.__movie_id = movie_id
        self.__title = title
        self.__director = director
        self.__genre = genre
        self.__available = available
        self.__price = price
        self.__rental_count = rental_count
        self.__GENRE_NAME = {0: 'Action', 1: 'Comedy', 2: 'Drama', 3: 'Horror', 4: 'Sci-Fi',
        5: 'Romance', 6: 'Thriller', 7: 'Animation', 8: 'Documentary', 9: 'Fantasy'}
    
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
        genre_index = self.get_genre()
        genre_get = self.__GENRE_NAME.get(genre_index)
        return genre_get
    
    def get_availability(self):
        if(self.get_available()):
            return 'Available'
        else:
            return 'Rented'
        
    def list_genre(self):
        return self.__GENRE_NAME
    
    def get_genre_keys(self):
        return self.__GENRE_NAME.keys()
    
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

    def set_available(self, available):
        self.__available = available
    
    def set_rental_count(self, rental_count):
        self.__rental_count = rental_count
    
    def __str__():
        return "{:10s}{:30s}{:25s}{:12s}{:12s}{:>12s}{:>12s}".format("ID", "Title",
        "Director", "Genre", "Availability", "Price", "# Rentals")