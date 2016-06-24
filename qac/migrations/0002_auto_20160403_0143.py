# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-02 20:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qac', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer_text',
            new_name='text',
        ),
        migrations.AddField(
            model_name='answer',
            name='answered_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers_written', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='qac.Question'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comments_text',
            field=models.TextField(default='', max_length=200),
        ),
    ]