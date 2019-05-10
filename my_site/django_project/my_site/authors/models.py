from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField('имя автора', null=False, blank=False, max_length=30)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name