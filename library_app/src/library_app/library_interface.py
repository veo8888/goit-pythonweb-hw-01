from abc import ABC, abstractmethod


# ISP + DIP:
# The interface defines only those methods that are necessary for working with the library.
# This allows high-level modules (such as LibraryManager) to depend on the abstraction rather than on a concrete class.
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, title, author, year):
        pass

    @abstractmethod
    def remove_book(self, title):
        pass

    @abstractmethod
    def get_books(self):
        pass
