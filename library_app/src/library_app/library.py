import logging
from typing import List
from .book import Book
from .library_interface import LibraryInterface


# OCP + LSP:
# The Library class implements the LibraryInterface interface,
# therefore it can be replaced by any other class with the same interface (LSP),
# and can be extended with new functionality (search, sorting, etc.) without changing existing code (OCP).
class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, title: str, author: str, year: str) -> None:
        if any(book.title.lower() == title.lower() for book in self.books):
            logging.info(f"⚠️  Book '{title}' already exists.")
            return

        self.books.append(Book(title, author, year))
        logging.info(f"✅ Book '{title}' successfully removed!")

    def remove_book(self, title: str) -> None:
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                logging.info(f"🗑️  Book '{title}' successfully removed!")
                return

        logging.info(f"❌ Book '{title}' not found in the library.")

    def get_books(self) -> List[Book]:
        return self.books
