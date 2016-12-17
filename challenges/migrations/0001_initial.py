# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-14 18:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IdentityLeakCheckerChallenge',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('NOT_STARTED', 'Not started'), ('IN_PROGRESS', 'In progress'), ('DONE', 'Done'), ('ERROR', 'Error')], default='NOT_STARTED', max_length=11)),
                ('message', models.CharField(blank=True, max_length=140)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TorChallenge',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('NOT_STARTED', 'Not started'), ('IN_PROGRESS', 'In progress'), ('DONE', 'Done'), ('ERROR', 'Error')], default='NOT_STARTED', max_length=11)),
                ('message', models.CharField(blank=True, max_length=140)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
