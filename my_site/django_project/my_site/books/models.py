from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField('Название книги', max_length=100)
    cover = models.ImageField('Обложка', null=True, blank=True)
    price = models.IntegerField('Цена', blank=True, null=True)
    author = models.ManyToManyField("authors.Author", blank=True, verbose_name='Автор')
    serie = models.ForeignKey("series.Serie", on_delete=models.PROTECT, blank=True, null=True, verbose_name='Серия')
    genre = models.ForeignKey("genres.Genre", on_delete=models.PROTECT, blank=True, null=True, verbose_name='Жанр')
    pub_year = models.IntegerField('Год публикации', blank=True, null=True)
    pages = models.IntegerField('Количество страниц', blank=True, null=True)
    binding = models.CharField('Переплет', max_length=30)
    form = models.CharField('Формат',max_length=30)
    isbn = models.CharField('ISBN', max_length=30)
    weigth = models.IntegerField('Вес(гр)', blank=True, null=True)
    publisher = models.ForeignKey("publishers.Publisher", on_delete=models.PROTECT,  blank=True, null=True, verbose_name='Издатель')
    availability = models.IntegerField('Количество книг в наличие', blank=True, null=True)
    activ = models.BooleanField('Активный', default=True)
    rating = models.IntegerField('Рейтинг', blank=True, null=True)
    add_date = models.DateField('Дата внесения в каталог', auto_now=False, auto_now_add=True, blank=True, null=True)
    change_date = models.DateField('Дата последнего изменения', auto_now=True, auto_now_add=False, blank=True, null=True)

    description = models.TextField(null=True, blank=True)
    



    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

