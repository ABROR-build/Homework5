from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms


# read cRud
def list_books(request):
    books = models.Books.objects.all()
    context = {
        'books': books
    }
    return render(request, 'dashboard.html', context=context)


def about_book(request, pk):
    details = models.Books.objects.get(pk=pk)
    context = {
        'details': details
    }
    return render(request, 'about_book.html', context=context)


def list_genres(request):
    genres = models.Genres.objects.all()
    context = {
        'genres': genres
    }
    return render(request, 'genres.html', context=context)


def about_genre(request, pk):
    details = models.Books.objects.filter(genre=pk)
    context = {
        'genre_details': details
    }
    return render(request, 'about_genres.html', context=context)


def list_authors(request):
    authors = models.BookAuthor.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'authors.html', context=context)


def about_author(request, pk):
    author_details = models.Author.objects.get(pk=pk)
    context = {
        'author_details': author_details
    }
    return render(request, 'about_author.html', context=context)


def author_books(request, pk):
    author_books = models.BookAuthor.objects.filter(book=pk)
    context = {
        'author_books': author_books
    }
    return render(request, 'author_books.html', context=context)


# create Crud
def add_author(request):
    form = forms.CreateAuthor(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('match_author')
    context = {
        'form': form
    }
    return render(request, 'add_author.html', context=context)


def add_book(request):
    form = forms.AddBook(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('list_books')
    context = {
        'form': form
    }
    return render(request, 'add_book.html', context=context)


def book_and_author_march(request):
    form = forms.BookAuthorMatch(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('list_books')
    context = {
        'form': form
    }
    return render(request, 'book_and_author.html', context=context)


# update crUd
def edit_author(request, pk):
    objects = get_object_or_404(models.Author, pk=pk)
    if request.method == 'POST' or 'GET':
        form = forms.CreateAuthor(request.POST, instance=objects)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = forms.CreateAuthor(instance=objects)
    context = {
        'forms': form
    }
    return render(request, 'edit_author.html', context=context)


def edit_book(request, pk):
    objects = get_object_or_404(models.Books, pk=pk)
    if request.method == 'POST' or 'GET':
        form = forms.AddBook(request.POST, instance=objects)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = forms.AddBook(instance=objects)
    context = {
        'form': form
    }
    return render(request, 'edit_book.html', context=context)


# delete cruD
def delete_author(request, pk):
    obj = get_object_or_404(models.Author, pk=pk)
    if request.method == 'POST' or 'GET':
        obj.delete()
        return render(request, 'delete_auth.html')
