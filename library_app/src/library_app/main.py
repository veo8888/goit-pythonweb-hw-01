import logging
from .library import Library
from .manager import LibraryManager
from .utils import input_required


# Main module: the entry point to the program.
# Here instances of classes implementing the DIP and OCP principles are created.
def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    library = Library()
    manager = LibraryManager(library)

    logging.info("📚 Welcome to Simple Library!")
    logging.info("Enter command (add, remove, show, exit):")

    while True:
        command = input("> ").strip().lower()

        match command:
            case "add":
                title = input_required("Enter book title: ")
                author = input_required("Enter book author: ")
                year = input_required("Enter book year: ")
                manager.add_book(title, author, year)

            case "remove":
                title = input_required("Enter book title to remove: ")
                manager.remove_book(title)

            case "show":
                manager.show_books()

            case "exit":
                logging.info("👋 Bye!")
                break

            case _:
                logging.info(
                    "⚠️  Invalid command. Try again. (add, remove, show, exit)."
                )


if __name__ == "__main__":
    main()
