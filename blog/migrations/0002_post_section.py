# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='section',
            field=models.CharField(default='home', max_length=15),
        ),
    ]
