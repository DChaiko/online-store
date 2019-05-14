from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', related_query_name='user', blank=True, null=True)
    create_date = models.DateField('Дата внесения', auto_now=False, auto_now_add=True)


class BookInCart(models.Model):
    cart = models.ForeignKey("cart.Cart", verbose_name=("Корзина"), on_delete=models.CASCADE)
    book = models.ForeignKey("books.Book", verbose_name=("Книга"), on_delete=models.CASCADE)
    quantity = models.IntegerField('количество', default=1)