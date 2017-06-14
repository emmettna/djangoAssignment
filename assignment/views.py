# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from assignment.models import User, User_team, User_resource
from django.http import HttpResponse
from django.template import loader
import json
from django.shortcuts import render


# Create your views here.

# Takes usn as parameter ~/user_profile/(usn)
# By usn number, function decides which user to retrieve from Database
# Through the for loops, values assigned to variables
# JSon object returned as requested


def user_profile(request, usn=1):

    #Version1 sending via user_profile.html

    # anotherqueryset = User.objects.filter(usn=usn)
    # anotherqueryset2 = User_team.objects.filter(usn=usn)
    # anotherqueryset3 = User_resource.objects.filter(usn=usn)
    #
    # list = []
    # list.append(anotherqueryset2)
    # for e in anotherqueryset2:
    #     list.append(e.team_id)
    # print(list)
    #
    # context = {
    #     'User' : anotherqueryset,
    #     'User_team' : list,
    #     'User_resource' : anotherqueryset3
    # }
    # return render(request,'user_profile.html',context)

    # Version2 sending JSon file directly

    queryset = User.objects.filter(usn=usn)
    queryset2 = User_team.objects.filter(usn=usn)
    queryset3 = User_resource.objects.filter(usn=usn)

    usn = ''
    username = ''
    token = ''
    trophy = ''
    team_Id = []

    for e in queryset:
        for e2 in queryset2:
            for e3 in queryset3:
                usn = e.usn
                username = e.username
                token= e.token
                trophy = e3.trophy
                team_Id.append(e2.team_id)

    object_Dictation = {'usn': usn,
                        'username': username,
                        'token': token,
                        'trophy': trophy,
                        'team_id': team_Id}

    object_JSon = json.dumps(object_Dictation)

    return HttpResponse(object_JSon, content_type="application/json")
