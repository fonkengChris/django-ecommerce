# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-04-15 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
