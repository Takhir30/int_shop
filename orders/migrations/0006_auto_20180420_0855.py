# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-20 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_productinbasket_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Товар в заказе', 'verbose_name_plural': 'Товары в заказе'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус заказа', 'verbose_name_plural': 'Статусы заказа'},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customer_adress',
            new_name='customer_address',
        ),
        migrations.AddField(
            model_name='productinorder',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]