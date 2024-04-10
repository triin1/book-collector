from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    path('books/', views.books_index, name='book_index'),
    path('books/<int:book_id>/', views.books_detail, name='detail'),
    path('books/create/', views.BookCreate.as_view(), name='books_create'),
    path('books/<int:pk>/update/', views.BookEdit.as_view(), name='books_edit'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='books_delete'),
    path('books/<int:book_id>/add_read/', views.add_read, name="add_read"),
    path('books/<int:book_id>/add_genre/<int:genre_id>', views.add_genre, name='add_genre'),
]