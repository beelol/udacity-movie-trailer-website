import webbrowser
class Movie():

    """
    
    Attributes:
        title (str): The title of a movie
        storyline (str): The storyline of a movie
        poster_image_url (str): URL to an image of
        the movie poster.
        trailer_youtube_url (str): URL to the
        trailer of the movie on youtube
    
    """

    # Sets title, storyline, poster url, and trailer
    # url of a movie
    def __init__(self, title, storyline, poster_image,
				youtube_trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

    # Opens the url of a movie trailer in a web
    # browser
    def show_trailer(self):
        webbrowser.open(self.youtube_trailer)
