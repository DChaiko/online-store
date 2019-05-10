from django.db import models

# Create your models here.

class Genre(models.Model):
    genre = models.CharField('жанр', null=False, blank=False, max_length=30)
    
    def __str__(self):
        return self.genre