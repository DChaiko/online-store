from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', related_query_name='user', blank=True, null=True)
    create_date = models.DateField('Дата внесения', auto_now=False, auto_now_add=True)

    @property
    def price_calc(self):
        price = 0
        for book in self.user_cart.all():
            price += book.price
        return price 

    def number_of_books(self):
        total = 0
        for book in self.user_cart.all():
            total += book.quantity
        return total

class BookInCart(models.Model):
    cart = models.ForeignKey("cart.Cart", verbose_name=("Корзина"), related_name='user_cart', on_delete=models.CASCADE)
    book = models.ForeignKey("books.Book", verbose_name=("Книга"), related_name='book_in_cart', on_delete=models.CASCADE)
    quantity = models.IntegerField('количество', default=1)

    def __str__(self):
        #return (self.cart, self.book)
        return '{} {}'.format(self.cart, self.book)

    # @property
    # def price_calc(self):
    #     price = 'fdadgag'
    #     for book in self.user_cart.all():
    #         price += self.book.price
    #     return price 

    @property
    def price_of_books(self):
        price = self.quantity * self.book.price
        return price 

    
