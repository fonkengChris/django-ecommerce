# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-04-23 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_guestemail_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestemail',
            name='email',
            field=models.EmailField(default='guest_email', max_length=254),
        ),
    ]
