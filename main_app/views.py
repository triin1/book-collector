from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book, Genre
from .forms import ReadForm

# Create your views here:

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {
        'books': books
    })

def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    read_form = ReadForm()
    genre_ids = book.genres.all().values_list('id')
    available_genres = Genre.objects.exclude(id__in=genre_ids)
    return render(request, 'books/detail.html', {
        'book': book,
        'read_form': read_form,
        'available_genres': available_genres
    })

def add_genre(request, book_id, genre_id):
    Book.objects.get(id=book_id).genres.add(genre_id)
    return redirect('detail', book_id=book_id)

def remove_genre(request, book_id, genre_id):
    Book.objects.get(id=book_id).genres.remove(genre_id)
    return redirect('detail', book_id=book_id)

class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class BookEdit(UpdateView):
    model = Book
    fields = '__all__'

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'

def add_read(request, book_id):
    read_form = ReadForm(request.POST)
    if read_form.is_valid():
        new_read = read_form.save(commit=False)
        new_read.book_id = book_id
        new_read.save()
    return redirect('detail', book_id=book_id) 

class GenreList(ListView):
    model = Genre

class GenreCreate(CreateView):
    model = Genre
    fields = '__all__'

class GenreUpdate(UpdateView):
    model = Genre
    fields = '__all__'

class GenreDelete(DeleteView):
    model = Genre
    success_url = '/genres/'