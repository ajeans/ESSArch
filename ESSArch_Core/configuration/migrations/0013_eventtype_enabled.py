# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-21 08:01
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0012_auto_20170802_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtype',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
