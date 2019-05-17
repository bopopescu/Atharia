# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-04-13 03:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dominion', '0008_auto_20170211_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='crisisaction',
            name='economic',
            field=models.PositiveSmallIntegerField(blank=0, default=0, help_text=b'Additional economic resources added by the player'),
        ),
        migrations.AddField(
            model_name='crisisaction',
            name='military',
            field=models.PositiveSmallIntegerField(blank=0, default=0, help_text=b'Additional military resources added by the player'),
        ),
        migrations.AddField(
            model_name='crisisaction',
            name='secret_action',
            field=models.TextField(blank=True, verbose_name=b'Secret actions the player is taking'),
        ),
        migrations.AddField(
            model_name='crisisaction',
            name='silver',
            field=models.PositiveSmallIntegerField(blank=0, default=0, help_text=b'Additional silver added by the player'),
        ),
        migrations.AddField(
            model_name='crisisaction',
            name='social',
            field=models.PositiveSmallIntegerField(blank=0, default=0, help_text=b'Additional social resources added by the player'),
        ),
        migrations.AddField(
            model_name='crisisactionassistant',
            name='can_see_secret',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='crisisactionassistant',
            name='secret_action',
            field=models.TextField(blank=True, verbose_name=b'Secret action the assistant is taking'),
        ),
        migrations.AddField(
            model_name='crisisactionassistant',
            name='share_secret',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='militaryunit',
            name='orders',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='units', to='dominion.Orders'),
        ),
        migrations.AddField(
            model_name='orders',
            name='action',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='dominion.CrisisAction'),
        ),
        migrations.AddField(
            model_name='orders',
            name='assisting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assisting_orders', to='dominion.Orders'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, b'Troop Training'), (2, b'Explore territory'), (3, b'Raid Domain'), (4, b'Conquer Domain'), (5, b'Enforce Order'), (6, b'Besiege Castle'), (7, b'March'), (8, b'Defend'), (9, b'Patrol'), (10, b'Assist')], default=1),
        ),
    ]
