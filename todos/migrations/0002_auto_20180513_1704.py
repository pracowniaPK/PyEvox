# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-13 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='author_ip',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]