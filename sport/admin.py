# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Team, Footballer
from django.contrib import admin

# Register your models here.
admin.site.register(Team)
admin.site.register(Footballer)