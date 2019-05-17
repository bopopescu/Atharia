# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-04 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dominion', '0029_auto_20180731_0001'),
        ('character', '0024_auto_20180310_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='storyemit',
            name='orgs',
            field=models.ManyToManyField(blank=True, related_name='emits', to='dominion.Organization'),
        ),
    ]
