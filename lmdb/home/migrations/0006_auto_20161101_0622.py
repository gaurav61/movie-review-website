# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-01 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
