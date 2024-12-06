# library_manager/utils/formatting.py

def format_book_data(data: dict) -> str:
    title = data.get("title", "Unknown Title")
    author = data.get("author", "Unknown Author")
    genre = data.get("genre", "Unknown Genre")
    return f"Title: {title}, Author: {author}, Genre: {genre}"
