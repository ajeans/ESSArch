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
# Generated by Django 1.10 on 2016-12-20 09:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ip', '0025_auto_20161216_1621'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='informationpackage',
            options={'ordering': ['id'], 'permissions': (('set_uploaded', 'Can set IP as uploaded'), ('create_sip', 'Can create SIP'), ('submit_sip', 'Can submit SIP'), ('transfer_sip', 'Can transfer SIP'), ('change_sa', 'Can change SA connected to IP'), ('lock_sa', 'Can lock SA to IP'), ('unlock_profile', 'Can unlock profile connected to IP')), 'verbose_name': 'Information Package'},
        ),
    ]
