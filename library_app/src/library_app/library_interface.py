from abc import ABC, abstractmethod
from typing import List
from .book import Book


# ISP + DIP:
# The interface defines only those methods that are necessary for working with the library.
# This allows high-level modules (such as LibraryManager) to depend on the abstraction rather than on a concrete class.
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, title: str, author: str, year: str) -> None: ...

    @abstractmethod
    def remove_book(self, title: str) -> None: ...

    @abstractmethod
    def get_books(self) -> List[Book]: ...
