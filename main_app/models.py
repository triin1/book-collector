from django.db import models
from django.urls import reverse

# Create your models here:

ACTIVITIES = (
    ('Start', 'Started reading'),
    ('Finish', 'Finished reading'),
)

class Genre(models.Model):
    name = models.CharField(max_length=256)

    def get_absolute_url(self):
        return reverse('genres_index')

    def __str__(self):
        return self.name    

class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=256)
    format = models.CharField(max_length=256)
    language = models.CharField(max_length=256)
    publish_year = models.IntegerField()
    genres = models.ManyToManyField(Genre)

    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'book_id': self.id })

    def __str__(self):
        return self.title

class Read(models.Model):
    date = models.DateField()
    activity = models.CharField(
        max_length=256,
        choices=ACTIVITIES,
        default=ACTIVITIES[0][0]
        )
    review = models.TextField(max_length=400, blank=True)

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_activity_display()} on {self.date}"