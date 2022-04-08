from django.db import models
from django.contrib.auth.models import User

from itertools import chain

from main.models import Product

from cart.choices import StatusChoice


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Корзина', related_name='cart')
    products = models.ManyToManyField(
        Product, through='CartItem', related_name='cart')

    @property
    def total_price(self):
        prices = self.cart_products.annotate(
            last_price=models.F('product__price') * models.F('amount')
        ).values_list('last_price')
        return sum(chain(*prices))

    def __str__(self):
        return f'{self.user.username} - {self.total_price}'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class CartItem(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='cart_products')
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='cart_products')
    quantity = models.PositiveIntegerField(
        default=1, verbose_name='Количество')
    order = models.ForeignKey(
        'Order', on_delete=models.CASCADE, verbose_name='Заказ', related_name='cart_products', null=True)

    @property
    def final_price(self):
        return self.product.price * self.amount

    @property
    def price(self):
        return self.product.price

    @property
    def title(self):
        return self.product.title

    def __str__(self):
        return f"{self.amount} {self.final_price}"

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'


class Order(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, null=True, blank=True)
    descriptions = models.CharField(max_length=255, null=True)
    price = models.PositiveIntegerField()
    status = models.CharField(
        max_length=15, choices=StatusChoice.choices, default=StatusChoice.ORDER)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
