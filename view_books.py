import json
import os

class BookViewer:
    _booklistfile="books.json"

    def __init__(self):
        self._books=self._load_books()

    def _load_books(self):
        if os.path.exists(self._booklistfile):
            with open(self._booklistfile, "r", encoding="utf-8") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("eror: books.json problematic")
                    return {}
        return {}

    def view_books(self):
        if not self._books:
            print("kono boi nai")
            return

        for isbn, book in self._books.items():
            print(f"Book title: {book.get('title', 'N/A')}")
            print(f"Author: {book.get('author', 'N/A')}")
            print(f"Genre: {book.get('genre', 'N/A')}")
            print(f"Stock count: {book.get('stock', 'N/A')}")
            print(f"publisher: {book.get('publisher', 'N/A')}")
            print(f"price {book.get('price', 'N/A')}")
            print(f"ISBN: {isbn}\n")
            #print("\n")

