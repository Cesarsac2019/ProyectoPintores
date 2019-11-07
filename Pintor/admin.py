# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from django.contrib import admin
from pintura.models import Pintor, PintorAdmin, Pintura, PinturaAdminlaAdmin

admin.site.register(Pintor, PintorAdmin)
admin.site.register(Pintura, PinturaAdmin)
