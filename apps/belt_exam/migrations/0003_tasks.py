# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_exam', '0002_remove_user_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=255)),
                ('time', models.TimeField()),
            ],
        ),
    ]
