import media
import fresh_tomatoes

"""

This script creates a list of movies
and opens them in an interface within
the default web browser.
    
"""

# Create Toy Story movie
toy_story = media.Movie("Toy Story",
	"A story of a boy and his toys that come to life.",
	"https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",  # NOQA
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")  # NOQA

# Create Avatar movie
avatar = media.Movie("Avatar",
	"A marine on an alien planet.",
	"https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",  # NOQA
	"https://www.youtube.com/watch?v=uZNHIU3uHT4")  # NOQA

# Create District 9 movie
district9 = media.Movie("District 9",
	"Aliens come to Earth and get stranded.",
	"https://upload.wikimedia.org/wikipedia/en/thumb/d/d7/District_nine_ver2.jpg/220px-District_nine_ver2.jpg",  # NOQA
	"https://www.youtube.com/watch?v=DyLUwOcR5pk")  # NOQA

# Make a list of all movies
movies = [toy_story, avatar, district9]

# Display the list of movies in a
# web browser
fresh_tomatoes.open_movies_page(movies)
