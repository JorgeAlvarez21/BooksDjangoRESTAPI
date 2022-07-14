from models import Book

def dropdown_data():
    instance = Book

    titles = [obj.title for obj in books_list]
    authors = [obj.author for obj in books_list]

    return books_list