from directory.models import Author
from directory.models import Serie
from directory.models import Genre
from directory.models import Publisher
from books.models import Book


def create_author(data):
    obj = Author.objects.create(name = 'Author Name', description = '')
    obj.save()

def delete_author(data):
    obj = Author.objects.get(name = 'Author Name')
    obj.delete()

def count(data):
    Author.objects.count()

def generator(data):
    for i in range(1,10):
        obj = Author.objects.create(name = 'name' + str(i), description = i)
        obj.save()

def filter(data):
    Author.objects.filter(name__istartswith = 'name').all()

dict = {
    'book_name':'book',
    'price':300,
    'author':'Лев Толстой',
    'serie':'Гарри Поттер',
    'genre':'Фантастика',
    'pub_year':1990,
    'pages':500,
    'binding':'твердый',
    'form':'фвафп',
    'isbn':315125,
    'weigth':200,
    'publisher':'Эксмо',
    'availability':15,
    'activ':'True',
    'rating':3,
    }

def new_book(dict):
    obj, created = Author.objects.get_or_create(name=dict['author'])
    obj, created = Serie.objects.get_or_create(name=dict['serie'])
    obj, created = Genre.objects.get_or_create(name=dict['genre'])
    obj, created = Publisher.objects.get_or_create(name=dict['publisher'])

    
    obj = Book.objects.create(book_name=dict['book_name'], price=dict['price'], author=obj.author, serie=obj.serie, genre=obj_genre, pub_year=dict['pub_year'], \
        pages=dict['pages'], binding=dict['binding'], form=dict['form'], isbn=dict['isbn'], weigth=dict['weigth'], publisher=obj_publisher, availability=dict['availability'], \
            activ=dict['activ'], rating=dict['rating'])
    obj.save()


def upd_create(name):
    obj. created = Author.objects.update_or_create(name=name)

