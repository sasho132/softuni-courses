from unittest import TestCase, main

from project.movie import Movie


class MovieTests(TestCase):
    def test_init(self):
        name = 'Name'
        year = 2020
        rating = 8.6
        movie = Movie(name, year, rating)
        self.assertEqual(movie.name, name)
        self.assertEqual(movie.year, year)
        self.assertEqual(movie.rating, rating)
        self.assertListEqual([], movie.actors)

    def test_init_with_name_empty_string_raise(self):
        name = ''
        year = 2020
        rating = 8.6
        with self.assertRaises(ValueError) as error:
            movie = Movie(name, year, rating)

        self.assertEqual("Name cannot be an empty string!", str(error.exception))

    def test_init_with_invalid_year_raise(self):
        name = 'Name'
        year = 1880
        rating = 8.6
        with self.assertRaises(ValueError) as error:
            movie = Movie(name, year, rating)
        self.assertEqual("Year is not valid!", str(error.exception))

    def test_add_actor_with_existing_name(self):
        name = 'Name'
        year = 2020
        rating = 8.6
        actor_name = 'Actor'
        movie = Movie(name, year, rating)
        movie.add_actor(actor_name)
        actual_result = movie.add_actor(actor_name)
        expected_result = f"{actor_name} is already added in the list of actors!"
        self.assertEqual(actual_result, expected_result)

    def test_add_actor_with_not_existing_name(self):
        name = 'Name'
        year = 2020
        rating = 8.6
        movie = Movie(name, year, rating)
        actor_name = 'Actor'
        movie.add_actor(actor_name)
        actual_result = movie.actors
        expected_result = [actor_name]
        self.assertListEqual(expected_result, actual_result)

    def test_gt_other_rating_with_first_rating_is_grater(self):
        name = 'Name'
        name2 = 'Name2'
        year = 2020
        year2 = 2021
        rating = 8.6
        rating2 = 8.0
        movie = Movie(name, year, rating)
        movie2 = Movie(name2, year2, rating2)
        actual_result = movie > movie2
        expected_result = f'"{movie.name}" is better than "{movie2.name}"'
        self.assertEqual(expected_result, actual_result)

    def test_gt_other_rating_with_second_rating_is_grater(self):
        name = 'Name'
        name2 = 'Name2'
        year = 2020
        year2 = 2021
        rating = 8.6
        rating2 = 9.0
        movie = Movie(name, year, rating)
        movie2 = Movie(name2, year2, rating2)
        actual_result = movie > movie2
        expected_result = f'"{movie2.name}" is better than "{movie.name}"'
        self.assertEqual(expected_result, actual_result)

    def test_repr(self):
        name = 'Name'
        year = 2020
        rating = 8.6
        actor1 = 'actor1'
        actor2 = 'actor2'
        movie = Movie(name, year, rating)
        movie.add_actor(actor1)
        movie.add_actor(actor2)
        expected_result = f"Name: {movie.name}\nYear of Release: {movie.year}\n" \
                          f"Rating: {movie.rating:.2f}\nCast: {', '.join(movie.actors)}"
        actual_result = repr(movie)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
