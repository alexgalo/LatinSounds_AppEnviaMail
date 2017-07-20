from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.

class SongPost(models.Model):
    titulo= models.CharField(max_length=150)
    autor= models.CharField(max_length=150)
    letra= models.TextField()
    liga= models.CharField(max_length=150)
    fecha= models.DateTimeField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo, self.autor
