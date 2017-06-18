# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User, User_team, User_resource, Match_list, Team_list

# Register your models here.

admin.site.register(User)
admin.site.register(User_resource)
admin.site.register(User_team)
admin.site.register(Match_list)
admin.site.register(Team_list)
