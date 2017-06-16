# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from assignment.models import User, User_team, User_resource, Match_list
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

    JSon_Object = json.dumps(object_Dictation)

    return HttpResponse(JSon_Object, content_type="application/json")


    # Take usn as a parameter then get user details which team the user likes
    # Then it searches both home and away team match
    # Finally wrap the details and return json object

def match_list(request, usn=1):

    queryset = User_team.objects.filter(usn=usn)

    team_Id = []

    # Get data from user_team and put it in team_id list

    for e in queryset:
        team_Id.append(e.team_id)

    # Match the team ids with match list. if it matches either home or away or both
    # Then it returns.
    # issue
    # #1 home_team_id is not being matched with integer cuz it's an object not integer

    queryset2 = Match_list.objects.filter(home_team_id__in=team_Id)
    queryset3 = Match_list.objects.all()

    print(queryset2)




    object_Dictation_Processed = {'usn' : usn,
                        'match_list' : match_list
                        }

    return HttpResponse(queryset3,content_type="application/json")