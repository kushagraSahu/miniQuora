# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-25 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20160322_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='gender',
            field=models.CharField(default='M', max_length=1),
        ),
    ]
