# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 21:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt_exam', '0003_tasks'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tasks',
        ),
    ]