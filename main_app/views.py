from django.shortcuts import render

# temporary data:
books = [
    {'title': 'My Brilliant Friend', 'author': 'Elena Ferrante', 'format': 'Paperback', 'language': 'English', 'publish_year': '2012'},
    {'title': 'Banker to the Poor', 'author': 'Muhammad Yunus', 'format': 'Ebook', 'language': 'English', 'publish_year': '1999'},
    {'title': 'Ready Player One', 'author': 'Ernest Cline', 'format': 'Audiobook', 'language': 'English', 'publish_year': '2012'},
]

# Create your views here:

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def books_index(request):
    return render(request, 'books/index.html')
