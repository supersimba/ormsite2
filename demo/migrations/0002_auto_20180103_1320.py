# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-03 05:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '\u4f5c\u8005', 'verbose_name_plural': '\u4f5c\u8005'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '\u8457\u4f5c', 'verbose_name_plural': '\u8457\u4f5c'},
        ),
        migrations.AlterModelTable(
            name='author',
            table='author',
        ),
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
    ]