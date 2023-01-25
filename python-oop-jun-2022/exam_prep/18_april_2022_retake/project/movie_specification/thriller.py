from project.movie_specification.movie import Movie


class Thriller(Movie):
    AGE_RESTRICTION = 16
    MOVIE_GENRE = 'Thriller'

    def __init__(self, title: str, year: int, owner: object, age_restriction=16):
        super().__init__(title, year, owner, age_restriction)
