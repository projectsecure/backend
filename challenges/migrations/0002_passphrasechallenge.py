# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-28 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassphraseChallenge',
            fields=[
                ('challenge_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='challenges.Challenge')),
                ('check_passphrase_status', models.CharField(choices=[('NOT_STARTED', 'Not started'), ('IN_PROGRESS', 'In progress'), ('COMPLETED', 'Completed'), ('ERROR', 'Error')], default='NOT_STARTED', max_length=11)),
            ],
            options={
                'abstract': False,
            },
            bases=('challenges.challenge',),
        ),
    ]