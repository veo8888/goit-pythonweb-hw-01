from .library_interface import LibraryInterface


# DIP:
# The LibraryManager class depends on an abstraction (LibraryInterface) rather than on a concrete library implementation.
# This allows you to use any implementation of the interface without changing the manager code.
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title, author, year):
        self.library.add_book(title, author, year)

    def remove_book(self, title):
        self.library.remove_book(title)

    def show_books(self):
        books = self.library.get_books()
        if not books:
            print("🚫 The library is empty.")
        else:
            for book in books:
                print(book)
