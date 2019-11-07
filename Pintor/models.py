# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.

class Pintor(models.Model):

    nombre  =   models.CharField(max_length=30)
    Apellido =  models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    telefono = models.IntegerField()


    def __str__(self):

        return self.nombre

class Puntura(models.Model):
    nombre    = models.CharField(max_length=60)
    codigo    = models.IntegerField()
    color     = models.CharField(max_length=60)


pinturas   = models.ManyToManyField(Pintor, through='Actuacion')

    def __str__(self):

        return self.nombre


class Color (models.Model):

    pintor = models.ForeigxnKey(Pintor, on_delete=models.CASCADE)

    pintura = models.ForeignKey(Puntura, on_delete=models.CASCADE)

class ActuacionInLine(admin.TabularInline):

    model = Color

    extra = 1


class PintorAdmin(admin.ModelAdmin):

    inlines = (ActuacionInLine,)


class PinturaAdmin (admin.ModelAdmin):

    inlines = (ActuacionInLine,)
