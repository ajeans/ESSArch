# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-22 11:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WorkflowEngine', '0001_initial'),
        ('tags', '0013_auto_20180925_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tags', to='WorkflowEngine.ProcessTask'),
        ),
        migrations.AddField(
            model_name='tagstructure',
            name='structure_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tags.StructureUnit'),
        ),
    ]
