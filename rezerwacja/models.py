from __future__ import unicode_literals

# -*- coding: utf-8 -*-
from django.db import models



class Stoliki(models.Model):
    nr_stolika = models.IntegerField('Nr Stolika')
    ile_osob = models.IntegerField('Ile Osob')

    class Meta:
        verbose_name = "Stolik"
        verbose_name_plural = "Stoliki"


class Rezerwacje(models.Model):
    data_rezerwacji = models.DateTimeField('Data rezerwacji', auto_now_add=True)
    imie = models.CharField('Imie', max_length=20)
    nazwisko = models.CharField('Nazwisko', max_length=40)
    email = models.EmailField('Email', max_length=254)
    stolik = models.IntegerField('Stolik')
    od = models.DateTimeField('Data od')
    do = models.DateTimeField('Data do')
    ileosob = models.IntegerField('Ilosc osob')

    class Meta:
        verbose_name = "Rezerwacja"
        verbose_name_plural = "Rezerwacje"

    def __unicode__(self):
        return self.imie + " " + self.nazwisko        



