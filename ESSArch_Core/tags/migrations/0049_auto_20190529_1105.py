# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-29 09:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0048_auto_20190529_1043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery',
            options={'verbose_name': 'delivery', 'verbose_name_plural': 'deliveries'},
        ),
        migrations.AlterModelOptions(
            name='transfer',
            options={'verbose_name': 'transfer', 'verbose_name_plural': 'transfers'},
        ),
    ]