from unittest import TestCase, main

from project.bookstore import Bookstore


class BookstoreTesting(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(10)

    def test_init(self):
        self.assertEqual(self.bookstore.books_limit, 10)
        self.assertDictEqual(self.bookstore.availability_in_store_by_book_titles, {})
        self.assertEqual(self.bookstore.total_sold_books, 0)

    def test_books_limit_with_limit_equal_to_0_raise(self):
        value = 0
        with self.assertRaises(ValueError) as error:
            self.bookstore.books_limit = value
        self.assertEqual(f"Books limit of {value} is not valid", str(error.exception))

    def test_books_limit_with_limit_bellow_0_raise(self):
        value = -10
        with self.assertRaises(ValueError) as error:
            self.bookstore.books_limit = value
        self.assertEqual(f"Books limit of {value} is not valid", str(error.exception))

    def test_receive_book_with_books_with_limit_reached_raise(self):
        self.bookstore.receive_book('BookTitle', 10)
        with self.assertRaises(Exception) as error:
            self.bookstore.receive_book('BookTitle2', 11)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(error.exception))
        self.assertDictEqual({'BookTitle': 10}, self.bookstore.availability_in_store_by_book_titles)

    def test_receive_book_with_books_bellow_the_limit(self):
        total_number = 4
        book_title = 'BookTitle'
        self.assertDictEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.bookstore.receive_book(book_title, 3)
        actual_message = self.bookstore.receive_book(book_title, 1)
        expected_result = {book_title: 4}
        expected_message = f"{total_number} copies of {book_title} are available in the bookstore."
        self.assertDictEqual(self.bookstore.availability_in_store_by_book_titles, expected_result)
        self.assertEqual(actual_message, expected_message)

    def test_len_books_expect_proper_books_count(self):
        books_quantity = 5
        book_title = 'BookTitle'
        book_title2 = 'BookTitle2'
        self.bookstore.receive_book(book_title, 3)
        self.bookstore.receive_book(book_title2, 2)
        self.assertEqual(len(self.bookstore), books_quantity)

    def test_sell_book_with_invalid_title_raise(self):
        searched_title = 'SearchedTitle'
        self.bookstore.receive_book('BookTitle', 3)
        self.assertNotIn(searched_title, self.bookstore.availability_in_store_by_book_titles)
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book(searched_title, 1)

        expected_message = f"Book {searched_title} doesn't exist!"
        self.assertEqual(expected_message, str(error.exception))
        self.assertDictEqual({'BookTitle': 3}, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_with_invalid_quantity(self):
        books_quantity = 3
        book_title = 'BookTitle'
        self.bookstore.receive_book(book_title, books_quantity)
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book(book_title, 5)
        expected_message = f"{book_title} has not enough copies to sell. Left: {books_quantity}"
        self.assertEqual(expected_message, str(error.exception))
        self.assertDictEqual({book_title: books_quantity}, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_with_valid_quantity(self):
        books_quantity = 3
        books_sell_quantity = 3
        book_title = 'BookTitle'
        self.bookstore.receive_book(book_title, books_quantity)
        self.assertEqual(self.bookstore.total_sold_books, 0)
        actual_message = self.bookstore.sell_book(book_title, books_sell_quantity)
        expected_dict = {book_title: 0}
        self.assertDictEqual(self.bookstore.availability_in_store_by_book_titles, expected_dict)
        self.assertEqual(self.bookstore.total_sold_books, 3)
        expected_message = f"Sold {books_sell_quantity} copies of {book_title}"
        self.assertEqual(expected_message, actual_message)

    def test_str(self):
        books_quantity = 3
        book_title = 'BookTitle'
        books_sell_quantity = 1
        self.bookstore.receive_book(book_title, books_quantity)
        self.bookstore.sell_book(book_title, books_sell_quantity)
        book_quantity_after_sell = 2

        expected_message = f"Total sold books: {books_sell_quantity}\n" \
                           f"Current availability: {len(self.bookstore)}\n" \
                           f" - {book_title}: {book_quantity_after_sell} copies"
        self.assertEqual(expected_message, str(self.bookstore))


if __name__ == "__main__":
    main()
