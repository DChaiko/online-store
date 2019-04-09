from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField('имя автора', null=False, blank=False, max_length=30)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Serie(models.Model):
    serie = models.CharField('название серии', null=False, blank=False, max_length=30)

    def __str__(self):
        return self.serie

class Genre(models.Model):
    genre = models.CharField('жанр', null=False, blank=False, max_length=30)
    
    def __str__(self):
        return self.genre

class Publisher(models.Model):
    pub = models.CharField('издательство', null=False, blank=False, max_length=30)

    def __str__(self):
        return self.pub

