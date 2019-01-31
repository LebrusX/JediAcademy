# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-29 06:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='имя')),
                ('age', models.IntegerField(verbose_name='возраст')),
                ('email', models.EmailField(max_length=254, verbose_name='почта')),
            ],
        ),
        migrations.CreateModel(
            name='Jedi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='имя')),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='название')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.CharField(max_length=30, verbose_name='код ордена')),
                ('questions', models.CharField(max_length=50, verbose_name='тестовые вопросы')),
            ],
        ),
        migrations.AddField(
            model_name='jedi',
            name='edu_planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedi.Planet'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='homeplanet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedi.Planet'),
        ),
    ]
