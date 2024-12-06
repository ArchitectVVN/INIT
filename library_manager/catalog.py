# library_manager/catalog.py

from .utils.data_validation import validate_book_data

class Library:
    def __init__(self):
        # Храним книги в списке словарей: [{"title": ..., "author": ..., "genre": ...}, ...]
        self._books = []

    def add_book(self, data: dict) -> bool:
        """Добавляет книгу в библиотеку. Возвращает True, если успешно, иначе False."""
        if validate_book_data(data):
            self._books.append(data)
            return True
        return False

    def remove_book(self, title: str) -> bool:
        """Удаляет книгу по названию. Возвращает True, если книга была удалена, иначе False."""
        initial_count = len(self._books)
        self._books = [book for book in self._books if book.get("title") != title]
        return len(self._books) < initial_count

    def find_books(self, title: str = None, author: str = None, genre: str = None):
        """Ищет книги по названиям, автору или жанру. Возвращает список книг, подходящих под критерии."""
        results = self._books
        if title is not None:
            results = [b for b in results if b.get("title") == title]
        if author is not None:
            results = [b for b in results if b.get("author") == author]
        if genre is not None:
            results = [b for b in results if b.get("genre") == genre]
        return results

    def get_all_books(self):
        """Возвращает список всех книг."""
        return self._books
