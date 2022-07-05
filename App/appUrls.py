
from django.urls import path
from .views import book_list, book_detail, form_home
from .forms import new_book_insert

urlpatterns = [
    path('books/', book_list, name='list'),
    path('detail/<int:pk>/', book_detail, name='detail'),
    #path('home/', index_home, name= 'home'),
    path('home/', form_home, name='home insert form'),

]