# -*- coding: utf-8 -*-
import Movie
import fresh_tomatoes as ft

'''
    movie_list: a list containing all the movie object
    film0, film1, film2, film3: are instances of Movie.movie
'''
movie_list = []

film0 = Movie.movie(
        "Harry Potter and the Deathly Hallows: Part 2",
        "Harry, Ron and Hermione search for Voldemort's remaining Horcruxes in their effort " \
        "to destroy the Dark Lord as the final battle rages on at Hogwarts.",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY2MTk3MDQ1N15BMl5BanBnXkFtZTcwMzI4NzA2NQ@@._V1_SY1000_SX675_AL_.jpg",
        "https://www.youtube.com/watch?v=5NYt1qirBWg")
film1 = Movie.movie(
        "Eternal Sunshine of the Spotless Mind",
        "When their relationship turns sour, a couple undergoes a procedure to have each "\
        "other erased from their memories. But it is only through the process of loss that they discover what they had to begin with.",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY4NzcwODg3Nl5BMl5BanBnXkFtZTcwNTEwOTMyMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
        "https://www.youtube.com/watch?v=yE-f1alkq9I")
film2 = Movie.movie(
        "Fight Club",
        "An insomniac office worker, looking for a way to change his life, crosses paths with" \
        " a devil-may-care soap maker, forming an underground fight club that evolves into something"\
        " much, much more.",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BNGM2NjQxZTAtMmU5My00YTk5LWFmOWMtYjZlYzk4YzMwNjFlXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
        "https://www.youtube.com/watch?v=SUXWAEX2jlg")
film3 = Movie.movie(
        "Forrest Gump",
        "Forrest Gump, while not intelligent, has accidentally been present at many historic moments" \
        ", but his true love, Jenny Curran, eludes him.",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,757,1000_AL_.jpg",
        "https://www.youtube.com/watch?v=bLvqoHBptjg")

movie_list.append(film0)
movie_list.append(film1)
movie_list.append(film2)
movie_list.append(film3)

ft.open_movies_page(movie_list)
