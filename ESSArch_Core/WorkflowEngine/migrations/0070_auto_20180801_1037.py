# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-01 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkflowEngine', '0069_processtask_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processstep',
            name='hidden',
            field=models.BooleanField(db_index=True, default=False, editable=False),
        ),
    ]
