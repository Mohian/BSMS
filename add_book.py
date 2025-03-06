import json
import os
from datetime import datetime

class TotalManager:
    _booklistfile="books.json"

    def __init__(self):
        self._books=self._loadbooks()

    def _loadbooks(self):
        if os.path.exists(self._booklistfile):
            with open(self._booklistfile, "r", encoding="utf-8") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return {}
        return {}

    def _savebooks(self):
        existing_books=self._loadbooks()
        existing_books.update(self._books)
        with open(self._booklistfile, "w", encoding="utf-8") as file:
            json.dump(existing_books, file, indent=4)

    def add_book(self):
        while True:
            isbn=input("enter the isbn number (i.e: 12345): ")
            if not isbn.isdigit():  
             print("error: isbn must be a number!!.")
            else:
                break

        if self._book_exists(isbn):
            print("Ooops! Book already exists.")
            return

        print("***New Book Entry***")
        title=input("enter book title:")
        author=input("enter author name:")
        genre=input("enter genre: ")
        stock=input("enter the stock: ")
        price=input("enter the price")
        publisher=input("enter the publisher")

        while True:
            year=input("publication date (DD/MM/YYYY format): ")
            if not self._validatedate(year):  
                print("error: Invalid date, doya kore abar year din")
            else:
                break

        self._books[isbn]={
            "title": title,
            "author": author,
            "genre": genre,
            "year": year,
            "stock":stock,
            "price":price,
            "publisher":publisher
        }

        self._savebooks()
        print("Book added")

    def _book_exists(self, isbn):
        return isbn in self._loadbooks()

    def _validatedate(self, date_str):
        try:
            datetime.strptime(date_str, "%d/%m/%Y") 
            return True
        except ValueError:
            return False
