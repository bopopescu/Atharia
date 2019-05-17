# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-05-14 06:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0009_investigation_roll'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField(blank=True)),
                ('wrote_short_rel', models.BooleanField(default=False)),
                ('wrote_journal', models.BooleanField(default=False)),
                ('from_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initiated_contacts', to='character.AccountHistory')),
                ('to_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_contacts', to='character.AccountHistory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='accounthistory',
            name='contacts',
            field=models.ManyToManyField(blank=True, null=True, related_name='_accounthistory_contacts_+', through='character.FirstContact', to='character.AccountHistory'),
        ),
    ]
