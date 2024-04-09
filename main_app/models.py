from django.db import models
from django.urls import reverse

# Create your models here:

class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=256)
    format = models.CharField(max_length=256)
    language = models.CharField(max_length=256)
    publish_year = models.IntegerField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'book_id': self.id })

    def __str__(self):
        return self.title

