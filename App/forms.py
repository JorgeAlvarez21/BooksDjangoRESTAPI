from django import forms
import datetime as dt
from .models import Book


class new_book_insert(forms.Form):
    title = forms.CharField(max_length=50, required=True)
    author = forms.CharField(max_length=50, required=True)
    genre = forms.CharField(max_length=50, required=True)
    date = forms.DateField(initial=dt.date.today, required=True)
    release_date = forms.DateField(required=True)


books_list = Book.objects.all()
books_ls = []
for book in books_list:
    if not books_ls:
        books_ls.append(("default", "------------------"))
    else:
        item = books_ls.append((book.id, f'{book.title}, By: {book.author}'))

class BookForm(forms.Form):
    book_choice = forms.ChoiceField(choices=books_ls,
                                    label="",
                                    required=False,
                                    initial="default")
