import webbrowser


class Movie:
    # Movie class providing blueprint for movie information
    """ This class stores movie information"""

# Init method that initializes object with movie information
    def __init__(self, movie_title,
                 movie_storyline,
                 movie_poster_image_url,
                 movie_trailer_youtube_url,
                 release_date,
                 first_actor,
                 second_actor):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url
        self.release_date = release_date
        self.first_actor = first_actor
        self.second_actor = second_actor

# Show trailer method to open up web browser to launch trailer video
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
