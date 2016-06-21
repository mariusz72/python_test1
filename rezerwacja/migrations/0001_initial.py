# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klienci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=20, verbose_name='Imie')),
                ('mazwisko', models.CharField(max_length=40, verbose_name='Nazwisko')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Klient',
                'verbose_name_plural': 'Klienci',
            },
        ),
        migrations.CreateModel(
            name='Rezerwacje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_rezerwacji', models.DateTimeField(auto_now_add=True, verbose_name='Data rezerwacji')),
                ('imie', models.CharField(max_length=20, verbose_name='Imie')),
                ('nazwisko', models.CharField(max_length=40, verbose_name='Nazwisko')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('stolik', models.IntegerField(verbose_name='Stolik')),
                ('od', models.DateTimeField(verbose_name='Data od')),
                ('do', models.DateTimeField(verbose_name='Data do')),
                ('ileosob', models.IntegerField(verbose_name='Ilosc osob')),
            ],
            options={
                'verbose_name': 'Rezerwacja',
                'verbose_name_plural': 'Rezerwacje',
            },
        ),
        migrations.CreateModel(
            name='Stoliki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr_stolika', models.IntegerField(verbose_name='Nr Stolika')),
                ('ile_osob', models.IntegerField(verbose_name='Ile Osob')),
            ],
            options={
                'verbose_name': 'Stolik',
                'verbose_name_plural': 'Stoliki',
            },
        ),
    ]
