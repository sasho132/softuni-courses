from project.movie_specification.movie import Movie


class Fantasy(Movie):
    AGE_RESTRICTION = 6
    MOVIE_GENRE = 'Fantasy'

    def __init__(self, title: str, year: int, owner: object, age_restriction=6):
        super().__init__(title, year, owner, age_restriction)
