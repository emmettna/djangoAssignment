# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from assignment.models import User, User_team, User_resource
from django.core import serializers
from django.http import HttpResponse
from itertools import chain
import json
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


    Usn = ''
    Username = ''
    Token = ''
    Trophy = ''
    Team_Id = []

    for e in queryset:
        for e2 in queryset2:
            for e3 in queryset3:

                Usn = e.usn
                Username =e.username
                Token= e.token
                Trophy = e3.trophy
                Team_Id.append(e2.team_id)
    print('Values here', Usn, Username,Token,Trophy,Team_Id)

    targetObject ={'usn' : Usn,
                   'username': Username,
                   'token' : Token,
                   'trophy' : Trophy,
                   'team_id' : Team_Id
    }
    targetConverted = json.dumps(targetObject)

    # for userQuery in userQueries:
    #
    #     str = "<p>No. {} Name. {} Token. {} Trophy. {} Team. {}<p>".format(userQuery.usn,
    #                                                                       userQuery.username,
    #                                                                       userQuery.token,
    #                                                                       user_resourceQueries.trophy,
    #                                                                       user_teamQueries.team_id)
    # return HttpResponse(str)

    return HttpResponse(targetConverted, content_type="application/json")
