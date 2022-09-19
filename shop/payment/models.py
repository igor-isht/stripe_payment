from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models
from market.models import Item

User = get_user_model()


class Discount(models.Model):
    coupon_id = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    percent_off = models.FloatField(blank=True, null=True)
    amount_off = models.PositiveSmallIntegerField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"


class Order(models.Model):
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cart", verbose_name="Клиент"
    )
    items = models.ManyToManyField(
        Item,
        through="ItemInCart",
        related_name="items",
        verbose_name="Товары в корзине",
    )
    discount = models.ForeignKey(
        Discount,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="discount",
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class ItemInCart(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order",
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
    )
