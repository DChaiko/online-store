from django.contrib import admin
from .models import Author
from .models import Series
from .models import Genre
from .models import Publisher
# Register your models here.

admin.site.register(Author)
admin.site.register(Series)
admin.site.register(Genre)
admin.site.register(Publisher)