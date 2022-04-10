from django.db import models
from django.contrib.auth.models import User

from itertools import chain

from main.models import Product


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Корзина', related_name='cart')
    products = models.ManyToManyField(
        Product, through='CartItem', related_name='cart')

    @property
    def total_price(self):
        prices = self.cart_products.annotate(
            last_price=models.F('product__price') * models.F('quantity')
        ).values_list('last_price')
        return sum(chain(*prices))

    def __str__(self):
        return f'{self.user.username} - {self.total_price}'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class CartItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='cart_products')
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='cart_products')
    quantity = models.PositiveSmallIntegerField(
        default=1, verbose_name='Количество')
    order = models.ForeignKey(
        'Order', on_delete=models.CASCADE, verbose_name='Заказ', related_name='cart_products', null=True)

    @property
    def final_price(self):
        return self.product.price * self.quantity

    @property
    def price(self):
        return self.product.price

    @property
    def title(self):
        return self.product.title

    def __str__(self):
        return f"{self.quantity} {self.final_price}"

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'


class Order(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    number = models.CharField(max_length=13, verbose_name='Номер телефона')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    email = models.EmailField(max_length=255, null=True, blank=True, verbose_name='Email')
    descriptions = models.CharField(max_length=255, null=True, verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders", verbose_name='Пользователь')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
