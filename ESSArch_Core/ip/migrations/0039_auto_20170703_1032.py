# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-03 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ip', '0038_auto_20170608_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informationpackage',
            name='message_digest_algorithm',
            field=models.IntegerField(choices=[(0, b'MD5'), (1, b'SHA-1'), (2, b'SHA-224'), (3, b'SHA-256'), (4, b'SHA-384'), (5, b'SHA-512')], null=True),
        ),
        migrations.AlterField(
            model_name='informationpackagemetadata',
            name='message_digest_algorithm',
            field=models.IntegerField(choices=[(0, b'MD5'), (1, b'SHA-1'), (2, b'SHA-224'), (3, b'SHA-256'), (4, b'SHA-384'), (5, b'SHA-512')], null=True),
        ),
    ]