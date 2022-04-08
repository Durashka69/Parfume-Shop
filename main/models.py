from django.db import models
from django.contrib.auth.models import User

from main.choices import ScoreChoice

from itertools import chain


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название продукта')
    year = models.PositiveSmallIntegerField(verbose_name='Год выпуска')
    image = models.ImageField(upload_to='pictures',
                              verbose_name='Изображение продукта', blank=True, null=True)
    brand = models.ForeignKey(
        'Brand', on_delete=models.CASCADE, verbose_name='Бренд', related_name='brands')
    volume = models.ForeignKey(
        'Volume', on_delete=models.CASCADE, related_name='volume', verbose_name='Объем')
    purpose = models.ForeignKey(
        'Purpose', on_delete=models.CASCADE, verbose_name='Назначение', related_name='purposes')
    type_of = models.ForeignKey(
        'Type_of', on_delete=models.CASCADE, verbose_name='Тип продукта')
    price = models.PositiveIntegerField(verbose_name='Цена продукта')
    code = models.PositiveIntegerField(verbose_name='Код товара')
    family = models.ForeignKey(
        'Family', on_delete=models.CASCADE, verbose_name='Семейство')
    notes = models.ForeignKey(
        'Note', on_delete=models.CASCADE, verbose_name='Ноты продукта')
    description = models.TextField(verbose_name='Описание продукта')
    for_men = models.BooleanField(default=True, verbose_name='Для мужчин')
    available = models.BooleanField(default=True)

    @property
    def raiting(self):
        raitings = self.raitings.values_list("value")
        if raitings:
            return sum(chain(*raitings)) / len(raitings)
        else:
            return None

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title']


class Volume(models.Model):
    value = models.FloatField(default=0, verbose_name='Объём')

    def __str__(self):
        return f'{self.value} мл'

    class Meta:
        verbose_name = 'Объём'
        verbose_name_plural = 'Объемы'


class Brand(models.Model):
    title = models.CharField(max_length=255, verbose_name='Бренд')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        ordering = ['title']


class Purpose(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назначение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Назначение'
        verbose_name_plural = 'Назначения'
        ordering = ['title']


class Type_of(models.Model):
    title = models.CharField(max_length=255, verbose_name='Тип')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
        ordering = ['title']


class Family(models.Model):
    title = models.CharField(max_length=255, verbose_name='Семейство')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Семейство'
        verbose_name_plural = 'Семейcтсва'
        ordering = ['title']


class Note(models.Model):
    title = models.CharField(max_length=255, verbose_name='Нота')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Нота'
        verbose_name_plural = 'Ноты'
        ordering = ['title']


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='comments', verbose_name='Продукт')
    content = models.TextField(verbose_name='Содержание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Reply(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь')
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='replies', verbose_name='Комментарий')
    content = models.TextField(verbose_name='Содержание ответа')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    def __str__(self):
        return 'Reply'

    class Meta:
        verbose_name = 'Ответ на комментарий'
        verbose_name_plural = "Ответы на комментарии"


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Пользователь', related_name='rating')
    score = models.PositiveSmallIntegerField(
        choices=ScoreChoice.choices, verbose_name='Оценка')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='ratings')

    def __str__(self):
        return f'{self.score} - {self.product}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
