# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User, User_team, User_resource

# Register your models here.

admin.site.register(User)
admin.site.register(User_resource)
admin.site.register(User_team)