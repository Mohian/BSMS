import json
import os

class BookSearcher:
    _booklistfile = "books.json"

    def __init__(self):
        self._books = self._load_books()

    def _load_books(self):
        if os.path.exists(self._booklistfile):
            with open(self._booklistfile, "r", encoding="utf-8") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("error: books.json is empty or corrupted.")
                    return {}
        return {}

    def search_book(self):
        isbn = input("Enter the ISBN number of the book to search: ")

        if isbn not in self._books:
            print(f"error: No book found with ISBN {isbn}.")
            return

        book = self._books[isbn]
        print("\nYahooo!!! khuje peyechhi broooh!!")
        print(f"Book title: {book.get('title', 'N/A')}")
        print(f"Author: {book.get('author', 'N/A')}")
        print(f"Genre: {book.get('genre', 'N/A')}")
        print(f"Stock count: {book.get('stock', 'N/A')}")
        print(f"ISBN: {isbn}")
