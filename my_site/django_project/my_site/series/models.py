from django.db import models

# Create your models here.

class Serie(models.Model):
    serie = models.CharField('название серии', null=False, blank=False, max_length=30)

    def __str__(self):
        return self.serie