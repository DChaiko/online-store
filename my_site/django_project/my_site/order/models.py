from django.db import models

# Create your models here.

class Order(models.Model):
    cart = models.ForeignKey("cart.Cart", verbose_name=("Корзина"), on_delete=models.CASCADE)
    status = models.ForeignKey("order.Status", verbose_name='Статус', on_delete=models.CASCADE)
    adress = models.CharField('Адресс', max_length=50)
    email = models.EmailField(("Email"), max_length=254, default='example@mail.com')
    contacts = models.IntegerField('Телефон')
    date_create = models.DateTimeField("Дата создания", auto_now_add=True, )
    
    
    def __str__(self):
            return "Заказ №" + str(self.pk) + " от " + self.date_create.strftime("%d.%m.%Y")


    
    

class Status(models.Model):
    status = models.CharField('Статус', max_length=50)

    def __str__(self):
            return self.status