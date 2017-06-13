# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from assignment.models import User, User_team, User_resource
from django.core import serializers
from django.http import HttpResponse
from itertools import chain
from operator import attrgetter

from django.shortcuts import render


# Create your views here.

def user_profile(request, usn=1):

    queryset = User.objects.filter(usn=usn)
    queryset2 = User_team.objects.filter(usn=usn)
    queryset3 = User_resource.objects.filter(usn=usn)

    result_list = sorted(chain(queryset,queryset2,queryset3),key=lambda instance: instance.usn)
    print(result_list[1].team_id)

    print("??????????")
    print(result_list)

    for e in queryset:
        for e2 in queryset2:
            for e3 in queryset3:
              print("Usn = {} Username = {} Token = {} Trophy = {} Team_Id = {}".format(e.usn,
                                                                                        e.username,
                                                                                        e.token,
                                                                                        e3.trophy,
                                                                                        e2.team_id))

    queryset = serializers.serialize('json', queryset)
    queryset2 = serializers.serialize('json', queryset2)
    queryset3 = serializers.serialize('json', queryset3)

    total = queryset3

    userQueries = User.objects.all()
    user_teamQueries = User_team.objects.filter()
    user_resourceQueries = User_resource.objects.all()

    str = ''

    # for userQuery in userQueries:
    #
    #     str = "<p>No. {} Name. {} Token. {} Trophy. {} Team. {}<p>".format(userQuery.usn,
    #                                                                       userQuery.username,
    #                                                                       userQuery.token,
    #                                                                       user_resourceQueries.trophy,
    #                                                                       user_teamQueries.team_id)

    # return HttpResponse(str)

    return HttpResponse(total, content_type="application/json")
