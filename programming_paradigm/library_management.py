class Book:
    """A class representing a book in a library."""
    
    def __init__(self, title, author):
        """
        Initialize a Book with title, author, and availability.
        
        Args:
            title (str): Book title
            author (str): Book author
        """
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        """
        Mark the book as checked out.
        
        Returns:
            bool: True if checkout succeeds, False if already checked out
        """
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True
    
    def return_book(self):
        """
        Mark the book as returned (available).
        
        Returns:
            bool: True if return succeeds, False if already returned
        """
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True
    
    def is_available(self):
        """
        Check if the book is available.
        
        Returns:
            bool: True if available, False if checked out
        """
        return not self._is_checked_out

class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize an empty library with a list of books."""
        self._books = []
    
    def add_book(self, book):
        """
        Add a book to the library's collection.
        
        Args:
            book (Book): Book instance to add
        """
        if isinstance(book, Book):
            self._books.append(book)
    
    def check_out_book(self, title):
        """
        Check out a book by title if available.
        
        Args:
            title (str): Title of the book to check out
        
        Returns:
            bool: True if checkout succeeds, False otherwise
        """
        for book in self._books:
            if book.title == title and book.is_available():
                return book.check_out()
        return False
    
    def return_book(self, title):
        """
        Return a book by title.
        
        Args:
            title (str): Title of the book to return
        
        Returns:
            bool: True if return succeeds, False otherwise
        """
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False
    
    def list_available_books(self):
        """
        Print all available books in the library.
        """
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")