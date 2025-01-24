"""
Peter Botros
lab8.py
November 12 2024
"""

# This program will show the details about books.

author.py
class Author:
    def __init__(self, name: str, nationality: str, num_books_written: int):
        self.name = name
        self.nationality = nationality
        self.num_books_written = num_books_written

    def __str__(self):
        return f"Author: {self.name}, Nationality: {self.nationality}, Books Written: {self.num_books_written}"

    def write_new_book(self):
        self.num_books_written += 1

    def get_num_books_written(self):
        return self.num_books_written

    def set_num_books_written(self, count: int):
        if count >= 0:
            self.num_books_written = count
        else:
            print("Number of books cannot be negative.")

book.py
from author import Author

class Book:
    def __init__(self, title: str, genre: str, year: int, author: Author):
        self.title = title
        self.genre = genre
        self.year = year
        self.author = author

    def __str__(self):
        return f"Book: {self.title}, Genre: {self.genre}, Year: {self.year}, Author: {self.author.name}"

    def set_genre(self, new_genre: str):
        self.genre = new_genre

    def get_author_info(self):
        return str(self.author)

    def summary(self):
        return f"'{self.title}' by {self.author.name}, published in {self.year}. Genre: {self.genre}. Author Nationality: {self.author.nationality}"

main.py 

from author import Author
from book import Book

def main():
    # Creating an author
    author = Author(name="Gabriel Garcia Marquez", nationality="Colombian", num_books_written=10)
    
    # Creating a book and associating it with the author
    book = Book(title="One Hundred Years of Solitude", genre="Magical Realism", year=1967, author=author)

    # Using the __str__ method
    print(book)

    # Using a setter to change the genre of the book
    book.set_genre("Literary Fiction")
    print(f"Updated Genre: {book.genre}")

    # Using a getter to get author information
    print(book.get_author_info())

    # Demonstrating an action method by adding a new book to the author's count
    author.write_new_book()
    print(f"Books written after new book: {author.get_num_books_written()}")

    # Using the summary method
    print(book.summary())

if __name__ == "__main__":
    main()
