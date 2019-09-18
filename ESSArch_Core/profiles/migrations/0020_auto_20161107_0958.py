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
# Generated by Django 1.10 on 2016-11-07 08:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0019_auto_20161106_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileIP',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Unlockable', models.BooleanField(default=False)),
                ('LockedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('ip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ip.InformationPackage')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileSA',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Unlockable', models.BooleanField(default=False)),
                ('LockedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
                ('submission_agreement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.SubmissionAgreement')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='profilesalock',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='profilesalock',
            name='LockedBy',
        ),
        migrations.RemoveField(
            model_name='profilesalock',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='profilesalock',
            name='submission_agreement',
        ),
        migrations.AlterUniqueTogether(
            name='saiplock',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='saiplock',
            name='LockedBy',
        ),
        migrations.RemoveField(
            model_name='saiplock',
            name='information_package',
        ),
        migrations.RemoveField(
            model_name='saiplock',
            name='submission_agreement',
        ),
        migrations.DeleteModel(
            name='ProfileSALock',
        ),
        migrations.DeleteModel(
            name='SAIPLock',
        ),
        migrations.AlterUniqueTogether(
            name='profilesa',
            unique_together=set([('profile', 'submission_agreement')]),
        ),
        migrations.AlterUniqueTogether(
            name='profileip',
            unique_together=set([('profile', 'ip')]),
        ),
    ]
