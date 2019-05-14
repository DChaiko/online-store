from django.shortcuts import render
from django.views.generic.edit import UpdateView
from cart.models import BookInCart, Cart
from django.urls import reverse_lazy
from books.models import Book

# Create your views here.

class AddIntoCart(UpdateView):
    model = BookInCart
    fields = ['book', 'quantity']
    success_url = reverse_lazy('home')
    def get_object(self, queryset=None):
        user = None
        if self.request.user.is_authenticated:
            user = self.request.user
        cart_id = self.request.session.get('cart-id')
        print(user)
        print (cart_id)
        cart, created = Cart.objects.get_or_create(pk=cart_id, defaults={'user': user})
        if created:
            self.request.session['cart-id'] = cart.pk
        book = Book.objects.get(pk=self.kwargs['pk'])
        book_in_cart, created = self.model.objects.get_or_create(cart = cart, book = book, defaults={'cart': cart, 'book': book, 'quantity': '1'})
        return book_in_cart

