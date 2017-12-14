# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-14 18:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footballer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('position', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('which_league', models.CharField(max_length=250)),
                ('number_of_champions', models.CharField(max_length=250)),
                ('logo', models.CharField(max_length=10000)),
            ],
        ),
        migrations.AddField(
            model_name='footballer',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.Team'),
        ),
    ]
