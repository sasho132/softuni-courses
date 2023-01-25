from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author, book_name, days_to_return, user: User):
        for auth, book_names in self.books_available.items():
            if book_name in book_names:
                if user.username not in self.rented_books:
                    self.rented_books[user.username] = {}
                self.rented_books[user.username][book_name] = days_to_return
                user.books.append(book_name)
                self.books_available[author].remove(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"

        book_returning_time = None
        for user, book in self.rented_books.items():
            for name, days in book.items():
                if name == book_name:
                    book_returning_time = days

        return f'The book "{book_name}" is already rented and will be available in {book_returning_time} days!'

    def return_book(self, author, book_name, user: User):
        if book_name in user.books:
            del self.rented_books[user.username][book_name]
            self.books_available[author].append(book_name)
            user.books.remove(book_name)
        return f"{user.username} doesn't have this book in his/her records!"
