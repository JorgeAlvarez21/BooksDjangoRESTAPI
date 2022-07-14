from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import Context
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer

from .serializers import BookSerializer
from .models import Book
from rest_framework.parsers import JSONParser
from .forms import new_book_insert, BookForm


# Create your views here.

@csrf_exempt
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        content = JsonResponse(serializer.data, safe=False)
        return content

    elif request.method == 'POST':
        parsed_data = JSONParser().parse(request)
        serializer = BookSerializer(data=parsed_data, many=False)
        if serializer.is_valid():
            serializer.save()
            content = JsonResponse(serializer.data, status=201)
            return content
        return JsonResponse(serializer.errors, status=400)


# Getting details for one book by its ID, Updating and deleting.

# Get request for only one book, Needs pk = Private Key (ID)
@csrf_exempt
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except book.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(book)
        content = JsonResponse(serializer.data)
        return content

    # Updating a book
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
            content = JsonResponse(serializer.data)
            return content
        return JsonResponse(serializer.errors, status=400)
    # Deleting the book
    elif request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=204)

    # Home


def index_home(request):
    return HttpResponse('Welcome to the Api\'s homepage!')


def form_home(request):
    form = new_book_insert()
    choices_form = BookForm()
    context = {}

    if request.method == 'POST':

        input_form = new_book_insert(request.POST)
        choice_selected = BookForm(request.POST)

        if input_form.is_valid():
            title = input_form.cleaned_data['title']
            author = input_form.cleaned_data['author']
            genre = input_form.cleaned_data['genre']
            date = input_form.cleaned_data['date']
            release_date = input_form.cleaned_data['release_date']

            new_book = Book(title=title, author=author, genre=genre, date=date, release_date=release_date)
            new_book.save()

        if choice_selected.is_valid():
            try:
                book_id = choice_selected.cleaned_data['book_choice']
                if book_id != 'default':
                    book_obj = Book.objects.get(pk=book_id)
                    context['Book'] = book_obj
            except NameError:
                print('Book does not exist.')

        choices_form = BookForm()

    context["form"] = form
    context["choices_form"] = choices_form

    return render(request, 'home_form.html', context)
