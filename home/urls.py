from django.urls import path
from .views import single_book, search_book, book_list, search


urlpatterns = [
    path('books', book_list),
    path('', search_book),
    path('book/<int:pk>', single_book),
    path('search/', search),
]