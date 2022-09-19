# Generated by Django 3.2.15 on 2022-09-19 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0007_auto_20220919_1435"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="discount",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="discount",
                to="payment.discount",
                verbose_name="скидка",
            ),
        ),
    ]