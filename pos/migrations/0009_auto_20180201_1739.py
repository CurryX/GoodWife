# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-01 09:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0008_auto_20180201_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='change',
            new_name='balance',
        ),
    ]
