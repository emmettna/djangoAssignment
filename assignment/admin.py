# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User, User_team, User_resource, Match_list, Team_list, User_rank, Bet_list, Bet_history
from .models import Player_table, Comp_table

# Register your models here.

admin.site.register(User)
admin.site.register(User_resource)
admin.site.register(User_team)
admin.site.register(Match_list)
admin.site.register(Team_list)
admin.site.register(User_rank)
admin.site.register(Bet_list)
admin.site.register(Bet_history)
admin.site.register(Player_table)
admin.site.register(Comp_table)