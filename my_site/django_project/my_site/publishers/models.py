from django.db import models

# Create your models here.

class Publisher(models.Model):
    pub = models.CharField('издательство', null=False, blank=False, max_length=30)

    def __str__(self):
        return self.pub