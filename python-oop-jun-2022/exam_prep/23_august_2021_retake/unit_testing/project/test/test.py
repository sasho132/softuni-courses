from unittest import TestCase, main

from project.library import Library


class LibraryTests(TestCase):
    NAME = 'Name'

    def setUp(self) -> None:
        self.library = Library(self.NAME)

    def test_init(self):
        self.assertEqual(self.library.name, self.NAME)
        self.assertDictEqual(self.library.books_by_authors, {})
        self.assertDictEqual(self.library.readers, {})

    def test_name_init_with_empty_string_raise(self):
        with self.assertRaises(ValueError) as error:
            self.library.name = ''

        self.assertEqual("Name cannot be empty string!", str(error.exception))

    def test_add_book(self):
        self.library.add_book('Author', 'Title')
        actual_result = self.library.books_by_authors
        expected_result = {'Author': ['Title']}
        self.assertDictEqual(expected_result, actual_result)

    def test_add_reader_with_existing_reader(self):
        name = 'Name'
        self.library.add_reader(name)
        actual_result = self.library.add_reader(name)
        expected_result = f"{name} is already registered in the {self.library.name} library."
        self.assertEqual(actual_result, expected_result)

    def test_add_reader_to_readers(self):
        name = 'Name'
        self.library.add_reader(name)
        actual_result = self.library.readers
        expected_result = {name: []}
        self.assertEqual(actual_result, expected_result)

    def test_rent_book_with_not_existing_reader(self):
        reader_name = 'Name'
        actual_result = self.library.rent_book(reader_name, 'Author', 'Title')
        expected_result = f"{reader_name} is not registered in the {self.library.name} Library."
        self.assertEqual(actual_result, expected_result)

    def test_rent_book_with_not_existing_book_author(self):
        self.library.add_reader('Name')
        book_author = 'Author'
        actual_result = self.library.rent_book('Name', book_author, 'Title')
        expected_result = f"{self.library.name} Library does not have any {book_author}'s books."
        self.assertEqual(actual_result, expected_result)

    def test_rent_book_with_not_existing_book_title(self):
        title = 'Test'
        book_author = 'Author'
        self.library.add_reader('Name')
        self.library.add_book('Author', 'Title')
        actual_result = self.library.rent_book('Name', 'Author', title)
        expected_result = f"""{self.library.name} Library does not have {book_author}'s "{title}"."""
        self.assertEqual(actual_result, expected_result)

    def test_rent_book_with_proper_data(self):
        book_title = 'Title'
        book_author = 'Author'
        name = 'Name'
        self.library.add_book(book_author, book_title)
        self.library.add_reader(name)
        self.library.rent_book(name, book_author, book_title)

        self.assertEqual(self.library.readers[name], [{book_author: book_title}])
        self.assertEqual(self.library.books_by_authors, {'Author': []})


if __name__ == '__main__':
    main()
