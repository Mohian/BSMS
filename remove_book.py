import json
import os

class BookRemover:
    _booklistfile = "books.json"

    def __init__(self):
        self._books = self._load_books()

    def _load_books(self):
        if os.path.exists(self._booklistfile):
            with open(self._booklistfile, "r", encoding="utf-8") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return {}
        return {}

    def _save_books(self):
        with open(self._booklistfile, "w", encoding="utf-8") as file:
            json.dump(self._books, file, indent=4)

    def removebook(self):
        isbn = input("enter the ISBN number of the book to remove: ")

        if isbn not in self._books:
            print(f"error: No book found with ISBN {isbn}.")
            return

        #title nicchi
        book_title = self._books[isbn]["title"]
        
        
        del self._books[isbn]
        self._save_books()

        
        print(f"{isbn}'{book_title}' has been removed.")
