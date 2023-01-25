from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        if self.__find_user_by_username(username):
            raise Exception("User already exists!")

        user = User(username, age)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user = self.__find_user_by_username(username)
        if user is None:
            raise Exception("This user does not exist!")
        if user != movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.__find_user_by_username(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            if key == 'title':
                movie.title = value
            elif key == 'year':
                movie.year = value
            elif key == 'age_restriction':
                movie.AGE_RESTRICTION = value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)

        if movie.owner == user:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))

        result = '\n'.join(m.details() for m in sorted_movies)
        return result

    def __str__(self):
        result = ''
        if not self.users_collection:
            result += "All users: No users.\n"
        else:
            result += f"All users: {', '.join(x.username for x in self.users_collection)}\n"

        if not self.movies_collection:
            result += "All movies: No movies.\n"
        else:
            result += f"All movies: {', '.join(x.title for x in self.movies_collection)}\n"

        return result.strip()

    def __find_user_by_username(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user
        return None
