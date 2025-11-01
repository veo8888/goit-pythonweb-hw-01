# SRP: The Book class is only responsible for storing and presenting data about a book.
class Book:
    def __init__(self, title, author, year):
        self.title = title.strip()
        self.author = author.strip()
        self.year = year.strip()

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"
