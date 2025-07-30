class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book.title}")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Removed: {title}")
                return
        print("Book not found")

    def display_books(self):
        if not self.books:
            print("Library is empty")
        for book in self.books:
            print(f"{book.title} by {book.author}")
