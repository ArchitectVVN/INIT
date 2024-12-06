# library_manager/report.py

from .utils.formatting import format_book_data

def generate_report(library) -> str:
    """Генерирует отчет о всех книгах в библиотеке."""
    books = library.get_all_books()
    if not books:
        return "No books in the library."
    report_lines = ["Library Report:"]
    for book in books:
        report_lines.append(format_book_data(book))
    return "\n".join(report_lines)
