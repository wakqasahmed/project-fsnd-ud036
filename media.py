import webbrowser

class Movie():
    """ This class provides information about a movie. """
    VALID_RATINGS=["G","PG","PG-13","R"]
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube

    """ This method adds additional information in the movie object """
    def set_additional_information(self, year, rating, runtime, genre, imdb_rating):
    		self.year = year
    		if self.VALID_RATINGS.index(rating) > -1:
    			self.rating = rating
    		self.runtime = runtime
    		self.genre = genre
    		self.imdb_rating = imdb_rating

    """ This method opens a popup and plays trailer automatically """
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
