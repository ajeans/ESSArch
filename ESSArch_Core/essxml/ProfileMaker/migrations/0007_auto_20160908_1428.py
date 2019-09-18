"""
    ESSArch is an open source archiving and digital preservation system

    ESSArch
    Copyright (C) 2005-2019 ES Solutions AB

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.

    Contact information:
    Web - http://www.essolutions.se
    Email - essarch@essolutions.se
"""

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileMaker', '0006_auto_20160902_1308'),
    ]

    operations = [
        migrations.DeleteModel(
            name='finishedTemplate',
        ),
        migrations.RemoveField(
            model_name='templatepackage',
            name='generated',
        ),
        migrations.AddField(
            model_name='templatepackage',
            name='namespace',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='templatepackage',
            name='root_element',
            field=models.CharField(default='', max_length=55),
        ),
    ]
