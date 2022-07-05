from django.db import models
import datetime as dt


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    release_date = models.DateField()
    def __str__(self):
        return self.title

