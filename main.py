# main.py

from library_manager import Library, generate_report

def main():
    # Создаем экземпляр библиотеки
    lib = Library()

    # Добавляем книги
    lib.add_book({"title": "1984", "author": "George Orwell", "genre": "Dystopia"})
    lib.add_book({"title": "Brave New World", "author": "Aldous Huxley", "genre": "Dystopia"})
    lib.add_book({"title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Fiction"})

    # Генерируем отчет
    print("Первоначальный отчет о книгах в библиотеке:\n")
    print(generate_report(lib))
    print()

    # Ищем книги по автору
    print("Поиск книг по автору 'Aldous Huxley':")
    found_books = lib.find_books(author="Aldous Huxley")
    for book in found_books:
        print(book)
    print()

    # Удаляем книгу "1984"
    print("Удаляем книгу '1984'...")
    lib.remove_book("1984")

    # Генерируем отчет после удаления книги
    print("Отчет после удаления '1984':\n")
    print(generate_report(lib))

if __name__ == "__main__":
    main()
