from django.urls import path
from . import views

urlpatterns = [
    # read
    path('', views.list_books, name='list_books'),
    path('about/<int:pk>/', views.about_book, name='about_book'),
    path('genres/', views.list_genres, name='list_genres'),
    path('about_genres/<int:pk>/', views.about_genre, name='about_genre'),
    path('authors/', views.list_authors, name='list_authors'),
    path('author_about/<int:pk>/', views.about_author, name='about_author'),
    path('author_books/<int:pk>/', views.author_books, name='author_books'),

    # create
    path('add_author/', views.add_author, name='create_author'),
    path('add_book/', views.add_book, name='add_book'),
    path('match_author/', views.book_and_author_march, name='match_author'),

    # update
    path('edit/author/<int:pk>', views.edit_author, name='edit_author'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),

    # delete
    path('delete/author/<int:pk>', views.delete_author, name='delete_author')

]
