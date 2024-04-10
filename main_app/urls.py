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
    path('books/<int:book_id>/add_genre/<int:genre_id>/', views.add_genre, name='add_genre'),
    path('books/<int:book_id>/remove_genre/<int:genre_id>/', views.remove_genre, name='remove_genre'),
    
    path('genres/', views.GenreList.as_view(), name='genres_index'),
    path('genres/create/', views.GenreCreate.as_view(), name='genres_create'),
    path('genres/<int:pk>/update/', views.GenreUpdate.as_view(), name='genre_update'),
    path('genres/<int:pk>/delete/', views.GenreDelete.as_view(), name='genre_delete'),

    # # Attempt to add genres at the bottom of the field:
    # path('books/<int:book_id>/create_genre/<int:genre_id>/', views.create_genre, name='create_genre'),
]