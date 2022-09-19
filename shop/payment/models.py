from operator import mod
from statistics import mode
from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator

from market.models import Item

User = get_user_model()

class Discount(models.Model):
    percent_off = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(100)]
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Скидка',
        verbose_name_plural = 'Скидки'
        

class Order(models.Model):
    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='Покупатель'
    )
    items = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='покупки в корзине'
    )
    discount = models.ForeignKey(
        Discount,
        on_delete=models.CASCADE,
        related_name='discount',
        verbose_name='скидка'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Корзина',
        verbose_name_plural = 'Корзины'

