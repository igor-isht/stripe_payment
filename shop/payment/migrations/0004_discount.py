# Generated by Django 3.2.15 on 2022-09-19 13:25

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0003_order_quantity"),
    ]

    operations = [
        migrations.CreateModel(
            name="Discount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "percent_off",
                    models.PositiveSmallIntegerField(
                        validators=[django.core.validators.MaxValueValidator(100)]
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order",
                        to="payment.order",
                        verbose_name="Заказ со скидкой",
                    ),
                ),
            ],
            options={
                "verbose_name": ("Скидка",),
                "verbose_name_plural": "Скидки",
                "ordering": ["-id"],
            },
        ),
    ]
