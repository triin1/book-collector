from django.contrib import admin
from .models import Book, Read, Genre

# Register your models here:

admin.site.register(Book)
admin.site.register(Read)
admin.site.register(Genre)
