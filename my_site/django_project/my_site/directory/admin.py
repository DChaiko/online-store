from django.contrib import admin
from .models import Author
from .models import Serie
from .models import Genre
from .models import Publisher
# Register your models here.

admin.site.register(Author)
admin.site.register(Serie)
admin.site.register(Genre)
admin.site.register(Publisher)