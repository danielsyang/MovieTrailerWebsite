# -*- coding: utf-8 -*-
'''
Class Attributes:
    title(String): Movie's title.
    movie_description(String): String containing the description of the movie.
    poster_image_url(String): an URL of a poster of the film
    trailer_youtube_url(String): an URL of a trailer of the film
'''
class movie:

    def __init__(self, title, movie_description, poster_image, url_trailer):
        self.title = title
        self.movie_description = movie_description
        self.poster_image_url = poster_image
        self.trailer_youtube_url = url_trailer
