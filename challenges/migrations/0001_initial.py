# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-27 17:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('NOT_STARTED', 'Not started'), ('IN_PROGRESS', 'In progress'), ('COMPLETED', 'Completed'), ('ERROR', 'Error')], default='NOT_STARTED', max_length=11)),
                ('message', models.CharField(blank=True, max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='IdentityLeakCheckerChallenge',
            fields=[
                ('challenge_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='challenges.Challenge')),
                ('check_email_status', models.CharField(choices=[('NOT_STARTED', 'Not started'), ('IN_PROGRESS', 'In progress'), ('COMPLETED', 'Completed'), ('ERROR', 'Error')], default='NOT_STARTED', max_length=11)),
            ],
            options={
                'abstract': False,
            },
            bases=('challenges.challenge',),
        ),
        migrations.CreateModel(
            name='TorChallenge',
            fields=[
                ('challenge_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='challenges.Challenge')),
                ('check_tor_connection_status', models.CharField(choices=[('NOT_STARTED', 'Not started'), ('IN_PROGRESS', 'In progress'), ('COMPLETED', 'Completed'), ('ERROR', 'Error')], default='NOT_STARTED', max_length=11)),
            ],
            options={
                'abstract': False,
            },
            bases=('challenges.challenge',),
        ),
        migrations.AddField(
            model_name='challenge',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_challenges.challenge_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='challenge',
            unique_together=set([('user', 'polymorphic_ctype')]),
        ),
    ]
